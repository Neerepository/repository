from ast import Return, arg
from contextlib import redirect_stderr
from distutils.command.build_scripts import first_line_re
from typing import Generic
from django_filters import rest_framework as filters
import string
from tkinter.tix import Form
from urllib import request
from .models import *
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .froms import ProyectoForm,SubCategoryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.shortcuts import render
from .utils import render_to_pdf

class EjemploListView(LoginRequiredMixin,ListView):

    login_url = reverse_lazy('registration:login.html')


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
         
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    

class ProjetcListView(ListView):
    model =  Project
    template_name = 'portfolio\project_list.html'
    context_object_name = 'herrammientas'
class ProjetcListView(View):
    def get(self, request, *args, **kwargs):
        query= self.request.GET.get('Kword1')
        projectList= Project.objects.filter(categoria__icontains=query)
        data = {
            'projectList':projectList   
        }
        return render(request, 'portfolio:project_list.html', data)
   
class ListherramientasPdf(View):

    def get(self, request, *args, **kwargs):
        herramientas = Project.objects.all()
        data = {
            'object_list': herramientas,
            'count': herramientas.count(),
            
        }
        pdf = render_to_pdf('portfolio\project-pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Create your views here.

class ProyectosListView(ListView):
    paginate_by = 6

    ordering = 'likes'   
    def get_queryset(self): 
        palabra_clave= self.request.GET.get("Kword",'')
        lista= Project.objects.filter(
            title__icontains=palabra_clave, 
        )
    
        return lista


class  DetalleDetailView(DetailView):
    model = Project
   
@method_decorator(staff_member_required, name='dispatch') 
class ProyectosCreateView(CreateView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')
    form_class = ProyectoForm

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosUpdateView( UpdateView):
    model = Project
    form_class = ProyectoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('portfolio:update', args=[self.kwargs['pk']]) +'?ok'

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')




#------------------Discapacidasd-----------------------------------------#
@method_decorator(staff_member_required, name='dispatch') 
class SubcategoriaCreateView(CreateView):
    model = SubCategory
    success_url = reverse_lazy('portfolio:proyectos')
    form_class = SubCategoryForm

class CategoryListView(ListView):
    model =  SubCategory
    template_name = 'portfolio\subcategory_list.html'

class  DetalleCatelView(DetailView):
    model = SubCategory
 

@method_decorator(staff_member_required, name='dispatch') 
class CategoryUpdateView( UpdateView):
    model = Category
    form_class = SubCategoryForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('portfolio:updatecategoria', args=[self.kwargs['pk']]) +'?ok'

@method_decorator(staff_member_required, name='dispatch') 
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('portfolio:subcategory_list.html') 

class AddLike(ListView):
    def post(self, request, pk, *args, **kwargs):
        post = Project.objects.get(pk=pk)
    
        
          
        is_dislike = False
        
        for dislikes in post.dislikes.all():
            if dislikes == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_likes = False
        for likes in post.likes.all():
            if likes == request.user:
                is_likes = True
                break
        
        if not is_likes:
            post.likes.add(request.user)

        if is_likes:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
      
    

class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Project.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)