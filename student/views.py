from django.shortcuts import render
from student.models import Student
from login.models import Login
from Question.models import Questions
from django.http import HttpResponseRedirect
import smtplib
# Create your views here.
def manage_students(request):
    obj = Student.objects.all()
    context = {
        'x': obj
    }
    return render(request,'student/manage_students.html',context)

def accpt(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='Accepted'
    obj.save()
    try:
        email = "projectmailbg@gmail.com"
        em = obj.email
        sub = "Registration Approval"
        msg = "Hi "+obj.name+", \n Your Registration is approved\nThank You"
        text = f'subject : {sub} \n\n{msg}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, 'iqjjrhsyerovorav')
        server.sendmail(email, str(em), text)
    except:
        pass
    return manage_students(request)

def reject(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_students(request)

def reg_students(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        if Login.objects.filter(username=uname).exists():
            message="username already exist"
        else:
            obj=Student()
            obj.name=request.POST.get('Uname')
            obj.addres=request.POST.get('Address')
            obj.dob=request.POST.get('DOB')
            obj.gender=request.POST.get('Gender')
            obj.email=request.POST.get('email')
            obj.phone_no=request.POST.get('phoneNo')
            obj.pincode=request.POST.get('pincode')
            obj.place=request.POST.get('place')
            obj.state=request.POST.get('State')
            obj.education=request.POST.get('Education')
            obj.language=request.POST.get('Language')
            obj.guardian_info=request.POST.get('guardianinfo')
            obj.username=uname
            obj.password=request.POST.get('pwd')
            obj.save()

            ob=Login()
            ob.username=obj.username
            ob.password=obj.password
            ob.type='student'
            ob.u_id=obj.student_id
            ob.save()

            message = "Registered successfully " \
                      "you will receive a mail when admin confirms"
        context = {
                'msg': message
        }

        return render(request, 'student/student register.html',context)
    return render(request,'student/student register.html')


def student_profile(request):
    uid=request.session["u_id"]
    obj=Student.objects.get(student_id=uid)
    context={
        'x':obj
    }
    if request.method=='POST':
        obj.name=request.POST.get('Uname')
        obj.addres=request.POST.get('Address')
        obj.dob=request.POST.get('DOB')
        obj.gender=request.POST.get('Gender')
        obj.email=request.POST.get('email')
        obj.phone_no=request.POST.get('phoneNo')
        obj.pincode=request.POST.get('pincode')
        obj.place=request.POST.get('place')
        obj.state=request.POST.get('State')
        obj.education=request.POST.get('Education')
        obj.language=request.POST.get('Language')
        obj.guardian_info=request.POST.get('guardianinfo')
        obj.save()
        return HttpResponseRedirect('/temp/student')
    return render(request,'student/student profile.html',context)



def view_student(request):
    obj=Student.objects.all()
    context={
        'x':obj
    }
    return render(request,'student/view_students.html',context)


def view_student_admin(request):
    obj=Student.objects.all()
    context={
        'x':obj
    }
    return render(request,'student/view students admin.html',context)
from exam_schedule.models import ExamSchedule
def view_exam(request,idd):
    objex=ExamSchedule.objects.get(exam_schedule_id=idd)
    qst=objex.questions.split(',')

    obj=Questions.objects.filter(question_id__in=qst)
    context = {
        'x': obj
    }

    if request.method=="POST":
        mark=0
        for q in qst:
            sel=request.POST.get("opt"+str(q))
            cur=request.POST.get("ans"+str(q))
            if sel==cur:
                mark+=1
        objex.status="attended"
        objex.result=str(mark)
        objex.save()
        return HttpResponseRedirect('/temp/student/')

    return render(request,'student/view exam student.html',context)
