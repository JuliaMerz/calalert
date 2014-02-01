from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from twilio import twiml
from twilio.rest import TwilioRestClient
import time
import threading
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
import os


TWILIO_ACCOUNT_SID = 'AC4745c2a611c2c4eda07ec50245065641'
TWILIO_AUTH_TOKEN = '93cea5d8882178bfdec8abae2c18cf67'
TWILIO_NUMBER = '+1 408-916-4543'

RSS_WAIT_TIME=60

# create an authenticated client that can make requests to Twilio for your
# account.
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

FEEDCHECK_ACTIVE = True

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models, lookups, backend, inserts

'Initialize the feed checking loop'
def feedchecker():
    while FEEDCHECK_ACTIVE:
        backend.checkfeeds()
        time.sleep(RSS_WAIT_TIME)

thread = threading.Thread(target = feedchecker)
thread.start()
