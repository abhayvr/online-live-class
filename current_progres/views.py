from django.shortcuts import render
from current_progres.models import CurrentProgres
from student.models import Student
from parent.models import Parent
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
def current_progres(request):
    uid=request.session["u_id"]
    ob = Student.objects.all()
    context = {
        'p': ob
    }
    if request.method=='POST':
        obj=CurrentProgres()
        obj.progress_report=request.POST.get('Reply')
        obj.date=datetime.datetime.today()
        obj.parent_id=1
        obj.tutor_id=uid
        obj.student_id=request.POST.get('tid')
        obj.save()
        return HttpResponseRedirect('/temp/tutor')
    return render(request,'current_progres/Current Progress.html',context)

def view_progres(request):
    uid=request.session["u_id"]
    obj=CurrentProgres.objects.filter(student_id=uid)
    context={
        'x': obj
    }
    return render(request,'current_progres/view_current_progres.html',context)

def view_progres_parent(request):
    uid=request.session["u_id"]
    sob=Parent.objects.get(parent_id=uid)
    obj=CurrentProgres.objects.filter(student_id=sob.student_id)
    context={
        'x': obj
    }
    return render(request,'current_progres/view_progress_parent.html',context)
