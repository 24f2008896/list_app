from flask import render_template, request
from model import *

def Dashboard(app):
    @app.route('/app/<ID>',methods=['GET','POST'])
    def dashboard(ID):
        user=Users.query.filter_by(id=ID).first()
        return render_template('dashboard.html',u=user)