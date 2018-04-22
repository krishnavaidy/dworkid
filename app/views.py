from flask import render_template, request, redirect, url_for, session, jsonify
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine(app)
app.config['SECRET_KEY'] = 'blockhack'
app.secret_key = 'blockhack'
#app.config['TESTING'] = False
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = None

class User(UserMixin, db.Document):
    meta = {'collection': 'dworkid'}
    email = db.StringField(max_length=40)
    password = db.StringField()
    publicAddress = db.StringField()
    type_user = db.StringField(max_length=20)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signUp')
def sign_up():
    return render_template('signUp.html')

@app.route('/exp')
@login_required
def exp():
    return render_template('exp.html')

@app.route('/verify')
@login_required
def verify():
    return render_template('verify.html')

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/submitLogin', methods=['GET', 'POST'])
def submit_login():
    if request.method == 'POST':
        data = request.form.to_dict()
        print 'post'
        print data
	# if current_user.is_authenticated == True:
            # session['logged_in'] = True
	#     return redirect('/')
	check_user = User.objects(email=data['email']).first()
	if check_user:
	    if check_password_hash(check_user['password'], data['password']):
		login_user(check_user)
                session['logged_in'] = True
                session['email'] = data['email']
                session.modified = True
                print 'logged in'
		return redirect('/')

    session['logged_in'] = False
    session.modified = True
    return redirect('/')

@app.route('/submitSignUp', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form.to_dict()
        print 'post'
        print data
        existing_user = User.objects(email=data['email']).first()
        if existing_user is None:
            hashpass = generate_password_hash(data['password'], method='sha256')
            hey = User(data['email'],hashpass, data['publicAddress'], data['type_user']).save()
            login_user(hey)
            session['logged_in'] = True
            session.modified = True
            print 'logged in'
            return redirect('/')
        else:
            session['logged_in'] = True
            session.modified = True
            return redirect('/login')

    session['logged_in'] = False
    session.modified = True
    return redirect('/signUp')


@app.route('/userInfo', methods=['GET'])
def get_user_info():
    li = session.get('logged_in', False)
    email = session.get('email','')
    return jsonify({'logged_in': li, 'email': email})
