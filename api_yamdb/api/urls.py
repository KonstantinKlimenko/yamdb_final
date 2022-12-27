from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, SignInViewSet, SignUpViewSet,
                       TitleViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register(r"categories", CategoryViewSet)
router_v1.register(r"genres", GenreViewSet)
router_v1.register(r"titles", TitleViewSet)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews"
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)" r"/comments",
    CommentViewSet,
    basename="comments",
)
router_v1.register(r"users", UserViewSet, basename="users",)
# router_v1.register("auth/signup", SignUpViewSet.as_view(), basename='signup')
router_v1.register("auth/token", SignInViewSet, basename='signin')

urlpatterns = [
    path("v1/auth/signup/", SignUpViewSet.as_view(), name='signup'),
    path("v1/", include(router_v1.urls)),
]
