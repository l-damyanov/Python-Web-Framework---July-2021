from django.urls import path
from articles.web.views import ArticlesListView, ArticleCreateView, SourceCreateView, SourceDetailView, SourceListView


urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('create-article/', ArticleCreateView.as_view(), name='create article'),
    path('create-source/', SourceCreateView.as_view(), name='create source'),
    path('list-sources/', SourceListView.as_view(), name='source list'),
    path('source-details/<int:pk>', SourceDetailView.as_view(), name='source details'),
]
