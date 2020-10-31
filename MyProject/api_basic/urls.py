from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article_model', ArticleModelViewSet, basename='article_model')

urlpatterns = [
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),
    # path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:id>/', ArticleDetails.as_view()),
    # path('generic/article/', GenericAPIView.as_view()),
    # path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
]
