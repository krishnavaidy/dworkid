from flask import render_template
#from flask_mongoengine import MongoEngine, Document
from app import app
#from model import User

# db = MongoEngine(app)
# #app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

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
def exp():
    return render_template('exp.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')

# @login_manager.user_loader
# def load_user(user_id):
    # return User.objects(pk=user_id).first()

# @app.route('/submitSignUp', methods=['GET', 'POST'])
# def register():
    # if request.method == 'POST':
	# print 'post'
	# # if form.validate():
	    # # existing_user = User.objects(email=form.email.data).first()
	    # # if existing_user is None:
		# # hashpass = generate_password_hash(form.password.data, method='sha256')
		# # hey = User(form.email.data,hashpass).save()
		# # login_user(hey)
		# # return redirect(url_for('/'))
#     return redirect(url_for('/signUp'))
