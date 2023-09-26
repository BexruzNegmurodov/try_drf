from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly

from .models import Article
from .serializers import ArticleSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])  # login qilgan bo'lishi kk
def article_list_view(request):
    # http://127.0.0.1:8000/api/article/list
    articles = Article.objects.all()
    title = request.GET.get('q')
    if title:
        articles = articles.filter(title__icontains=title)
    # paginator = PageNumberPagination()
    # paginator.page_size = 1
    # result_page = paginator.paginate_queryset(articles, request)
    serializers = ArticleSerializer(articles, many=True)
    return Response(serializers.data, status=200)


@api_view(['GET'])
def article_retrieve_view(request, pk):
    # http://127.0.0.1:8000/api/article/retrieve/{pk}
    article = get_object_or_404(Article, id=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsOwnerOrReadOnly])
def article_create_view(request):
    # http://127.0.0.1:8000/api/article/create
    data = request.data
    data['author'] = request.user.id
    serializer = ArticleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsOwnerOrReadOnly])
def article_list_create_view(request):
    # http://127.0.0.1:8000/api/article/list_create
    if request.method == 'GET':
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=200)
    if request.method == 'POST':
        data = request.data
        data['author'] = request.user.id
        serializer = ArticleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsOwnerOrReadOnly])
def article_update_view(request, pk):
    # http://127.0.0.1:8000/api/article/update/{pk}
    instance = get_object_or_404(Article, id=pk)
    data = request.data
    serializer = ArticleSerializer(instance=instance, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def article_delete_view(request, pk):
    # http://127.0.0.1:8000/api/article/delete/{pk}
    article = get_object_or_404(Article, id=pk)
    article.delete()
    return Response({"detail": "Article delete"})


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def article_rud_view(request, pk):
    # http://127.0.0.1:8000/api/article/rud/{pk}
    instance = get_object_or_404(Article, id=pk)
    if request.method == 'GET':
        serializers = ArticleSerializer(instance)
        return Response(serializers.data, status=200)
    elif request.method in ['PUT', 'PATCH']:
        data = request.data
        serializer = ArticleSerializer(instance=instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        instance.delete()
        return Response({"detail": "Article delete"})
