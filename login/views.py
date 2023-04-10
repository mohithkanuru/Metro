from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
em = ''
pwd = ''
def sample(request):
     global em,pwd
     if request.method =="POST":
        m = sql.connect(host = "localhost",user = "root",passwd = "Mohith@123",database = 'metro')
        cursor = m.cursor()
        d = request.POST
        for key,value in  d.items():
             if key=="uname":
                  em = value
             if key=="pwd":
                  pwd = value
             print(key)
        c = "select * from users where user_name = '{}' and password = '{}'".format(em,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t==():
            return render(request,'hai.html')
        else:
             return render(request,'regis.html')
      
     return render(request,'sample.html')
   