#from django.conf.urls import url
from django.urls import path
from EmployeeApp import views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('Emp/', views.employeeApi),
    path('Dept/', views.departmentApi),
    path('SaveFile/', views.SaveFile),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)