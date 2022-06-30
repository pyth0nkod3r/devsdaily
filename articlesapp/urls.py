from django.urls import path 
from .views import (
    ArticleListView, 
    ArticleUpdateView, 
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    )

urlpatterns=[
    path('', ArticleListView.as_view(), name='articlelist'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='articleupdate'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='articledelete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articledetail'),
    path('new/', ArticleCreateView.as_view(), name='articlecreate'),
    ]