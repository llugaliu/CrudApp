from django.urls import path
from . import views

urlpatterns = [
    path('',views.employer,name='employer'),
    path('edit-employer/<int:pk>/',views.edit_employer,name='edit-employer'),
    path('delete-employer/<int:pk>/',views.delete_employer,name='delete-employer')
]