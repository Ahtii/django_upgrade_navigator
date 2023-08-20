from rest_framework import serializers

from versions.models import DjangoVersion
from versions.models import PythonVersion


class DjangoVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoVersion
        fields = '__all__'


class PythonVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonVersion
        fields = '__all__'
