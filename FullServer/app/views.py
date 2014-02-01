from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
import forms
import models
import inserts
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('index.html',
        title = 'Home',
        user = user)

@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(name = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/addsensor', methods=['GET', 'POST'])
def addsensor():
    form = forms.SensorForm(request.form)
    if request.method == 'POST' and form.validate():
        sensor = inserts.insert_sensor(form.sensor_name.data, form.url.data, form.macaddr.data)
        inserts.insert_alert_request(form.sensor_name.data, g.user, form.phone.data, form.priority.data, 1, None, sensor)
        db.session.commit()
        flash('Congratulations for configuring your sensor!')
        return redirect(url_for('index'))
    return render_template('base.html', form=form)

@app.route('/addrss', methods=['GET', 'POST'])
def addrss():
    form = forms.RSSForm(request.form)
    if request.method == 'POST' and form.validate():
        feed = inserts.find_or_insert_feed(form.url)
        alert_request = inserts.insert_alert_request(form.sensor_name.data, g.user, form.phone.data, 3, 2, feed)
        keywords = form.keywords.data.split()
        for keyword in keywords:
            insert_keyword(keyword, alert_request)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('base.html', form=form)
        
    
