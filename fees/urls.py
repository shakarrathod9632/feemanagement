from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('payments/', views.payments, name='payments'),
    path('add-payment/', views.add_payment, name='add_payment'),
    path('stats/', views.stats, name='stats'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
]
