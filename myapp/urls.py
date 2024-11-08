from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
