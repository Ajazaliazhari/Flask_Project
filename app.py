from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.secret_key = 'iTsNormAlKeys'  # Change this to a strong, random key

# SQLAlchemy configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://czroot:sqladmin@localhost/ajaz_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your NASAData model
class NASADATA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    explanation = db.Column(db.Text)
    date = db.Column(db.String(20))

# NASA API endpoint
NASA_API_URL = 'https://api.nasa.gov/planetary/apod'

# NASA API key (Get your own key from: https://api.nasa.gov/)
NASA_API_KEY = 'POD0qNqjfDrc4R9UMfYomEYpOCFjfYawFPE0TQ5L'

# Routes

@app.route('/')
def index():
    if 'username' in session:
        # Fetch the latest NASA data from the database
        latest_data = NASADATA.query.order_by(NASADATA.id.desc()).first()
        return render_template('dashboard.html', username=session['username'], latest_data=latest_data)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Add your authentication logic here (e.g., check username and password)
        if username == 'your_username' and request.form['password'] == 'your_password':
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/fetch_nasa_data')
def fetch_nasa_data():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Fetch data from NASA API
    params = {'api_key': NASA_API_KEY}
    response = requests.get(NASA_API_URL, params=params)
    data = response.json()

    # Store data in MySQL database
    new_data = NASADATA(title=data['title'], explanation=data['explanation'], date=data['date'])
    db.session.add(new_data)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host = '172.16.1.241',port = '5001')
