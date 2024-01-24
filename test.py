from flask import Flask, render_template
from flask import Flask, request,render_template
import pymysql

app = Flask(__name__)


@app.route("/")
def main():

    return "Here I am for Testing"
	
if(__name__ == "__main__"):
    app.run(debug=True, host='172.16.1.241', port=5002)
