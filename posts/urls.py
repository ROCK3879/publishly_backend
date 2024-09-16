from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet,CommentViewSet, like_post,dislike_post
router = DefaultRouter()
router.register(r'posts/', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    
    # path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),
    # path('questions/update-latest-version/<int:pk>/', QuestionViewSet.as_view({'patch': 'update_latest_version'}), name='update-latest-version'),    path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),

    path('posts/', PostViewSet.as_view({'get': 'list'}), name='posts-list'),
    path('post/create/<int:user_id>/', PostViewSet.as_view({'post': 'create'}), name='post-create'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-retrieve'),
    # path('customer/register/', register_customer, name="customer-register" ),
    path('post/<int:pk>/', PostViewSet.as_view({'delete': 'delete'}), name='post-delete'),
    path('post/update/<int:pk>/', PostViewSet.as_view({'put': 'update'}), name='post-update'),
    path('posts/like/<int:post_id>/', like_post, name='post-like'),
    path('posts/dislike/<int:post_id>/', dislike_post, name='post-dislike'),
    # Comment

    path('comments/', CommentViewSet.as_view({'get': 'list'}), name='comments-list'),
    path('comment/create/<int:post_id>/', CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve'}), name='comment-retrieve'),
    path('comment/update/<int:pk>/', CommentViewSet.as_view({'put': 'update'}), name='comment-update'),

    path('comment/<int:pk>/', CommentViewSet.as_view({'delete': 'delete'}), name='comment-delete'),
]
