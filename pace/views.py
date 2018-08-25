from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from pace.forms import UserCreateForm, UserLoginForm
from django.views.generic import (TemplateView, DetailView, FormView, ListView, CreateView, DeleteView, UpdateView)


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class LoginUserView(LoginView):
    template_name='login.html'
    form_class = UserLoginForm

class SignUpView(CreateView):
    context_object_name= 'user_create'
    success_url = reverse_lazy('pace:login')
    form_class = UserCreateForm
    template_name='sign_up.html'

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name='dashboard.html'

class SessionListView(ListView):
    template_name='session_list.html'c

class ProgressView(DetailView):
    template_name='session_list.html'