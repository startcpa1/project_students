from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, StudentCreateView, StudentUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),

]