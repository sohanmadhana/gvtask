from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.employee, name='employee' ),
    path('add-employee/', views.addEmployee, name='add-employee' ),
    path('edit-employee/<str:id>/', views.editEmployee, name='edit-employee' ),
    path('delete-employee/<str:id>/', views.deleteEmployee, name='delete-employee' ),
    path('update-status/<str:id>/', views.updateStatus, name='update-status' ),
    
]