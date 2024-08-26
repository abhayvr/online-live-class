from django.conf.urls import url
from parent_chat import views

urlpatterns=[
    url('tut/',views.con),
    url('ppp/(?P<idd>\w+)',views.cochat),

    url('parr/',views.std),
    url('vvv/(?P<idd>\w+)',views.stchat),

]