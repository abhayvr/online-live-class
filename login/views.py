from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
from tutor.models import Tutor
from parent.models import Parent
from student.models import Student

# Create your views here.
def post_login(request):
    if request.method =="POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("pwd")
        obj = Login.objects.filter(username=uname,password=passw)
        tp = ""
        for ob in obj :
            tp = ob.type
            uid = ob.u_id
            if tp =="admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')

            elif tp =="student":
                uob = Student.objects.get(student_id=uid)
                if uob.status == 'Accepted':
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/student/')
                else:
                    objlist = "Your registration is pending"
                    context = {
                        'msg': objlist
                    }
                    return render(request, 'login/Login.html', context)

            elif tp == "parent":
                uob = Parent.objects.get(parent_id=uid)
                if uob.status == 'Accepted':
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/parent/')
                else:
                    objlist = "Your registration is pending"
                    context = {
                        'msg': objlist
                    }
                    return render(request, 'login/Login.html', context)

            elif tp == "tutor":
                uob=Tutor.objects.get(tutor_id=uid)
                if uob.status=='Accepted':
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/tutor/')
                else:
                    objlist="Your registration is pending"
                    context = {
                        'msg': objlist
                    }
                    return render(request, 'login/Login.html', context)
        else:
            objlist = "username or password incorrect....... please try again.....!"
            context = {
                'msg':objlist
            }
            return render(request,'login/Login.html', context)

    return render(request,'login/Login.html')