from rest_framework.routers import DefaultRouter
from ejemploApp.views import EstudianteViewSet

router = DefaultRouter()
router.register('estudiante',EstudianteViewSet)
urlpatterns=router.urls