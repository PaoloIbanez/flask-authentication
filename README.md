
# 🛡️ Flask Authentication System

Welcome to the **Flask Authentication System**! This project is about **user authentication**—allowing users to **register, log in, and access protected content securely** using Flask. It's a great way to learn about authentication, hashing passwords, and securing routes in Flask.

## 🚀 Features

✅ **User Registration** – Sign up with an email and password  
✅ **Secure Login** – Log in using hashed and salted passwords  
✅ **Authentication** – Restrict access to certain pages  
✅ **Flash Messages** – Get feedback when login fails  
✅ **Navigation Updates** – Show different buttons for logged-in users  
✅ **Download Feature** – Securely download a file after authentication  

## 🛠️ Technologies Used

🔹 Flask (Python Web Framework)  
🔹 Flask-Login (User authentication)  
🔹 Flask-WTF (Forms & validation)  
🔹 Flask-Bootstrap (Pre-styled UI)  
🔹 Werkzeug (Password hashing & security)  
🔹 SQLite (Lightweight database)  

## 📂 Project Structure

```
/static        # CSS files and static content
/templates     # HTML templates
  ├── base.html       # Main template layout
  ├── index.html      # Home page
  ├── login.html      # Login page
  ├── register.html   # Registration page
  ├── secrets.html    # Protected page (for logged-in users)
/static/files   # Secret files for download
main.py         # Flask application
users.db        # SQLite database for user data
requirements.txt # Dependencies
```

## 🏃‍♂️ Getting Started

### 1️⃣ Install Dependencies
First, make sure you have Python installed. Then, set up a **virtual environment** and install dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2️⃣ Run the Flask App
Start the Flask development server:

```sh
python main.py
```

Now, open your browser and go to **http://127.0.0.1:5000** 🎉

### 3️⃣ Try it Out!
- **Register a new user**  
- **Log in with the same credentials**  
- **Access the secret page!** 🔒  
- **Download the cheat sheet (only if logged in!)**  

## 🔑 How It Works

1️⃣ When a user **registers**, their password is **hashed and salted** using `pbkdf2:sha256` before being stored in the database.  
2️⃣ When logging in, the app **verifies the hash** using `check_password_hash()` to confirm credentials.  
3️⃣ Once logged in, Flask-Login manages **sessions**, keeping users authenticated across different pages.  
4️⃣ Users can **only access protected routes** (`/secrets`, `/download`) if logged in.  
5️⃣ The **login & register buttons disappear** when a user is logged in for a smoother experience.  

## Possible Improvements
- Add **email verification** for extra security  
- Implement **OAuth login** (Google, Facebook)  
- Expand the app into a **full-featured dashboard**  

## 🤝 Contributing
Got ideas? Found a bug? Feel free to **fork this repo**, submit a PR, or open an issue. Let's build something awesome together! 🚀

