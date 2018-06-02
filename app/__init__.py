# This file initializes the app directory into a python module

# Third-party Imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# app variable initialization
app = Flask(__name__, instance_relative_config=True)

# db variable initialization
db = SQLAlchemy()

login_manager = LoginManager()

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://kpbgvfvexcjuui:3f5ba960fdd401fd5aa9a6bf9497675d7057ab887a222cf5ed2494515f404392@ec2-54-225-96-191.compute-1.amazonaws.com:5432/ddp8g4fesva0gh'
app.secret_key = """ MIIEpQIBAAKCAQEAyemBIproxmW2KresUf2ex6StlQmcWgbxn9GhB9OkFUjRM7NF
MFLnZQONkbOhQNE1m8uQW3KjEnWtpBCTjoocN5SS9mbLC/w8JVx0poiJFoCGWUYE
2HTt/msL1mHn0LI9EMnPZ3nhaGz3n4p1W3pwKCh6KCXLsyaAzjU9Z6AEJsm28BxY
Nn+N866t21XJIzYIOQrd5drrf2a7gqjGs64CsZgM+Ill2mRuKOFacw1+xTP/bni7
0GiOThSBaFmyjD5tfibG4oEK5MQcl4PennBds7hEpmWxKs5sgA87pqtD/2mGk3pZ
MLY20G4J4u5wqyv8sTfI7CSfOlNXwU+ZMzeMIwIDAQABAoIBAQCBe8lgk88rTBbi
lh9gBTFJ/oWCykMGSOWzBBAsoMDdFXFzokeAkenqkbi782I52vByFL1ip8WEFQth
5295PYCS9Ci683jLGtrHat8z3ONtFscRgSGiXnoxahyRQwASifs3RPRI+5ReD2NN
YNGZ9I7wceTE0lgrb0my89mJFskSxazUvxq+mmbRJw2tSGr/7gqNTJr5Uyuf0bFr
a/PxC1Q6GhBfKDxAI9rksND49L9R5uesIzLSwwACpAP/abl2jVeiVv355m8luNcv
XfbXDSnM1HrPRyNa7S3o+SEm+/uvAPeyg48/fw2k/Er2dwQCHvjVSmA5QTq60iK2
06ZsoMhhAoGBAPMqkCEcQq2cFfuDfhAEBVAzrv+nBPZts6+FXdugw83P8RjpqG5L
0xlFtC0Z5cCKiQKeRIATEQZGg8NFiWB0GU0sSrUbmAS25OCSsYXC75Oq3JW4PynW
cAGRW2O9++DBGsNRa/7tON7zC4yDgX1gZek0CzC3ouw/T8BshgrhjUBdAoGBANSR
jccWZ9Kaat+vDjmq/RlpIzG1Ck+wCaGnsOmt1IOk0uqlWf15qYHcgJd+l+RkfRMp
XIO5s1IZt4olKqjhNbrLQMRQ7w9plwlKTYWJP3AXojWL+SU/wMXfboNKIxRVD3Je
z5pMwjDhig7vYnVeS8vIMq0vdEx0GfLW1O03xTZ/AoGBAJa8wc/kpujcIzxgzNq8
w1ZuU4MjVA42/vZFZGNrizWgO8LHxaNp2ZiG/yQeM7BhsIEw/yGtsBYFzFRWXMyv
66dNV5phWqFBhyw3g1h5+O2/MzKUnoMe7RvrsY1pDiTLT/3YEWxcPa7nVzdppfHE
uigQHQe8LoDo1lVgcM959of5AoGAXScsKoL3HKPvEfd1FHCKWghpE+9yhVlv3xfN
v5od91LT22B6/0nBrtciw0EG71/aL/uAP3mxy9jZRgDjoP6QvTs1NtMA8JAlUDzv
nAV5d3Xj7/NXS6uUnyI7G+3xUYe1LTm/YK8iqqksBz+Atk6MiNFC5AJXxOlcNb9P
sGUwV6ECgYEA5f7jNzf81vLtyBdf6pqRCnRk6pKmpwjg8Frcn95NwLZa401gqYAJ
mgBjYzNhx73gvNBpqJHCsbzCgT0qRLxrOJHR6Hl+5f3fTh1Z4tVp7MA7QfvFQzgi
WRdVAldhoDRsftRTuisN2EPZLfE0pq+SXHxh/do9XmdkuEOuOl63awc=


                 """
db.init_app(app)

Bootstrap(app)

from app import models

login_manager.init_app(app)

from app import models

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint

app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run()
