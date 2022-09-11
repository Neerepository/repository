from multiprocessing import managers
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from registration.models import Profile
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
   
        
class ProyectosListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

    def get_queryset(self): 
        palabra_clave= self.request.GET.get("Kword",'')
        lista= Profile.objects.filter(
            user__icontains=palabra_clave, 
        )
        return lista   
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'


    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
