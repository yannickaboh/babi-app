from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models
from plateforme import models
from django.conf import settings

# Register your models here.




class ClientAdmin(admin.ModelAdmin):
    list_display   = ('nom',
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
		'date_arr_gab', 'uploaded_at', 'ajoute_par',)
    list_filter    = ('nom',
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
		'date_arr_gab', 'uploaded_at', 'ajoute_par',)
    date_hierarchy = 'uploaded_at'
    ordering       = ('nom', )
    search_fields  = ('nom',
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
		'date_arr_gab', 'uploaded_at', 'ajoute_par', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'ajoute_par', None) is None:
            obj.ajoute_par = request.user
        obj.save()

admin.site.register(models.Client, ClientAdmin)
