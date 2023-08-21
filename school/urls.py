from django.contrib import admin
from django.urls import path, include

from courses.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('courses.urls')),
    path('api/v2/', include(router.urls)),
]
