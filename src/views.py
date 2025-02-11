from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Knowledge, Article
from .serializers import KnowledgeSerializer, ArticleSerializer


# Create your views here.

class KnowledgeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = KnowledgeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Knowledge.objects.all()
        return Knowledge.objects.filter(status='Pub')


class ArticleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Article.objects.all()
        return Article.objects.filter(status='Pub')