from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, ThreadViewSet, UserCreateAPIView


v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="post_id"
)
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments/(?P<id>\d+)/threads", ThreadViewSet, basename="id"
)
urlpatterns = [
    path("v1/", include(v1_router.urls),),
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/user_create/", UserCreateAPIView.as_view()),
    ]
