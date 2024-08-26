from django.shortcuts import render
from feedback.models import Feedback
from tutor.models import Tutor
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
def add_feedback_student(request):
    uid=request.session["u_id"]
    ob = Tutor.objects.all()
    context = {
        'p': ob
    }
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('Reply')
        obj.date=datetime.datetime.today()
        obj.parent_id=1
        obj.student_id=uid
        obj.tutor_id=request.POST.get('tid')
        obj.type='student'
        obj.save()
        return HttpResponseRedirect('/temp/student')
    return render(request,'feedback/feedback.html',context)

def add_feedback_parent(request):
    uid=request.session["u_id"]
    ob = Tutor.objects.all()
    context = {
        'p': ob
    }
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('Reply')
        obj.date=datetime.datetime.today()
        obj.parent_id=uid
        obj.student_id=1
        obj.type='parent'
        obj.tutor_id=request.POST.get('tid')
        obj.save()
        return HttpResponseRedirect('/temp/parent')
    return render(request,'feedback/feedback parent.html',context)

def view_feedback_tutor(request):
    uid=request.session["u_id"]
    obj = Feedback.objects.filter(tutor_id=uid)
    context = {
        'x': obj
    }
    return render(request,'feedback/view feedback.html',context)

def view_feedback_admin(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request,'feedback/view feedback admin.html',context)