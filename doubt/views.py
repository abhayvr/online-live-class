from django.shortcuts import render
from doubt.models import Doubt
from tutor.models import Tutor
import datetime
# Create your views here.
def replay(request,idd):
    if request.method=='POST':
        obj=Doubt.objects.get(doubt_id=idd)
        obj.replay=request.POST.get('Reply')
        obj.save()
        return view_doubt(request)
    return render(request, 'doubt/reply.html')

def post_doubt(request):
    uid=request.session["u_id"]
    ob = Tutor.objects.all()
    context = {
        'p': ob
    }
    if request.method == 'POST':
        obj = Doubt()
        obj.description = request.POST.get('Reply')
        obj.date = datetime.datetime.today()
        obj.tutor_id =request.POST.get('tid')
        obj.student_id = uid
        obj.replay = 'pending'
        obj.save()
    return render(request,'doubt/post doubt.html',context)

def view_doubt(request):
    uid=request.session["u_id"]
    obj = Doubt.objects.filter(tutor_id=uid)
    context = {
        'x': obj
    }
    return render(request,'doubt/View_doubt.html',context)

def view_doubt_student(request):
    uid=request.session["u_id"]
    obj = Doubt.objects.filter(student_id=uid)
    context = {
        'x': obj
    }
    return render(request,'doubt/view doubt student.html',context)

