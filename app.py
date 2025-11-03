from flask import Flask

app=Flask(__name__)

@app.route('/home',methods=['GET'])
def home():
    return "Welcome to Lists app 📋"

if __name__=="__main__":
    app.run(debug=True,port=3000)