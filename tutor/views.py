from django.shortcuts import render
from tutor.models import Tutor
from login.models import Login
import smtplib
from django.http import HttpResponseRedirect
# Create your views here.
def manage_tutor(request):
    obj = Tutor.objects.all()
    context = {
        'x': obj
    }
    return render(request,'tutor/manage_tutor.html',context)

def accpt(request,idd):
    obj=Tutor.objects.get(tutor_id=idd)
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
    return manage_tutor(request)

def reject(request,idd):
    obj=Tutor.objects.get(tutor_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_tutor(request)


def reg_tutor(request):
    if request.method==('POST'):
        uname= request.POST.get('name')
        if Login.objects.filter(username=uname).exists():
            message="Username already exist"
        else:
            obj=Tutor()
            obj.name=request.POST.get('Uname')
            obj.address=request.POST.get('address')
            obj.dob=request.POST.get('DOB')
            obj.gender=request.POST.get('Gender')
            obj.email=request.POST.get('email')
            obj.phone_no=request.POST.get('phoneNo')
            obj.pincode=request.POST.get('pincode')
            obj.place=request.POST.get('place')
            obj.state=request.POST.get('State')
            obj.availability=request.POST.get('Availability')
            obj.education=request.POST.get('Education')
            obj.username = request.POST.get('name')
            obj.password = request.POST.get('pwd')
            obj.subject=request.POST.get('Subject')
            obj.fees=request.POST.get('fees')
            obj.fee_category = request.POST.get('Fee category')
            obj.save()
            ob = Login()
            ob.username = obj.username
            ob.password = obj.password
            ob.type = 'tutor'
            ob.u_id = obj.tutor_id
            ob.save()

            message = "Registered successfully " \
                      "you will receive a mail when admin confirms"
        context = {
            'msg': message

        }
        # return HttpResponseRedirect('/temp/home')
        return render(request,'tutor/tutor register.html',context)

    return render(request,'tutor/tutor register.html')


def update_tutor(request):
    ss=request.session["u_id"]
    obj = Tutor.objects.get(tutor_id=ss)
    context = {
        'x': obj
    }
    if request.method =='POST':
        obj = Tutor()
        obj.name = request.POST.get('Uname')
        obj.address = request.POST.get('address')
        obj.dob = request.POST.get('DOB')
        obj.gender = request.POST.get('Gender')
        obj.email = request.POST.get('email')
        obj.phone_no = request.POST.get('phoneNo')
        obj.pincode = request.POST.get('pincode')
        obj.place = request.POST.get('place')
        obj.state = request.POST.get('State')
        obj.availability = request.POST.get('Availability')
        obj.education = request.POST.get('Education')
    # obj.username = request.POST.get('name')
    # obj.password = request.POST.get('pwd')
        obj.fees = request.POST.get('fees')
        obj.fee_category=request.POST.get('Fee category')
        obj.save()

    return render(request,'tutor/update tutor.html',context)

def view_tutor(request):
    obj=Tutor.objects.filter(status='Accepted')
    context={
        'x':obj
    }
    return render(request,'tutor/view_tutors.html',context)

def view_tutor_admin(request):
    obj=Tutor.objects.all()
    context={
        'x':obj
    }
    return render(request,'tutor/view tutor admin.html',context)

def view_tutor_parent(request):
    obj=Tutor.objects.filter(status='Accepted')
    context={
        'x':obj
    }
    return render(request,'tutor/view tutor parent.html',context)