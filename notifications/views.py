from django.shortcuts import render
from notifications.models import Notifications
from student.models import Student
from django.http import HttpResponseRedirect
import smtplib
from parent.models import Parent
import datetime
# Create your views here.
def add_notifications(request):
    uid=request.session["u_id"]
    ob = Student.objects.all()
    context = {
        'p': ob
    }
    if request.method=='POST':
        obj=Notifications()
        obj.notification=request.POST.get('Reply')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.student_id=request.POST.get('tid')
        pob=Parent.objects.filter(student_id=obj.student_id)
        if len(pob)>0:
            obj.parent_id=pob[0].parent_id
        else:
            obj.parent_id=''
        obj.tutor_id=uid
        obj.save()
        try:
            email = "projectmailbg@gmail.com"
            em=obj.student.email
            sub = "Notification"
            msg = obj.notification + '\nDate: ' + str(obj.date)+""
            text = f'subject : {sub} \n\n{msg}'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, 'iqjjrhsyerovorav')
            server.sendmail(email, str(em), text)
        except:
            pass
        return HttpResponseRedirect('/temp/tutor')
    return render(request,'notifications/notification.html',context)


def view_notifications(request):
    uid=request.session["u_id"]
    obj=Notifications.objects.filter(student_id=uid)
    context={
        'x':obj
    }
    return render(request,'notifications/view_notifications.html',context)

from parent.models import Parent
def view_notifications_parent(request):
    uid=request.session["u_id"]
    sob=Parent.objects.get(parent_id=uid)
    obj=Notifications.objects.filter(student_id=sob.student_id)
    context={
        'x':obj
    }
    return render(request,'notifications/view notification parent.html',context)