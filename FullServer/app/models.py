from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    alert_requests = db.relationship('AlertRequest', backref = 'user', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    url = db.Column(db.String(120))
    alert_requests = db.relationship('AlertRequest', backref= 'sensor', lazy = 'dynamic')
    alerts = db.relationship('Alert', backref = 'sensor', lazy = 'dynamic')
    macaddress = db.Column(db.String(12))

    def __repr__(self):
        return '<Sensor %r>' % (self.name)

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    url = db.Column(db.String(120))
    alerts = db.relationship('Alert', backref = 'feed', lazy = 'dynamic')
    keywords = db.relationship('Keyword', backref = 'feed', lazy = 'dynamic')
    posts = db.relationship('Post', backref = 'feed', lazy = 'dynamic')
    antiwords = db.relationship('Antiword', backref = 'feed', lazy = 'dynamic')
    feed = db.relationship('AlertRequest', backref = 'feed', lazy = 'dynamic')

    def __repr__(self):
        return '<Feed %r>' % (self.name)

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(40))
    id_alert_request = db.Column(db.Integer, db.ForeignKey('alert_request.id'))
    id_feed = db.Column(db.Integer, db.ForeignKey('feed.id'))
    alerts = db.relationship('Alert', backref = 'keyword', lazy = 'dynamic')

    def __repr__(self):
        return '<Antiword %r>' % (self.word)

class Antiword(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(40))
    id_alert_request = db.Column(db.Integer, db.ForeignKey('alert_request.id'))
    id_feed = db.Column(db.Integer, db.ForeignKey('feed.id'))

    def __repr__(self):
        return '<Antiword %r>' % (self.word)

class AlertRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    phone = db.Column(db.String(20))
    id_sensor = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    priority = db.Column(db.SmallInteger)
    alert_type = db.Column(db.SmallInteger)
    id_feed = db.Column(db.Integer, db.ForeignKey('feed.id'))

    keywords  = db.relationship('Keyword', backref = 'alert_request', lazy = 'dynamic')
    antiwords  = db.relationship('Antiword', backref = 'alert_request', lazy = 'dynamic')
    alerts  = db.relationship('Alert', backref = 'alert_request', lazy = 'dynamic')

    def __repr__(self):
        return '<AlertRequest %r>' % (self.name)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_alert_request = db.Column(db.Integer, db.ForeignKey('alert_request.id'))
    alert_type = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    id_feed = db.Column(db.Integer, db.ForeignKey('feed.id'))
    id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
    id_sensor = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    id_keyword = db.Column(db.Integer, db.ForeignKey('keyword.id'))
    priority = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<Alert %r>' % (self.id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    id_feed = db.Column(db.Integer, db.ForeignKey('feed.id'))
    url = db.Column(db.String(120))
    name = db.Column(db.String(200))
