from django.conf.urls import url
from videos import views

urlpatterns=[
    url('add_videos/',views.add_videos),
    url('view_videos/',views.view_videos)
]