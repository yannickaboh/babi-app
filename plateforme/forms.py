from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models
from plateforme import models
from django.conf import settings

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [

        'nom',
		'prenom',
		'sexe',
		'document',
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

        exclude = ['uploaded_at', 'ajoute_par', ]