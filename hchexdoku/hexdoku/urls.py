from django.urls import path
from .views import home, check_answer

urlpatterns = [
    path('', home, name='home'),
    path('check_answer', check_answer, name='check_answer'),
]