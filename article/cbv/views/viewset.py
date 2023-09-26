from rest_framework import viewsets, status

from article.models import Article
from article.cbv.serializers import ArticleGenericSerializer, ArticleCreateSerializer
from article.cbv.permissions import IsAuthorOrReadOnly
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/article/cbv/article_viewset/
    queryset = Article.objects.all()
    serializer_class = ArticleGenericSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        # list retrieve update create destroy
        if self.action in ['list', 'retrieve']:
            return ArticleGenericSerializer
        return ArticleCreateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"detail": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
