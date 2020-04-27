from django.contrib import admin
from django.urls import path, include
from quiz_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('quiz_app/', include('quiz_app.urls'))
]
