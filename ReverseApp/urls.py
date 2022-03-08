from django.urls import re_path
from ReverseApp import views

from django.conf.urls.static import static
from django.conf import settings


# urlpatterns = [
#     re_path(r'^topic$',views.departmentApi),
#     re_path(r'^department/([0-9]+)$',views.departmentApi),

#     re_path(r'^employee$',views.employeeApi),
#     re_path(r'^employee/([0-9]+)$',views.employeeApi),

#     re_path(r'^employee/savefile', views.SaveFile)
    
# ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = [
    re_path(r'^topic$', views.topicApi),
    re_path(r'^topic/([0-9]+)$', views.topicApi),
    re_path(r'^comment$', views.commentApi),
    re_path(r'^user$', views.userApi),
]