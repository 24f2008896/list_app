from model import *
from flask import render_template,request,redirect

def create_list_type():
    dicti={
    "cook_book page": "Where all the secret family recipes go to become famous.",
    "shopping list": "The official record of things I *absolutely* need, plus that one impulse snack.",
    "bucket list": "A record of ambitions ranging from 'learn to juggle' to 'visit the moon'.",
    "study list": "The list of topics standing between me and academic glory (or at least a passing grade).",
    "to-do-list": "The optimistic daily plan that often ends up rolling over to tomorrow.",
    "travel-list": "A collection of destinations where my out-of-office reply works its magic.",
    "grocery list": "Milk, bread, eggs, cheese, and questionable life choices down the snack aisle.",
    "custom list": "The wild card—it could be a list of favorite socks or theoretical physics theories.",
    "quotes list": "A database of witty remarks and profound thoughts I plan to steal and use as my own."
    }
    exists=Lists.query.all()
    if exists:
        print('Something already exists in lists table')
        return 
    for each in dicti.keys():
        obj=Lists(list_name=each,list_description=dicti[each])
        db.session.add(obj)
    db.session.commit()

def Home(app):

    @app.route('/register',methods=['POST'])
    def register():
        Name=request.form['name']
        Email=request.form['email']
        Password=request.form['password']
        user=Users.query.filter_by(email=Email).first()
        if user:
            return render_template('random.html',mood='info',message='User already exists -->> Login ')
        else:
            User=Users(name=Name,email=Email,password=Password)
            db.session.add(User)
            db.session.commit()
            return render_template('random.html',mood='success',message='User successfully registered')

    @app.route('/login',methods=['POST'])
    def login():
        Email=request.form['email']
        Password=request.form['password']
        user=Users.query.filter_by(email=Email).first()
        if user:
            if user.password==Password:
                return redirect(f'/app/{user.id}')
            return render_template('random.html', mood='error', message='Wrong password,Try again')
        return render_template('random.html',mood='error',message='No user with this email exists')
    
    @app.route('/logout',methods=['GET'])
    def logout():
        return redirect('/home')