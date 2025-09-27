from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new", PostCreateView.as_view(), name="post-new"),
    path("post/<int:pk>/editar", PostUpdateView.as_view(), name="post-edit"),
]
