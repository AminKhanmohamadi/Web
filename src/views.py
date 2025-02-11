from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Knowledge, Article
from .serializers import KnowledgeSerializer, ArticleSerializer


# Create your views here.

class KnowledgeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = KnowledgeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Knowledge.objects.all()
        if not user.is_superuser:
            queryset = queryset.filter(status="Pub")
        return queryset


class ArticleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.all()
        if not user.is_superuser:
            queryset = queryset.filter(status='Pub')
        return queryset
