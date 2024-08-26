from django.shortcuts import render
from Question.models import Questions


# Create your views here.

def reg_questions(request):
    obj = Questions.objects.all()
    context = {
        'x': obj
    }

    if request.method=='POST':
        obj=Questions()
        obj.questions=request.POST.get('question')
        obj.option1=request.POST.get('op1')
        obj.option2=request.POST.get('op2')
        obj.option3=request.POST.get('op3')
        obj.option4=request.POST.get('op4')
        obj.correct_option=request.POST.get('correct option')
        obj.subject=request.POST.get('Subject')
        obj.save()

    return render(request,'Question/postquest.html',context)