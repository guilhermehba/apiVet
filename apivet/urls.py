
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usuario.views import UsuarioViewSet
from paciente.views import PacienteViewSet, ProprietarioViewSet, AnamneseGeralViewSet, AnamneseEspecialViewSet,ExameObjetivoViewSet, ExameComplementarViewSet,MedicacaoViewSet,ConclusaoViewSet,ObservacaoViewSet

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

router.register(
    'anamnese_geral', AnamneseGeralViewSet
)

router.register(
    'anamnese_especial', AnamneseEspecialViewSet
)

router.register(
    'exame_objetivo', ExameObjetivoViewSet
)

router.register(
    'exame_complementar', ExameComplementarViewSet
)

router.register(
    'medicacao', MedicacaoViewSet
)

router.register(
    'conclusao', ConclusaoViewSet
)

router.register(
    'observacao', ObservacaoViewSet
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Administração da API de Veterinaria'
