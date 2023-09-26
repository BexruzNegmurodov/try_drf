from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="author.username", read_only=True
    )

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'username', 'title', 'description', 'modified_date', 'created_date']

        extra_kwargs = {
            'author': {'required': True}
        }
