from django.contrib.auth.models import User
import django_filters
from .models import Client
from django import forms


class ClientFilter(django_filters.FilterSet):
	nom = django_filters.CharFilter(lookup_expr='icontains')
	prenom = django_filters.CharFilter(lookup_expr='icontains')
	sexe = django_filters.CharFilter(lookup_expr='icontains')
	lieu_naissance = django_filters.CharFilter(lookup_expr='icontains')


	class Meta:
		model = Client
		fields = [

        'nom',
		'prenom',
		'sexe',
		'date_naissance',
		'lieu_naissance',
		'pere',
		'mere',
		'profession',
		'statut',
		'conjoint',
		'nbre_enfants',
		'pays_origine',
		'ville_origine',
		'ville_residence',
		'lieu_residence',
		'nationalite',
		'cni',
		'cni_delivre_par',
		'date_cni',
		'passport',
		'passp_delivre_par',
		'date_passp',
		'date_arr_gab',



        ]





