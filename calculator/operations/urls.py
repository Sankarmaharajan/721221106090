from django.contrib import admin
from django.urls import path
from .views import array
urlpatterns = [
    path('admin/', admin.site.urls),
    path('numbers/',array,name="array"),
]