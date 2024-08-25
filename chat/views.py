from django.shortcuts import render
from student.models import Student
from chat.models import Chat
import datetime
from django.db.models import Q
from tutor.models import Tutor
# Create your views here.
from login.models import Login


def con(request):
    ob= Tutor.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session["u_id"]
    obj = Tutor.objects.get(tutor_id=idd)
    ob = Chat.objects.filter(Q(student_id=ss) & Q(tutor_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.tutor_id=idd
        obk.student_id=ss
        obk.rectype="tutor"
        obk.sendertype = "student"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ob=Student.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =Student.objects.get(student_id=idd)
    ob=Chat.objects.filter(Q(student_id=idd) & Q(tutor_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.student_id=idd
        obk.tutor_id=ss
        obk.rectype="student"
        obk.sendertype="tutor"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
