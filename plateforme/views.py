from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Count

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils import timezone

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
#from .forms import EvenementForm
import re
from django.db.models import Q
from django.template.loader import render_to_string

from .models import Client
from .forms import ClientForm

from django.forms import ModelForm

from django.contrib.auth.models import User

from django.contrib import messages

from .filters import ClientFilter

from xhtml2pdf import pisa

from django.template.loader import get_template

from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        template = get_template('plateforme/invoice.html')

        client = {
            'clients': clients
        }

        html = template.render(client)
        pdf = render_to_pdf('plateforme/invoice.html', client)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "liste_%s.pdf" %("")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {'today': datetime.date.today(), 'amount': 39.99, 'customer_name': 'Cooper Mann', 'order_id': 1233434, }
        pdf = render_to_pdf('plateforme/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def accueil(request):
    return render(request, 'plateforme/accueil.html', {})


def client_list(request):
    clients = Client.objects.all()
    success_url = reverse_lazy('plateforme:client_list')
    return render(request, 'plateforme/client_list.html', { 'clients': clients })

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plateforme:client_list')
    else:
        form = ClientForm()
    return render(request, 'plateforme/client_create.html', {
        'form': form
    })


#def client_update(request, pk, **kwargs):
    #client = get_object_or_404(Client, pk=pk)
    #if request.method == 'POST':
        #form = ClientForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
            #return redirect('plateforme:client_list')
    #else:
        #form = ClientForm()
    #return render(request, 'plateforme/client_create.html', {
        #'form': form
    #})


class UpdateClientView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'plateforme/client_create.html'

    def get_success_url(self):
        return reverse('plateforme:client_list')

    def get_context_data(self, **kwargs):

        context = super(UpdateClientView, self).get_context_data(**kwargs)
        context['action'] = reverse('plateforme:client_update', kwargs={'pk':self.get_object().id})
        return context


def client_detail(request, pk):
        client = get_object_or_404(Client, pk=pk)
        #success_url = reverse_lazy('plateforme:client_list')
        return render(request, 'plateforme/client_detail.html', {'client': client, })


def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    clients = Client.objects.all()
    return render(request, 'plateforme/client_list.html', {'clients': clients})


def search(request):
    client_list = Client.objects.all()
    client_filter = ClientFilter(request.GET, queryset=client_list)
    return render(request, 'plateforme/client_search.html', {'filter': client_filter})
