
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from usuario.views import UsuarioViewSet
from paciente.views import PacienteViewSet, ProprietarioViewSet

router = routers.DefaultRouter()
router.register(
    'usuario', UsuarioViewSet,
)
router.register(
    'paciente', PacienteViewSet,
)
router.register(
    'proprietario', ProprietarioViewSet
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Administração da API de Veterinaria'
