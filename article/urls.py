from django.urls import path, include
from .views import article_list_view, article_retrieve_view, article_create_view, article_list_create_view, \
    article_update_view, article_delete_view, article_rud_view

app_name = 'article'

urlpatterns = [
    path('list/', article_list_view, name='list'),
    path('retrieve/<int:pk>/', article_retrieve_view, name='retrieve'),
    path('create/', article_create_view, name='create'),
    path('list_create/', article_list_create_view, name='list_create'),
    path('update/<int:pk>/', article_update_view, name='update'),
    path('delete/<int:pk>/', article_delete_view, name='delete'),
    path('rud/<int:pk>/', article_rud_view, name='rud'),
    path('cbv/', include('article.cbv.urls', namespace='cbv'))
]
