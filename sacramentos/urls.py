from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('diocesis', DiocesisViewSet)
router.register('parroquias', ParroquiaViewSet)
router.register('sacerdotes', SacerdoteViewSet)
router.register('personas', PersonaViewSet)
router.register('sacramentos', SacramentoViewSet)
router.register('celebraciones', CelebracionViewSet)

urlpatterns = [ path('', include(router.urls)) ]
