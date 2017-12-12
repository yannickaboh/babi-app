from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views

from django.contrib.auth import views as auth_views

from plateforme import views

from .filters import ClientFilter
from django_filters.views import FilterView

from .views import GeneratePDF, ChartData, get_data, HomeView

from django.contrib.auth import views as auth_views

app_name = 'plateforme'


urlpatterns = [

    url(r'^inscription/$', accounts_views.signup, name='signup'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='mon_compte'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^$', auth_views.LoginView.as_view(template_name='plateforme/login.html'), name='login'),

    url(r'^client_list/pdf/$', GeneratePDF.as_view(), name='pdf_client_list'),

    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='charts'),
    url(r'^api/data/$', views.get_data, name='api-data'),





    url(r'^accueil/$', views.accueil, name='accueil'),
    url(r'^client_create/$', views.client_create, name='client_create'),
    url(r'^client_list/$', views.client_list, name='client_list'),
    url(r'^client_detail/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    #url(r'^client_update/(?P<pk>[0-9]+)/$', views.client_update, name='client_update'),
    url(r'^client/update/(?P<pk>[0-9]+)/$', views.UpdateClientView.as_view(), name='client_update'),
    url(r'^client_delete/(?P<pk>[0-9]+)/$', views.client_delete, name='client_delete'),
    url(r'^client_search/$', FilterView.as_view(filterset_class=ClientFilter, 
        template_name='plateforme/client_search.html'), name='client_search'),


    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$',views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),





    url(r'^admin/', admin.site.urls),

    # Add, Update, Delete Client URLS
    #url(r'^client_list/$', views.ClientList.as_view(), name='client_list'),
    #url(r'^client_create/$', views.client_create, name='client_create'),
    #url(r'^client_update/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='client_update'),
    #url(r'^client_delete/(?P<pk>\d+)/$', views.ClientDelete.as_view(), name='client_delete'),
    #url(r'^client_detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^client_search/$', FilterView.as_view(filterset_class=ClientFilter, 
        #template_name='plateforme/client_search.html'), name='client_search'),
]