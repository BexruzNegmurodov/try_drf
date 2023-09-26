from rest_framework import serializers
from article.models import Category, Article


class CategoryAPVISerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ArticleGenericSerializer(serializers.ModelSerializer):
    category = CategoryAPVISerializers(read_only=True)
    username = serializers.CharField(
        source="author.username", read_only=True
    )

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'username', 'title', 'description', 'modified_date', 'created_date']

        extra_kwargs = {
            'author': {'required': True}
        }

        # read_only_fields = ['author']


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'description', 'modified_date', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        # category = validated_data.get('category')
        instance = super().create(validated_data)
        instance.author = user
        # instance.category = category
        instance.save()
        return instance
