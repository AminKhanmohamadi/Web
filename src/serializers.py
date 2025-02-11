from rest_framework import serializers
from .models import Knowledge , Article




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id' , 'title' , 'created_by' , 'created_at' , 'updated_at' , 'summery']


class KnowledgeSerializer(serializers.ModelSerializer):
    article = serializers.HyperlinkedRelatedField(view_name='article-detail', read_only=True , many=True)
    class Meta:
        model = Knowledge
        fields = ['id' , 'title' , 'created_by' , 'created_at' , 'updated_at' , 'article']




