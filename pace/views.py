from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from pace.forms import UserCreateForm, UserLoginForm, AddActivityForm, AddSessionForm
from pace.models import Session, Activity
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
    model = Session
    template_name='session_list.html'

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user.id)

class ActivityListView(ListView):
    model = Activity
    template_name='activity_list.html'

   # def get_queryset(self):
    #    return Activity.objects.filter(session=self.session.id)

class ProgressView(DetailView):
    template_name='progress.html'

class AddActivityView(CreateView):
    model = Activity
    template_name='add_activity.html'
    form_class = AddActivityForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.session = Session.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

class AddSessionView(CreateView):
    model = Session
    template_name='add_session.html'
    form_class = AddSessionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

