from django.contrib import admin
from django.urls import path
from task.views import endpoint_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task', endpoint_task),
]
