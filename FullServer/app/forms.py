from flask.ext.wtf import Form, TextField, BooleanField, validators, RadioField
from flask.ext.wtf import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    

class SensorForm(Form):
    sensor_name = TextField('Sensor Name', [validators.Length(min=4, max=60)])
    macaddr = TextField('Mac Address', [validators.Length(min=12, max=12)])
    url = TextField('URL', [validators.Length(min=0, max=120)])
    priority = TextField('Priority (1-3)', [validators.length(min=1, max=1)])
    phone = TextField('Phone Number')

class RSSForm(Form):
    alert_name = TextField('Sensor Name', [validators.Length(min=4, max=60)])
    url = TextField('URL', [validators.Length(min=0, max=120)])
    priority = TextField('Priority (1-3)', [validators.length(min=1, max=1)])
    phone = TextField('Phone Number')
    keywords = TextField('Space seperated key words here!')
