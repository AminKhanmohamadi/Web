from celery import shared_task
from openai import OpenAI
from .models import Article
import json
OPENAI_API_KEY = "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"



@shared_task
def summarize_article(article_id):
    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )
    try:
        article = Article.objects.get(id=article_id)

        if not article.description:
            return f"Article {article_id} has no description to summarize."

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that summarizes articles."},
                {"role": "user", "content": article.description},
            ],
            max_tokens=100
        )
        summary_text = response.choices[0].message.content
        if summary_text:
            article.summery = summary_text.strip()
            article.save(update_fields=["summery"])

            return f"Article {article_id} summarized successfully."

        return f"Invalid response format for Article {article_id}."

    except Article.DoesNotExist:
        return f"Article with ID {article_id} not found."

    except openai.error.OpenAIError as e:
        return f"OpenAI Error: {str(e)}"