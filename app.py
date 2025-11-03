import os
from flask import Flask,render_template
from model import *
from routes.home import create_list_type,Home
from routes.dashboard import Dashboard


current_dir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,"database.sqlite3")
db.init_app(app)
app.app_context().push()

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

Home(app)
Dashboard(app)

if __name__=="__main__":
    db.create_all()
    create_list_type()
    app.run(debug=True,port=3000,host='0.0.0.0')