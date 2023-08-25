from django.db import models

from versions.querysets.python_version import PythonVersionQueryset
from versions.querysets.django_version import DjangoVersionQueryset


class VersionBase(models.Model):
    version_id = models.CharField(max_length=10, unique=True, primary_key=True)
    release_date = models.DateField()
    end_of_life_date = models.DateField(null=True, blank=True)
    is_supported = models.BooleanField(default=True)
    doc_url = models.URLField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.version_id


class PythonVersion(VersionBase):
    objects = PythonVersionQueryset.as_manager()


class DjangoVersion(VersionBase):
    is_lts = models.BooleanField(default=False)
    python_version = models.ForeignKey(PythonVersion, on_delete=models.CASCADE)
    objects = DjangoVersionQueryset.as_manager()

