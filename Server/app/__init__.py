from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from twilio import twiml
from twilio.rest import TwilioRestClient

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = 'AC4745c2a611c2c4eda07ec50245065641'
TWILIO_AUTH_TOKEN = '93cea5d8882178bfdec8abae2c18cf67'
TWILIO_NUMBER = '+1 408-916-4543'

# create an authenticated client that can make requests to Twilio for your
# account.
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models, lookups, backend, inserts
