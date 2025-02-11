import os

from celery import shared_task
from dotenv import load_dotenv
from openai import OpenAI

from .models import Article

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


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


