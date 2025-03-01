from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered. Please log in.')
            return redirect(url_for('login'))

        # Hash the password with Werkzeug
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Create a new user with the hashed password
        new_user = User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Log the user in automatically
        session['user_id'] = new_user.id
        return redirect(url_for('secrets'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Verify user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email not found. Please register first.')
            return redirect(url_for('register'))

        # Verify password
        if not check_password_hash(user.password, password):
            flash('Incorrect password. Please try again.')
            return redirect(url_for('login'))

        # Log the user in
        login_user(user)
        return redirect(url_for('secrets'))

    return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html', name=current_user.name)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)



# I can enter to the secrets page and without signing in and I also cant log out