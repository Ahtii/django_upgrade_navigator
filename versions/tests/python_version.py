from django.test import TestCase
from django.shortcuts import reverse

from rest_framework.test import APIClient
from rest_framework import status

from django.core.management import call_command

from versions.models import PythonVersion

from versions.serializers import PythonVersionSerializer


class PythonDjangoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        call_command('loaddata', 'versions/fixtures/python_version.json')

    def test_get_endpoint_with_pk(self):
        python_version = PythonVersion.objects.first()
        with_pk_url = reverse('python_version', kwargs={'pk': python_version.pk})
        response = self.client.get(with_pk_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PythonVersionSerializer([python_version], many=True).data)

    def test_get_endpoint_without_pk(self):
        python_versions = PythonVersion.objects.all()
        with_pk_url = reverse('python_versions')
        response = self.client.get(with_pk_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PythonVersionSerializer(python_versions, many=True).data)

