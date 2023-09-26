from django.test import TestCase
from article.models import Article
from article.serializers import ArticleSerializer
from article.views import article_list_view
import json
from rest_framework import status


class TestSearchArticleList(TestCase):

    def test_search_list(self):
        queryset = Article.objects.create(title='bexruz', description="men uddaladim")
        queryset1 = Article.objects.create(title='bexruz0', description="men uddaladim")
        queryset2 = Article.objects.create(title='bexruz', description="men uddaladim")

        response = self.client.get('/api/article/list/?q=bexruz')
        qs = Article.objects.filter(title__icontains='bexruz')
        sz = ArticleSerializer(qs, many=True)
        print("1", json.dumps(response.json()))
        print("2", json.dumps(sz.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.dumps(response.json()), json.dumps(sz.data))



