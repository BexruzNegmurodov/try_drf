from django.urls import path, include
from article.cbv.views.views import CategoryAPIList, CategoryCreateAPIView, Category_RudDetail_API_View
from article.cbv.views.generic_views import ArticleListGenericView, ArticleRudAPIViView
from article.cbv.views.viewset import ArticleViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')


app_name = 'cbv'

urlpatterns = [
    path('list/', CategoryAPIList.as_view(), name='cbv_list'),
    path('create/', CategoryCreateAPIView.as_view(), name='create'),
    path('ruddetail/<int:id>/', Category_RudDetail_API_View.as_view(), name='rud_detail'),
    path('list_generic/', ArticleListGenericView.as_view(), name='list_generic'),
    path('rud_generic/<int:pk>/', ArticleRudAPIViView.as_view(), name='rud_generic'),

    path('article_viewset/', include(router.urls)),
]