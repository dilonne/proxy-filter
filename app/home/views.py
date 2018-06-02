from flask import render_template, redirect, flash, url_for, abort, request
from flask_login import login_required
from .forms import BlackListedWebsiteForm
import urllib.request

from . import home
from ..models import BlackListedWebsite, ServerResponse
from app import db, app


@home.route('/')
def index():
    return redirect('/login')


@home.route('/blacklisted_website', methods=['GET', 'POST'])
@login_required
def add_blacklisted_website():
    form = BlackListedWebsiteForm()

    if form.validate_on_submit():
        blacklisted_website = BlackListedWebsite(url=form.url.data)

        db.session.add(blacklisted_website)
        db.session.commit()
        return redirect('/blacklisted_websites')

    else:
        return render_template('home/blacklisted_websites/add.html', form=form, title='Add Blacklisted Website')


@home.route('/blacklisted_website/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blacklisted_website(id):

    blacklisted_website = BlackListedWebsite.query.get_or_404(id)
    db.session.delete(blacklisted_website)
    db.session.commit()
    flash('You have successfully deleted the blacklisted website')

    return redirect(url_for('home.list_blacklisted_websites'))


@home.route('/blacklisted_websites', methods=['GET', 'POST'])
@login_required
def list_blacklisted_websites():
    blacklisted_websites = BlackListedWebsite.query.all()
    return render_template('home/blacklisted_websites/list.html', blacklisted_websites=blacklisted_websites, title='BlackListed Websites')


@home.route('/is_blacklisted')
def is_blacklisted():
    url = request.args.get('hostname')
    if BlackListedWebsite.query.filter_by(url=url).first():
        server_response = ServerResponse(0, "Blacklisted")
        urllib.request.urlopen(
            'http://www.bluedotsms.com/api/mt/SendSMS?user=omri&password=marebera87&senderid=PROXYFILTER&channel=Normal&DCS=0&flashsms=0&number=0782641637&text=HOST%20IS%20TRYING%20TO%20ACCESS%20RESTRICTED%20WEBSITE')
        return server_response.to_json()
    else:
        server_response = ServerResponse(1, "Approved")
        return server_response.to_json()

