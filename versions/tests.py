from django.test import TestCase
from django.shortcuts import reverse

from rest_framework.test import APIClient
from rest_framework import status

from versions.models import DjangoVersion
from versions.models import PythonVersion

from versions.serializers import DjangoVersionSerializer


from django.test import TestCase
from django.shortcuts import reverse

from rest_framework.test import APIClient
from rest_framework import status

from versions.models import PythonVersion
from versions.models import DjangoVersion

from versions.serializers import PythonVersionSerializer
from versions.serializers import DjangoVersionSerializer


class PythonVersionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.python_version = PythonVersion.objects.create(
            version_id="3.8.0",
            release_date="2019-10-14",
            end_of_life_date="2024-04-10",
            is_supported=True,
            doc_url="https://www.python.org/downloads/release/python-380/"
        )
        self.endpoint_url = reverse('python_version', kwargs={'pk': self.python_version.pk})

    def test_response(self):
        response = self.client.get(self.endpoint_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PythonVersionSerializer(self.python_version).data)


class DjangoVersionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.python_version = PythonVersion.objects.create(
            version_id="3.8.0",
            release_date="2019-10-14",
            end_of_life_date="2024-04-10",
            is_supported=True,
            doc_url="https://www.python.org/downloads/release/python-380/"
        )
        self.django_version = DjangoVersion.objects.create(
            version_id='4.0',
            release_date="2021-10-01",
            end_of_life_date="2022-04-01",
            is_supported=True,
            doc_url='https://docs.djangoproject.com/en/4.0/releases/4.0/',
            python_version_id=self.python_version
        )
        self.endpoint_url = reverse('django_version', kwargs={'pk': self.django_version.pk})

    def test_response(self):
        response = self.client.get(self.endpoint_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, DjangoVersionSerializer(self.django_version).data)

