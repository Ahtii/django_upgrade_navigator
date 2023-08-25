from rest_framework.views import APIView
from rest_framework.response import Response

from versions.models import DjangoVersion
from versions.models import PythonVersion

from versions.serializers import DjangoVersionSerializer
from versions.serializers import PythonVersionSerializer


class BaseAPIView(APIView):
    model = None
    serializer = None

    def get(self, request, pk=None):
        instances = self.model.objects.by_pk_else_all(pk)
        serialized_data = self.serializer(instances, many=True).data if instances else dict()
        return Response(serialized_data)


class DjangoVersionAPIView(BaseAPIView):
    model = DjangoVersion
    serializer = DjangoVersionSerializer

    def get(self, request, pk=None):
        return super().get(request, pk)


class PythonVersionAPIView(BaseAPIView):
    model = PythonVersion
    serializer = PythonVersionSerializer

    def get(self, request, pk=None):
        return super().get(request, pk)
