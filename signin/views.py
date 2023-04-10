from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
fn=''
ln=''
s=''
em = ''
pwd = ''
def sample(request):
     global fn,ln,s,em,pwd
     if request.method =="POST":
        m = sql.connect(host = "localhost",user = "root",passwd = "Mohith@123",database = 'metro')
        cursor = m.cursor()
        d = request.POST
        for key,value in  d.items():
             if key=="first_name":
                  fn = value
             if key=="last_name":
                  ln = value
             if key=="sex":
                  s = value
             if key=="email":
                  em = value
             if key=="password":
                  pwd = value
             print(key)
        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn,s,"Not travelling",0,pwd)
        cursor.execute(c)
        m.commit()

      
     return render(request,'signup_page.html')
   