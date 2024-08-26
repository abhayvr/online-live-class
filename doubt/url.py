from django.conf.urls import url
from doubt import views

urlpatterns=[
    url('replay/(?P<idd>\w+)',views.replay),
    url('doubt/',views.post_doubt),
    url('view_db/',views.view_doubt),
    url('view_doubt_student/',views.view_doubt_student)
]