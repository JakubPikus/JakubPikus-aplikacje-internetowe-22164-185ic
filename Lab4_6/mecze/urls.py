from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .views import UserViewSet, MeczViewSet



urlpatterns = [
    
    #path('users/', UserList.as_view()),
    #path('users/<int:pk>/', UserDetail.as_view()),
    #path('<int:pk>/', MeczDetail.as_view()),
    #path('', MeczList.as_view()),
]


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', MeczViewSet, basename='mecz')
urlpatterns = router.urls
