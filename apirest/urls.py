from school.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculaAluno, ListaAlunoMatriculados
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunoMatriculados.as_view()),
]
