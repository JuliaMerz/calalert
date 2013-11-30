from app import db, models
"""
Much like lookups.py, this serves as a centralized module for all of the different kinds of inserting we might do.  I'm not sure how useful this is, but I want to write it down because it's easier to create it now than wait for the UI to finish and implement it in each specific spot there.  This is probably not best practice, but increases speed for the sake of finishing on time.

NOTE: remember to db.session.commit() after all database input is finished.

Author: Sebastian
"""

def insert_user(uname, uemail):
    if not models.User.query.filter_by(name=uname).first() and not models.User.query.filter_by(email=uemail).first():
        u = models.User(name=uname, email=uemai)
        db.session.add(u)

        return u
    else:
        return None

'Make sure nuser is a user object and nsensor is a sensor obect (or blank/None)'
def insert_alert_request(nname, nuser, nphone, npriority, nalert_type, nsensor=None):
    req = models.AlertRequest(name=nname, user=nuser, phone=nphone, sensor=nsensor, priority=npriority, alert_type=nalert_type)
    db.session.add(req)
    return req
