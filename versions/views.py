from rest_framework.views import APIView
from rest_framework.response import Response

from versions.models import DjangoVersion
from versions.models import PythonVersion

from versions.serializers import DjangoVersionSerializer
from versions.serializers import PythonVersionSerializer


class DjangoVersionAPIView(APIView):
    def get(self, request, pk=None):
        instances = DjangoVersion.objects.by_pk_else_all(pk)
        serialized_data = DjangoVersionSerializer(instances, many=True).data if instances else dict()
        return Response(serialized_data)


class PythonVersionAPIView(APIView):
    def get(self, request, pk=None):
        instances = PythonVersion.objects.by_pk_else_all(pk)
        serialized_data = PythonVersionSerializer(instances, many=True).data if instances else dict()
        return Response(serialized_data)
