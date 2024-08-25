from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('admin_reply/(?P<idd>\w+)',views.admin_reply),
    url('complaint/',views.complaint),
    url('comp_student',views.complaint_student),
    url('view_student',views.view_student),
    url('view_tutor',views.view_tutor),
    url('post_replay/',views.post_replay),
    url('view_admin/',views.view_admin),

]