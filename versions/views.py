from rest_framework.views import APIView
from rest_framework.response import Response

from versions.models import DjangoVersion
from versions.models import PythonVersion

from versions.serializers import DjangoVersionSerializer
from versions.serializers import PythonVersionSerializer


class DjangoVersionAPIView(APIView):
    def get(self, request, pk):
        instance = DjangoVersion.objects.filter(pk=pk).first()
        serialized_data = DjangoVersionSerializer(instance).data if instance else dict()
        return Response(serialized_data)


class PythonVersionAPIView(APIView):
    def get(self, request, pk):
        instance = PythonVersion.objects.filter(pk=pk).first()
        serialized_data = PythonVersionSerializer(instance).data if instance else dict()
        return Response(serialized_data)
