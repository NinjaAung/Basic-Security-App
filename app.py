from flask import render_template, Flask, url_for, redirect, request, session, abort, jsonify, flash, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from models import User, Corn
import requests
import os






app = Flask(__name__)

os.environ['MONGO_URI'] = 'mongodb://localhost:27017/corn-list'
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/corn-list')
app.config['MONGO_URI'] = host

client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
user = db.user
cornlist = db.cornlist
visitor = db.visitor

login_manager = LoginManager()
login_manager.init_app(app)



@app.route('/')
def index():
    if 'user' in session:
        if 'ammount' in session:
            # transfer the user session over to the home page
            user = session['user']
            cart = session['ammount']
            username = user['username']
            
            return render_template('user_index.html', user=user, cart=cart, username=username)
        else:
            user = session['user']
            cart = user['cart_ammount']
            username = user['username']
            

            return render_template('user_index.html', user=user, cart=cart, username=username)
    else:
        return render_template('index.html')


@app.route('/RegisterCorn')
def register():
    pass

@app.route('/loginCorn')
def login():
    return render_template('Sign In')





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000)) 









