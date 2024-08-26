from django.shortcuts import render
from videos.models import Videos
from django.core.files.storage import FileSystemStorage
# Create your views here.
def add_videos(request):
    # ss=request.session["u_id"]
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Videos()
        # obj.video_upload=request.POST.get('Video')
        myfile = request.FILES['Video']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.video_upload = myfile.name
        obj.tutor_id=uid
        obj.student_id=1
        obj.save()
    return render(request,'videos/videos.html')

def view_videos(request):
    obj=Videos.objects.all()
    context={
        'x':obj
    }
    return render(request,'videos/view_video.html',context)
