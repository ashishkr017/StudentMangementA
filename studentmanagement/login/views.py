from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
em=""
pwd=""
rol=""

def log(request):
    global fn,ln,rol,em,pwd
    if(request.method=='POST'):
        m=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='bank')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            # if key=="role":
            #     rol=value
        c = "SELECT * FROM users WHERE email='{}' AND password='{}'".format(em, pwd)
        cursor.execute(c)
        user_data = cursor.fetchone()

        if not user_data:
            return render(request, 'error.html', {'message': 'Invalid credentials'})

        # Assuming role is in the third column of the users table, adjust accordingly
        rol = user_data[2]

        # Fetch role from the database
        cursor.execute("SELECT * FROM users WHERE role = '{}'".format(rol))
        existing_roll = cursor.fetchone()

        if not existing_roll:
            return render(request, 'error.html', {'message': 'Invalid role in the database'})

        if rol == "teacher":
            return render(request, 'teacher.html')
        elif rol == "student":
            return render(request, 'student.html')
        else:
            return render(request, 'home.html')

    return render(request, 'login.html')

# def show_data(request):
#     m=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='bank')
#     cursor=m.cursor()
#     c="SELECT * FROM users WHERE email='{}' AND password='{}'".format(em, pwd)
#     cursor.execute(c)
#     user_data = cursor.fetchall()
#     return render(request,'teacher.html',{'data':user_data})


def show_data(request):
    m = sql.connect(host="localhost", user="root", passwd="Ashiucristo@1", database='bank')
    cursor = m.cursor(dictionary=True)  # Use dictionary cursor to get results as dictionaries

    # Assuming 'teacher' is the role for teachers
    c = "SELECT * FROM users WHERE role='student'"
    cursor.execute(c)

    user_data = cursor.fetchall()
    return render(request, 'studentdetail.html', {'user_data': user_data})