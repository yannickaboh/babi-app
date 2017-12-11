from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignUpForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('plateforme:accueil')
    else:
        form = SignUpForm()
    return render(request, 'plateforme/signup.html', {'form': form})


#@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'plateforme/mon_compte.html'
    success_url = reverse_lazy('plateforme:mon_compte')

    def get_object(self):
        return self.request.user