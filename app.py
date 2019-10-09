from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import os



app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000)) 









