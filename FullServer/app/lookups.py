from app import db, models
"""
The primary purpose of this file is to abstrace away as many of the database
calls as possible, so anytime a database lookup needs to be called, queries go 
in here, and the rest of the code simply sees a nice getter function.
I'm not sure if this is a good idea, but I'm tired and abstraction seems like
the best way to minimize mistakes.

Author: Sebastian
"""

'Returns a sensor object based on a mac address'
'Primary Use: web call made by Electric Imp'
def get_sensor_from_mac(mac):
    return models.Sensor.query.filter_by(macaddress=mac).first()

'Returns the AlertRequests for a specific sensor'
'Primary Use: Sensor sounds alarm, where does the alarm go?  To the AlertRequests!'
def get_requests_by_sid(sid):
    return models.AlertRequest.query.filter_by(id_sensor=sid).all()

'Returns the most recent alert sent for a specific sensor'
'Primary Use: Checking alarm recency to avoid duplicate alarms'
def get_most_recent_alert_by_sensor(sid):
    return models.Alert.query.filter_by(id_sensor=sid).order_by(models.Alert.timestamp.desc()).first()

    
