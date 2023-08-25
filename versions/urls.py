from django.urls import path

from versions.views import DjangoVersionAPIView
from versions.views import PythonVersionAPIView


urlpatterns = [
    path('django/', DjangoVersionAPIView.as_view(), name='django_versions'),
    path('django/<str:pk>/', DjangoVersionAPIView.as_view(), name='django_version'),
    path('python/', PythonVersionAPIView.as_view(), name='python_versions'),
    path('python/<str:pk>/', PythonVersionAPIView.as_view(), name='python_version'),
]
