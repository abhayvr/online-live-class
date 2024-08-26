from django.conf.urls import url
from tutor import views

urlpatterns=[
    url('manage_tutor/',views.manage_tutor),
    url('reg_tutor/',views.reg_tutor),
    url('update_tutor/',views.update_tutor),
    url('view_tutor/',views.view_tutor),
    url('accp/(?P<idd>\w+)',views.accpt),
    url('reject/(?P<idd>\w+)',views.reject),
    url('view_tutor_admin/', views.view_tutor_admin),
    url('view_tutor_parent/', views.view_tutor_parent),
]