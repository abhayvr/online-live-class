"""knowledge_dot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from temp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('chat/',include('chat.url')),
    url('complaint/',include('complaint.url')),
    url('current_progres/',include('current_progres.url')),
    url('doubt/',include('doubt.url')),
    url('exam_schedule/',include('exam_schedule.url')),
    url('feedback/',include('feedback.url')),
    url('live/',include('live.url')),
    url('login/',include('login.url')),
    url('notifications/',include('notifications.url')),
    url('parent/',include('parent.url')),
    url('payment/',include('payment.url')),
    url('student/',include('student.url')),
    url('study_material/',include('study_material.url')),
    url('time_schedule/',include('time_schedule.url')),
    url('tutor/',include('tutor.url')),
    url('videos/',include('videos.url')),
    url('temp/', include('temp.url')),
    url('parent_chat/', include('parent_chat.url')),
    url('message/', include('message.url')),
    url('conference/', include('conference.url')),
    url('Question/',include('Question.url')),
    url('$', views.home)
]
