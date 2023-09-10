
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add, name='add_employee'),
    path('<int:id>/', views.add, name='edit_employee'),
    path('list/', views.index, name='index_employee'),
    path('delete/<int:id>/', views.destroy, name='delete_employee'),
]
