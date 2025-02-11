from django.contrib import admin
from .models import Knowledge ,Article
from src.tasks import summarize_article
# Register your models here.
admin.site.register(Knowledge)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_by')
    list_filter = ('created_by',)

