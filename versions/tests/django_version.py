from django.test import TestCase
from django.shortcuts import reverse

from rest_framework.test import APIClient
from rest_framework import status

from django.core.management import call_command

from versions.models import DjangoVersion

from versions.serializers import DjangoVersionSerializer


class DjangoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        call_command('loaddata', 'versions/fixtures/python_version.json')
        call_command('loaddata', 'versions/fixtures/django_version.json')

    def test_get_endpoint_with_pk(self):
        django_version = DjangoVersion.objects.first()
        with_pk_url = reverse('django_version', kwargs={'pk': django_version.pk})
        response = self.client.get(with_pk_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, DjangoVersionSerializer([django_version], many=True).data)

    def test_get_endpoint(self):
        django_versions = DjangoVersion.objects.all()
        with_pk_url = reverse('django_versions')
        response = self.client.get(with_pk_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, DjangoVersionSerializer(django_versions, many=True).data)
