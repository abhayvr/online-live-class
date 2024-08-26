from django.conf.urls import url
from Question import views

urlpatterns=[
    url('add_questions/',views.reg_questions),
]
