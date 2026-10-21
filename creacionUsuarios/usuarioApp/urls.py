from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as vw
urlpatterns = [
    path('',vw.lista_empleados,name='lista_empleados'),
    path('empleado/<int:pk>/',vw.detalle_empleado,name='detalle_empleado'),
    path('crear/',vw.crear_empleado,name='crear_empleado'),
    path('editar/<int:pk>/',vw.editar_empleado,name='editar_empleado'),
    path('eliminar/<int:pk>/', vw.eliminar_empleado, name='eliminar_empleado'),
    path('login/',auth_views.LoginView.as_view(template_name='empleados/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
]