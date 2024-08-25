from django.shortcuts import render
from complaint.models import Complaint
from django.http import HttpResponseRedirect
from tutor.models import Tutor
import datetime
# Create your views here.
def admin_reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.replay=request.POST.get('Reply')
        obj.save()
        return post_replay(request)
    return render(request,'complaint/admin replay.html')

def complaint_student(request):
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('Reply1')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.student_id=uid
        obj.tutor_id=1
        obj.replay='pending'
        obj.type='student'
        obj.save()
        return HttpResponseRedirect('/temp/student')
        # return post_replay(request)
    return render(request,'complaint/complaint student.html')


def complaint(request):
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('Reply')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.tutor_id=uid
        obj.student_id=1
        obj.type='tutor'
        obj.replay='pending'
        obj.save()
        return HttpResponseRedirect('/temp/tutor')
    return render(request,'complaint/complaint.html')


def post_replay(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/view complaint & post reply.html', context)


def view_student(request):
    uid=request.session["u_id"]
    obj=Complaint.objects.filter(type='student',student_id=uid)
    context = {
        'x': obj
    }
    return render(request,'complaint/view complaint student.html',context)


def view_tutor(request):
    uid=request.session["u_id"]
    obj=Complaint.objects.filter(type='tutor',tutor_id=uid)
    context = {
        'x': obj
    }
    return render(request,'complaint/view complaint tutor.html',context)


def view_admin(request):
    obj=Complaint.objects.filter(type='tutor')
    context = {
        'x': obj
    }
    return render(request,'complaint/view complaint admin.html',context)
