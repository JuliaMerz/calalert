from app import client, app, db, models, lookups 
from flask import request
import datetime
import feedparser

TWILIO_ACCOUNT_SID = 'AC4745c2a611c2c4eda07ec50245065641'
TWILIO_AUTH_TOKEN = '93cea5d8882178bfdec8abae2c18cf67'
TWILIO_NUMBER = '+1 408-916-4543'

TYPE_SENSOR = 1
TYPE_FEED = 2
MIN_TIME = 120
PRIORITY_TO_STRING = {3:'EMERGENCY', 2:'URGENT', 1:'ALERT'}

@app.route('/alert', methods=['POST'])
def alert():
    mac = request.data
    alert_sensor = lookups.get_sensor_from_mac(mac)
    if alert_sensor == None:
        return 'No thing found'
    alert_requests = lookups.get_requests_by_sid(alert_sensor.id)
    
    'For every alert_request process if an alert needs to be sent and send it'
    for cur_alert_request in alert_requests:

        most_recent=lookups.get_most_recent_alert_by_sensor(alert_sensor.id)
        
        "Check the time difference to be creater than min time"
        if(most_recent == None or (datetime.datetime.utcnow() - most_recent.timestamp).seconds > MIN_TIME):

            "Create a new alert"
            alert = models.Alert(sensor=alert_sensor, timestamp=datetime.datetime.utcnow(), alert_request=cur_alert_request, priority = cur_alert_request.priority, alert_type=TYPE_SENSOR)

            db.session.add(alert)
            "Send the actual text message to warn the person and activate the app"
            message = client.sms.messages.create(to=cur_alert_request.phone,
                                         from_=TWILIO_NUMBER,
                                         body=PRIORITY_TO_STRING[cur_alert_request.priority]+
                                         '! '+cur_alert_request.name+' sent this warning from a sensor')
            print "Warning sent for "+cur_alert_request.name
            db.session.commit()
    return 'Success'


def checkfeeds():
    
    for ffeed in models.Feed.query.all():
        f = feedparser.parse(ffeed.url)
        print "Checking "+f.feed.title
        fpost = models.Post.query.filter_by(url=f.entries[0].link)
        if fpost != None:
            pass
        else:
            desc = f.entries[0].description
            words = desc.split()
            for kword in words:
                keywords = models.Keyword.query.filter_by(word=kword).all()
                for keyword in keywords:
                    cur_alert_request = models.AlertRequest.query.get(keyword.id_alert_request)

                    alert = models.Alert(keyword=keyword, timestamp=datetime.datetime.utcnow(), alert_request=cur_alert_request, priority = cur_alert_request.priority, alert_type=TYPE_FEED, post=fpost, feed=ffeed)

            db.session.add(alert)
            "Send the actual text message to warn the person and activate the app"
            message = client.sms.messages.create(to=cur_alert_request.phone,
                                         from_=TWILIO_NUMBER,
                                         body=PRIORITY_TO_STRING[cur_alert_request.priority]+
                                         '! '+cur_alert_request.name+' sent '+desc)
            db.session.commit()

