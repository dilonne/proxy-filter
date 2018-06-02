from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
from ..models import BlackListedWebsite


class BlackListedWebsiteForm(FlaskForm):
    url = StringField('Website url', validators=[DataRequired()])
    submit = SubmitField('Save')

    @staticmethod
    def validate_url(self, field):
        if BlackListedWebsite.query.filter_by(url=field.data).first():
            raise ValidationError('Website url is already registered')



