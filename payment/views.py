from django.shortcuts import render
from payment.models import Payment
from django.http import HttpResponseRedirect
# Create your views here.
def manage_payment(request):
    obj=Payment.objects.all()
    context={
        'x':obj
    }
    return render(request,'payment/manage_payment.html',context)

def view_payment(request):
    obj=Payment.objects.all()
    context={
        'x':obj
    }
    return render(request,'payment/view_payment.html',context)

from tutor.models import Tutor
def payment(request,idd):
    uid = request.session["u_id"]
    ob=Tutor.objects.get(tutor_id=idd)
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Payment()
        obj.card_holder_name=request.POST.get('Name')
        obj.card_number=request.POST.get('Cardnumber')
        obj.cvv=request.POST.get('Card')
        obj.amount=request.POST.get('fee')
        obj.tutor_id=idd
        obj.parent_id=uid
        obj.status="paid"
        obj.save()

        return HttpResponseRedirect('/temp/parent',)
    return render(request,'payment/payment.html',context)