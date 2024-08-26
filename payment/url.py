from django.conf.urls import url
from payment import views

urlpatterns=[
    url('manage_payment/',views.manage_payment),
    url('payment/(?P<idd>\w+)',views.payment),
    url('view_payment/',views.view_payment),
]