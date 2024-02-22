from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'veiculos', views.VeiculosViewSet, basename='VeiculosViewSet')

urlpatterns = router.urls




#authentication_classes=[JWTAuthentication],permission_classes=[IsAuthenticated]