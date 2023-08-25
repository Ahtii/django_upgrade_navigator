from django.contrib import admin
from django.urls import path
from django.urls import include
from djang_upgrade_navigator.constants import CURRENT_API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{CURRENT_API_VERSION}/versions/', include('versions.urls')),
]
