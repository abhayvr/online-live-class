from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('add_feedback_student/',views.add_feedback_student),
    url('add_feedback_parent/',views.add_feedback_parent),
    url('view_feedback/',views.view_feedback_tutor),
    url('view_feedback_admin/',views.view_feedback_admin),
]
