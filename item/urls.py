from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.add_new_item, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_items, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]