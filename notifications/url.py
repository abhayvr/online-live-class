from django.conf.urls import url
from notifications import views

urlpatterns=[
    url('add_notifications/',views.add_notifications),
    url('view_notifications/',views.view_notifications),
    url('view_notification_parent/',views.view_notifications_parent)
]