from django.conf.urls import url
from student import views

urlpatterns=[
    url('manage_students/',views.manage_students),
    url('reg_students/',views.reg_students),
    url('view_students/',views.view_student),
    url('view_exam/(?P<idd>\w+)',views.view_exam),
    url('accp/(?P<idd>\w+)', views.accpt),
    url('reject/(?P<idd>\w+)', views.reject),
    url('student_profile/', views.student_profile),
    url('view_student_admin/', views.view_student_admin),

]
