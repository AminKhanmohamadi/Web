from rest_framework.routers import DefaultRouter

from .views import KnowledgeViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'knowledge', KnowledgeViewSet , 'knowledge')
router.register(r'article', ArticleViewSet , 'article')


urlpatterns = router.urls