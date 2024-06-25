from app import app, db, bcrypt
from flask import render_template, redirect, url_for, jsonify, request
from app.forms import RegistrationForm, LoginForm, ScheduleForm, UpdateForm
from app.models import User, Schedule
from flask_login import login_user, current_user, logout_user, login_required
@app.route('/')
def home():
    
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return render_template('home.html')
    return render_template('login.html', title='Login', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return render_template('home.html')






@login_required
@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():


    schedule = Schedule.query.filter_by(user_id=current_user.id).all() 

    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
  
    return render_template('user_dashboard.html', schedules=schedule)

@app.route('/register', methods=['GET', 'POST'])
def register():


    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, sex=form.sex.data, adress=form.adress.data, phone_number=form.phone_number.data, house_number=form.house_number.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return render_template('home.html')
    return render_template('register.html', title='Register', form=form)
@login_required
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():

    form = ScheduleForm()

    if form.validate_on_submit():

        schedule = Schedule(date=form.date.data, type=form.type.data, user_id=current_user.id)
        db.session.add(schedule)
        db.session.commit()
        return render_template('home.html')
    return render_template('schedule.html', title='Schedule', form=form)



@app.route('/manage/<int:schedule_id>', methods=['GET', 'POST'])
def manage(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    return render_template('manage.html', schedules=schedule)



@app.route('/update/<int:schedule_id>', methods=['GET', 'POST'])
def update(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    form = UpdateForm()
    if form.validate_on_submit():
        schedule.date = form.date.data
        schedule.type = form.type.data
        db.session.commit()
        return redirect(url_for('user_dashboard'))
    
    elif request.method == 'GET':
        form.date.data = schedule.date
        form.type.data = schedule.type

    return render_template('update.html', schedules=schedule, form=form)


@app.route('/delete/<int:schedule_id>')
def delete(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    return redirect(url_for('user_dashboard'))

@app.route('/complete/<int:schedule_id>')
def complete(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    schedule.collected = True
    db.session.commit()
    return redirect(url_for('user_dashboard'))








# API endpoints
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_data = [{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'sex': user.sex,
        'address': user.adress,
        'phone_number': user.phone_number,
        'house_number': user.house_number
    } for user in users]
    return jsonify(user_data)


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'sex': user.sex,
        'address': user.adress,
        'phone_number': user.phone_number,
        'house_number': user.house_number
    }
    return jsonify(user_data)