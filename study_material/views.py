from django.shortcuts import render
from study_material.models import StudyMaterial
from django.core.files.storage import FileSystemStorage
# Create your views here.
def add_studymaterial(request):
    uid=request.session["u_id"]
    if request.method=='POST':
       obj=StudyMaterial()
       obj.description=request.POST.get('description')
       # obj.study_material=request.POST.get('studymaterial')
       myfile=request.FILES['studymaterial']
       fs=FileSystemStorage()
       filename=fs.save(myfile.name, myfile)
       obj.study_material=myfile.name
       obj.student_id=1
       obj.tutor_id=uid
       obj.save()
    return render(request,'study_material/study material.html')

def dowmload_studymaterial(request):
    return render(request,'study_material/study material download.html')

def view_studymaterial(request):
    obj=StudyMaterial.objects.all()
    context={
        'x':obj
    }
    return render(request,'study_material/view_studymaterial.html',context)