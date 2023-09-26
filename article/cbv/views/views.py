from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from article.cbv.permissions import IsAdminOrReadOnly
from article.cbv.serializers import CategoryAPVISerializers
from article.models import Category


class CategoryAPIList(views.APIView):
    # http://127.0.0.1:8000/api/article/cbv/list/
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializers = CategoryAPVISerializers(categories, many=True)
        return Response(serializers.data, status=200)


class CategoryCreateAPIView(views.APIView):
    # http://127.0.0.1:8000/api/article/cbv/create/
    serializer_class = CategoryAPVISerializers
    permission_classes = [IsAdminUser]

    def get_serializer_class(self, **kwargs):
        return self.serializer_class(**kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Category_RudDetail_API_View(views.APIView):
    # http://127.0.0.1:8000/api/article/cbv/ruddetail/{pk}
    class_model = Category
    serializer_class = CategoryAPVISerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset = get_list_or_404(self.class_model)
        return queryset

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Category, id=kwargs.get("id"))
        return obj

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get(self, *args, **kwargs):
        obj = self.get_object(*args, **kwargs)
        serializer = self.get_serializer_class(obj)
        return Response(serializer.data, status=200)

    def put(self, *args, **kwargs):
        obj = self.get_object(*args, **kwargs)
        serializer = self.get_serializer_class(data=self.request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, *args, **kwargs):
        obj = self.get_object(*args, **kwargs)
        serializer = self.get_serializer_class(data=self.request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, *args, **kwargs):
        obj = self.get_object(*args, **kwargs)
        obj.delete()
        return Response({"detail": "deleted"}, status=status.HTTP_204_NO_CONTENT)
