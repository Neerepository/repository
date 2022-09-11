#from importlib.resources import path
#from unicodedata import name
#from django.conf.urls import patterns, include, urls
#from .import views
from django.urls import path
from .views import *
#CategoryListView, ProyectosListView, DetalleDetailView, ProyectosCreateView, ProyectosUpdateView, ProyectosDeleteView, SubcategoriaCreateView, DetalleCatelView,AddLike, DetalleCatelView,AddDislike
#from .views  import ProyectosListView
#urlpattern= patterns('',
# url(r'˄buscar/$', Buscar)
from django.contrib.auth.decorators import login_required

#)
projectpatterns = ([ 
    path('', ProyectosListView.as_view(), name="proyectos"),
    #path('busqueda/', home , name="busqueda"),
    path('<int:pk>/<slug:Project_slug>/', DetalleDetailView.as_view(), name="detalles"), 
    path('create/', ProyectosCreateView.as_view(), name='Añadir'),
    path('createsubcategori/', SubcategoriaCreateView.as_view(), name='AñadirSubCategoria'),
    path('update/<int:pk>/', ProyectosUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProyectosDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/like/',login_required(AddLike.as_view()), name='like'),
    path('<int:pk>/dislike', login_required(AddDislike.as_view()), name='dislike'),
    path('categorias/',CategoryListView.as_view(), name="categorias"),
    path('<int:pk>/',DetalleCatelView.as_view(), name="detallescategoria"), 
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='deletecategoria'),
    path('lista-herramientas/', ListherramientasPdf.as_view(), name='projecto_all')
    #path('proyectos/',portfolio_views.proyectos, name="proyectos"),
    #path('detalle/<int:project_id>/', views.detalle, name="detalle"), 

], 'portfolio')