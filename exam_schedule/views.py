from django.shortcuts import render
from exam_schedule.models import ExamSchedule
from student.models import Student
from parent.models import Parent
from django.http import HttpResponseRedirect
import datetime
from Question.models import Questions
# Create your views here.
import random
def exam_schedule(request):
    uid=request.session["u_id"]
    ob = Student.objects.all()
    context = {
        'p': ob
    }
    if request.method=='POST':
        obj=ExamSchedule()
        obj.subject=request.POST.get('State')
        obj.date=request.POST.get('Date')
        obj.time=request.POST.get('Time')
        obj.tutor_id=uid
        obj.student_id=request.POST.get('tid')
        pob = Parent.objects.filter(student_id=obj.student_id)
        if len(pob)>0:
            obj.parent_id = pob[0].parent_id
        else:
            obj.parent_id=''
        qobj=Questions.objects.filter(subject=obj.subject)
        totq=len(qobj)
        qu=[]
        qno=1
        if totq>0:
            while True:
                r=random.randint(1,18)
                if r in qu:
                    pass
                else:
                    qu.append(r)
                    qno+=1
                    if qno==6:
                        break
            qs=""
            for i in qu:
                print(i,"hellooooo")
                qs=qs+","+str(qobj[i].question_id)
            print(qu)
            qs=qs[1:]

        obj.questions=qs
        obj.result="0"
        obj.status="pending"
        obj.save()
        return HttpResponseRedirect('/temp/tutor/')
    return render(request,'exam_schedule/exam schedule.html',context)

def view_exam(request):
    uid=request.session["u_id"]
    obj = ExamSchedule.objects.filter(student_id=uid)
    context = {
        'x': obj
    }
    return render(request,'exam_schedule/view exam schedule.html',context)

def view_exam_parent(request):
    uid=request.session["u_id"]
    sob=Parent.objects.get(parent_id=uid)
    obj = ExamSchedule.objects.filter(student_id=sob.student_id)
    context = {
        'x': obj
    }
    return render(request,'exam_schedule/view exam schedule parent.html',context)

def view_exam_admin(request):
    obj = ExamSchedule.objects.all()
    context = {
        'x': obj
    }
    return render(request,'exam_schedule/view exam schedule admin.html',context)
