from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from versions.models import DjangoVersion
from versions.models import PythonVersion

from versions.serializers import DjangoVersionSerializer
from versions.serializers import PythonVersionSerializer


class DjangoVersionAPIView(GenericAPIView):
    queryset = DjangoVersion.objects.all()
    serializer_class = DjangoVersionSerializer

    def get(self, request, pk):
        instance = self.get_object()
        serialized_data = self.get_serializer(instance).data
        return Response(serialized_data)


class PythonVersionAPIView(GenericAPIView):
    queryset = PythonVersion.objects.all()
    serializer_class = PythonVersionSerializer

    def get(self, request, pk):
        instance = self.get_object()
        serialized_data = self.get_serializer(instance).data
        return Response(serialized_data)
