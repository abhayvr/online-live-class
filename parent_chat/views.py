from django.shortcuts import render

from parent_chat.models import ParentChat
from parent.models import Parent
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
    return render(request,'parent_chat/viewcon.html',context)


def cochat(request,idd):
    ss=request.session["u_id"]
    obj = Tutor.objects.get(tutor_id=idd)
    ob =ParentChat.objects.filter(Q(parent_id=ss) & Q(tutor_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = ParentChat()
        obk.message = request.POST.get('mssg')
        obk.tutor_id=idd
        obk.parent_id=ss
        obk.rectype="tutor"
        obk.sendertype = "parent"
        obk.save()
    return render(request, 'parent_chat/chatuser1.html',context)



def std(request):
    ob=Parent.objects.all()
    context={
        'u':ob
    }
    return render(request,'parent_chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =Parent.objects.get(parent_id=idd)
    ob=ParentChat.objects.filter(Q(parent_id=idd) & Q(tutor_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=ParentChat()
        obk.message=request.POST.get('mssg')
        obk.parent_id=idd
        obk.tutor_id=ss
        obk.rectype="parent"
        obk.sendertype="tutor"
        obk.save()
    return render(request, 'parent_chat/chatuser2.html',context)
