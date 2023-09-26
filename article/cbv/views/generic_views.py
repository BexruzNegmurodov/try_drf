from rest_framework import status, generics
from article.cbv.permissions import IsAuthorOrReadOnly

from article.models import Article, Category
from article.cbv.serializers import ArticleGenericSerializer, ArticleCreateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArticleListGenericView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/article/cbv/list_generic/
    queryset = Article.objects.all()
    serializer_class = ArticleGenericSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ArticleGenericSerializer
        return ArticleCreateSerializer

    # def get_serializer_context(self):
    #     ctx = super().get_serializer_context()
    #     print(ctx)
    #     return ctx     // serializer ichiga request ni olish


class ArticleRudAPIViView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/article/cbv/rud_generic/{pk}/
    queryset = Article.objects.all()
    serializer_class = ArticleGenericSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ArticleGenericSerializer
        return ArticleCreateSerializer

