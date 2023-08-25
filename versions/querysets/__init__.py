from django.db.models import QuerySet


class BaseQueryset(QuerySet):

    def by_pk_else_all(self, pk):
        if pk:
            return self.filter(pk=pk)
        return self
