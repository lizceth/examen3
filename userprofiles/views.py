from django.shortcuts import redirect, render
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from userprofiles.forms import ProfileForm
from userprofiles.models import Profile
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import  TemplateView, FormView, View
from .forms import ProfileForm

from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

@method_decorator(permission_required('userprofiles.list'))
def listar(request):
    profiles = User.objects.all()
    return render(request, 'userprofiles/index.html', {'profiles':profiles})

class List(ListView):
    model=Profile


def detail(request, id_user):
    profile=get_object_or_404(Profile, id=id_user)
    return render_to_response('userprofiles/detail.html',{'profile':profile},
                              context_instance=RequestContext(request))
class Create(FormView):
	template_name = 'registrarse.html'
	form_class = ProfileForm
	success_url = reverse_lazy('new')

	def form_valid(self,form):
		user = form.save()
		perfil=Profile()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.documento = form.cleaned_data['documento']
		perfil.numero_doc = form.cleaned_data['numero_doc']
		perfil.departamento = form.cleaned_data['departamento']
		perfil.provincia = form.cleaned_data['provincia']
		perfil.distrito= form.cleaned_data['distrito']
		perfil.zona_horaria= form.cleaned_data['zona_horaria']
		perfil.save()
		return super(registrarse, self).form_valid(form)

def nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('userprofiles/nuevo_usuario.html',
                              {'formulario':formulario}, context_instance=RequestContext(request))

@method_decorator(permission_required('userprofile.update'))
def update(request, id):
    editar=Profile.objects.get(pk=id)
    if request.method=='POST':
        formulario = ProfileForm(request.POST, instance=editar)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/detail/')
    else:
        formulario = ProfileForm(instance=editar)
    return render_to_response('userprofiles/editar.html',
                              {'formulario':formulario}, context_instance=RequestContext(request))

class Delete(DeleteView):
    model = Profile
    @method_decorator(permission_required('userprofiles.delete'))
    def dispatch(self, *args, **kwargs):
        return super(Delete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse('list')


@method_decorator(permission_required('userprofile.delete'))
def borrar(request, id):
    borrar=get_object_or_404(Profile, pk=id)
    borrar.delete()
    return HttpResponseRedirect ("/detail/")

@login_required(login_url='/login')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
