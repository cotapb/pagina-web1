
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('pregunta',views.pregunta, name="pregunta"),
    path('estadistica',views.estadistica, name="estadistica"),
    path('informacion', views.informacion, name='informacion'),
    path('preguntas', views.preguntas, name='preguntas'),
    path('pregunta1', views.pregunta1, name='pregunta1'),

 
     
]
