from django.contrib import admin
from django.urls import path, include
from todolists import views

# admin / youngadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodoView.as_view(), name='home'),   
    path('api/', include('api.urls')),
]
