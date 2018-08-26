from django import forms
from pace.models import Activity, Session
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(UserCreationForm):
    class Meta:
        model= get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['username'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'username'})
        self.fields['email'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'email'})
        self.fields['password1'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'confirm password'})

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'username'})
        self.fields['password'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'password'})

class AddActivityForm(forms.ModelForm):
    class Meta:
        fields = ("name", "hours", "minutes")
        model = Activity

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of Activity'
        self.fields['hours'].label = 'Number of Hours'
        self.fields['hours'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'duration'})
        self.fields['minutes'].label = 'Number of Minutes'
        self.fields['minutes'].widget.attrs.update(
          {'class' : 'form-control input-field', 'placeholder': 'duration'})

class AddSessionForm(forms.ModelForm):
    class Meta:
        fields = ("date",)
        model = Session
        widgets = {
          'date': DateInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)