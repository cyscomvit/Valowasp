
from logging import debug
from flask import Flask,render_template,request
import pymongo
from werkzeug.utils import redirect
from flask_pymongo import PyMongo
import flask
from flask.json import jsonify
from dotenv import load_dotenv
load_dotenv()
import os
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired
from wtforms.validators import DataRequired, Email
import re
MONGO_URI = os.getenv("MONGO_URI")





app=Flask(__name__)






# app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
app.config["MONGO_URI"]=MONGO_URI
client = pymongo.MongoClient(MONGO_URI)
db = client.valo

@app.route("/add_one")
def add_one():
    db.users.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")


@app.route("/data",methods=["POST","GET"])
def data():
    message=''
    phone_no=''
    discord_id=''
    valorant_id=''
    success=''
    data={}
    if request.method=="POST":
        data['Team_name']=request.form['TeamName']
        data['Email_id_team_lead']=request.form['LeadEmail']
        data['Contact_no_team_lead']=request.form['LeadNumber']
        data['No_members']=request.form['No_mem']

        data['Discord_id1']=request.form['Did1']
        data['Valo_id1']=request.form['Vid1']
        data['Player_level']=request.form['playerLevel1']
        
        data['Discord_id2']=request.form['Did2']
        data['Valo_id2']=request.form['Vid2']
        data['Player_leve2']=request.form['playerLevel2']

        data['Discord_id3']=request.form['Did3']
        data['Valo_id3']=request.form['Vid3']
        data['Player_level3']=request.form['playerLevel3']

        data['Discord_id4']=request.form['Did4']
        data['Valo_id4']=request.form['Vid4']
        data['Player_level4']=request.form['playerLevel4']

        data['Discord_id5']=request.form['Did5']
        data['Valo_id5']=request.form['Vid5']
        data['Player_level5']=request.form['playerLevel5']

        data['Transcation_id']=request.form['Tid']
        # email_found = db.valo_owasp.find_one({"email": email})
        
        email=request.form.get("Email_id_team_lead")

        # if email_found:
        #     message="This email already exists"
        #     return jsonify({"error":"Email address already in use"}),400
        #     return render_template('index.html', message=message)
        if db.valo_owasp.find_one({"Email_id_team_lead":data['Email_id_team_lead']}):
             message="This email already exists"
             return render_template('data.html',message=message)
            #  return jsonify({"error":"Email address already in use"}),400

        if len(data['Contact_no_team_lead'])!=10:
            print(len(data['Contact_no_team_lead']))
            phone_no="Please enter a valid phone number"
            return render_template('data.html',phone_no=phone_no)
        
        Pattern = re.compile("^.{3,32}#[0-9]{4}$")

        for i in range(1,int(data['No_members'])+1):
            dis_id='Discord_id'+str(i)
            if (Pattern.match(dis_id)):
                print("Match found")

            else:
                print('No Match found')
                discord_id='Enter Valid Discord ID for Player '+str(i)
                return render_template('data.html',discord_id = discord_id)

        for i in range(1,int(data['No_members'])+1):
            valo_id='Valo_id'+str(i)
            if(Pattern.match(data[valo_id])):
                print("matched valo id")
            else:
                valorant_id="Please enter a valid valorant id for player"+str(i)
                return render_template("data.html",valorant_id=valorant_id)
           




        

            

        # if(data['Discord_id1'])!="~ /^\D+#\d{4}$/":
        #     discord_id="Please enter a valid discord_id"
        #     return render_template('index.html',discord_id=discord_id)



      
        # if db.valo_owasp.find_one({"Email_id_team_lead":data['Email_id_team_lead']}):
        #     return jsonify({"error":"Email address already in use"}),400
        db.valo_owasp.insert_one(data)
        success='registration succesfull'
        return render_template('index.html',success=success)

        
        
        
       
    return render_template('data.html')

        
    
        


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/data')
def register():
    return render_template('data.html')

@app.route('/rules')
def rules():
    return render_template('Rules.html')

@app.route('/FAQ')
def faqs():
    return render_template('FAQ.html')

@app.route('/Timeline')
def timeline():
    return render_template('Timeline.html')

@app.route('/Instructions')
def instructions():
    return render_template('Instructions.html')










if __name__== '__main__':
    app.run(debug=True)