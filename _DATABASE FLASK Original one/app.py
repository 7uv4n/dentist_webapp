from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__) #referencing

#configure db
app.config['MYSQL_HOST']='localhost'            #db['mysql_host']
app.config['MYSQL_USER']='root'                 #db['mysql_user']
app.config['MYSQL_PASSWORD']='Yuvan 27112000'   #db['mysql_password']
app.config['MYSQL_DB']='dentalproj'             #db['mysql_db']

mysql=MySQL(app)#instantiation


@app.route('/',methods=('GET','POST'))
def first():
    return render_template('1. first page.html')
    if request.method=='POST':
        #fetch form data
        usersDetails=request.form
        pname=usersDetails['name']
        birthdate=usersDetails['date']
        age=usersDetails['age']
        gender=usersDetails['Gender']
        occupation=usersDetails['occupation']
        mobile=usersDetails['mobile']
        raddress=usersDetails['raddress']
        e_name=usersDetails['e_name']
        e_mobile=usersDetails['e_mobile']
        relation=usersDetails['relation']
        e_date=usersDetails['e_date']
   
@app.route('/secondpage',methods=('GET','POST'))
def second():
    return render_template('2. second page.html')
    if request.method=='POST':
        #fetch form data
        usersDetails=request.form
        care=usersDetails['med1_']
        drugs=usersDetails['med2_']
        surgery=usersDetails['med3_']
        chest=usersDetails['med4_']


@app.route('/thirdpage',methods=('GET','POST'))
def third():
    return pname
    return care
    """return render_template('3. third page.html')
    if request.method=='POST':
        #fetch form data
        usersDetails=request.form
        pname=usersDetails['name']
        birthdate=usersDetails['date']
        age=usersDetails['age']
        gender=usersDetails['Gender']
        occupation=usersDetails['occupation']
        mobile=usersDetails['mobile']
        raddress=usersDetails['raddress']
        e_name=usersDetails['e_name']
        e_mobile=usersDetails['e_mobile']
        relation=usersDetails['relation']
        e_date=usersDetails['e_date']   """

@app.route('/fourthpage',methods=('GET','POST'))
def fourth():
    return render_template('4. fourth page.html')
    if request.method=='POST':
        #fetch form data
        usersDetails=request.form
        pname=usersDetails['name']
        birthdate=usersDetails['date']
        age=usersDetails['age']
        gender=usersDetails['Gender']
        occupation=usersDetails['occupation']
        mobile=usersDetails['mobile']
        raddress=usersDetails['raddress']
        e_name=usersDetails['e_name']
        e_mobile=usersDetails['e_mobile']
        relation=usersDetails['relation']
        e_date=usersDetails['e_date']
        

@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM users")
    if result>0:
        userDetails=cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


if __name__=="__main__":
    app.run(debug=True)#if any errors they'll pop on the web page
     
     
"""
index.html
{% extends 'base.html' %}

{% block head %}
{% endblock %}

{% block body %}
<h1>Template</h1>
{% endblock %}
"""