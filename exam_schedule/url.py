from django.conf.urls import url
from exam_schedule import views

urlpatterns=[
    url('exam_schedule/',views.exam_schedule),
    url('view_exam/',views.view_exam),
    url('view_exam_parent/',views.view_exam_parent),
    url('view_exam_admin/', views.view_exam_admin),
]