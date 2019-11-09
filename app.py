from flask import render_template, Flask, url_for, redirect, request, abort, jsonify
from datetime import datetime
import os






app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000)) 
