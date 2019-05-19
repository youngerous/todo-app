from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('todo/list/', views.ApiTodoListView.as_view(), name='list'),
    path('todo/<int:pk>/delete/', views.ApiTodoDeleteView.as_view(), name='delete'),
    path('todo/create/', views.ApiTodoCreateView.as_view(), name='create'),
]
