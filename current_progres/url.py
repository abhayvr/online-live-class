from django.conf.urls import url
from current_progres import views

urlpatterns=[
    url('current_progres/',views.current_progres),
    url('view_progres/',views.view_progres),
    url('view_progress_parent/',views.view_progres_parent)
]