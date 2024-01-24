from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
import requests

app = Flask(__name__)
app.secret_key = 'itsAjazAliincredibale@'  # Change this to a strong, random key

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sqladmin'
app.config['MYSQL_DATABASE_DB'] = 'ajaz_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# NASA API endpoint
NASA_API_URL = 'https://api.nasa.gov/planetary/apod'

# NASA API key (Get your own key from: https://api.nasa.gov/)
NASA_API_KEY = 'POD0qNqjfDrc4R9UMfYomEYpOCFjfYawFPE0TQ5L'

# Routes

@app.route('/profile')
def sample():
    return render_template('profile.html')


@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Add your authentication logic here (e.g., check username and password)
        if username == 'ajazAli' and request.form['password'] == 'ajaz@123':
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
    print("========data=====",data)

    # Store data in MySQL database
    cursor = mysql.get_db().cursor()
    cursor.execute('INSERT INTO NASADATA (title, explanation, date) VALUES (%s, %s, %s)',
                   (data['title'], data['explanation'], data['date']))
    mysql.get_db().commit()

    #return redirect(url_for('index'))
    return render_template('show_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True,host='172.16.1.241',port='5001')

