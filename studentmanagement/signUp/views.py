from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
fn=""
ln=""
rol=""
em=""
pwd=""
def signup(request):
    global fn,ln,rol,em,pwd
    if(request.method=='POST'):
        m=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='bank')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="fname":
                fn=value
            if key=="lname":
                ln=value
            if key=="role":
                rol=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        try:
            # Check if user already exists
            cursor.execute("SELECT * FROM users WHERE email = '{}' ".format(em))
            existing_user = cursor.fetchall()
            
            if existing_user:
                return render(request, "userExist.html")
            else:
                # If user does not exist, insert into the database
                c = "INSERT INTO users VALUES('{}', '{}', '{}', '{}', '{}')".format(fn, ln, rol, em, pwd)
                cursor.execute(c)
                m.commit()
                if rol == "teacher":
                    return render(request, 'teacher.html')
                elif rol == "student":
                    return render(request, 'student.html')
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'signUp.html')