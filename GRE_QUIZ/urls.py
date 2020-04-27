from django.contrib import admin
from django.urls import path, include
from quiz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('quiz_app/', include('quiz_app.urls'))
]
