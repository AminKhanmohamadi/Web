from rest_framework import serializers
from .models import Knowledge , Article




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description", "created_by", "created_at", "updated_at", "summery", "status"]


class KnowledgeSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    class Meta:
        model = Knowledge
        fields = ["id", "title", "created_by", "created_at", "updated_at", "status", "articles"]

    def get_articles(self, obj):
        user = self.context["request"].user
        articles = obj.article.all()

        if not user.is_superuser:
            articles = articles.filter(status="Pub")
        return ArticleSerializer(articles, many=True, context=self.context).data


