from app import db, models
from time import mktime
from datetime import datetime
"""
Much like lookups.py, this serves as a centralized module for all of the different kinds of inserting we might do.  I'm not sure how useful this is, but I want to write it down because it's easier to create it now than wait for the UI to finish and implement it in each specific spot there.  This is probably not best practice, but increases speed for the sake of finishing on time.

NOTE: remember to db.session.commit() after all database input is finished.

Author: Sebastian
"""

def insert_user(n_name, n_email):
    if not models.User.query.filter_by(name=n_name).first() and not models.User.query.filter_by(email=n_email).first():
        u = models.User(name=n_name, email=n_emai)
        db.session.add(u)

        return u
    else:
        return None

'Make sure n_user is a user object and n_sensor is a sensor obect (or blank/None)'
def insert_alert_request(n_name, n_user, n_phone, n_priority, n_alert_type,n_feed=None, n_sensor=None):
    req = models.AlertRequest(name=n_name, user=n_user, phone=n_phone, sensor=n_sensor, feed=n_feed, priority=n_priority, alert_type=n_alert_type)
    db.session.add(req)
    return req

'''The use case for this is special: This is used to scan RSS feeds, so we only need it once
if it already exists, we must return it.'''
def find_or_insert_feed(n_url):
    current = models.Feed.query.filter_by(url=n_url)
    if current == None:
        d = feedparser.parse(url)
        n_name = d.feed.title
        n_feed = models.Feed(name=n_name, url=n_url)
        insert_post(n_feed, d.entries[0].url)
        db.session.add(n_feed)
        return n_feed
    else:
        return current

'''Make sure n_feed is a feed object'''
def insert_post(n_feed, n_url):
    f = feedparser.parse(n_url)
    dt = datetime.fromtimestamp(mktime(f.entries[0].published_parsed))
    post = models.Post(name=f.entries[0].title, feed=n_feed, url=n_url, timestamp=dt) 
    db.session.add(post)
    return post

def insert_keyword(n_word, n_alert_request):
    n_feed = models.Feed.query.filter_by(id=n_alert_request.id_feed)
    keyword = models.Keyword(feed=n_feed, alert_request=n_alert_request, word=n_word)
    db.session.add(keyword)
    return keyword

def insert_antiword(n_word, n_alert_request):
    n_feed = models.Feed.query.filter_by(id=n_alert_request.id_feed)
    antiword = models.antiword(feed=n_feed, alert_request=n_alert_request, word=n_word)
    db.session.add(antiword)
    return antiword

def insert_sensor(n_name, n_url, n_macaddress):
    n_sensor= models.Sensor(name=n_name, url = n_url, macaddress = n_macaddress)
    db.session.add(n_sensor)
    return n_sensor
