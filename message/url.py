from django.conf.urls import url
from message import views
urlpatterns=[
    url('msg/',views.chatload),
    url('chat/',views.up),
    # url('chat/',views.chbottest),

]