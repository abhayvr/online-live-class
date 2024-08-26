from django.conf.urls import url
from study_material import views

urlpatterns=[
    url('add_studymaterial/',views.add_studymaterial),
    url('download_studymaterial/',views.dowmload_studymaterial),
    url('view_studymaterial/',views.view_studymaterial)
]