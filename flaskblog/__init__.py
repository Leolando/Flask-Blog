import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flaskdemo'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER']='smtp.163.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']= 'kevin_37s@163.com'
app.config['MAIL_PASSWORD'] = 'JFHNAVUWZOSHHXYW'
mail = Mail(app)

from flaskblog import routes