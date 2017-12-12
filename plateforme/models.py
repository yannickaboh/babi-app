from django.db import models
from django.contrib.auth.models import User, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

# Create your models here.


class Client(models.Model):

	nom = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nom")
	prenom = models.CharField(max_length=255, blank=True, null=True, verbose_name="Prénom")
	sexe = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sexe")
	document = models.FileField(upload_to='photos/', null=True, verbose_name="Photo")
	date_naissance = models.DateField(blank=True, null=True, verbose_name="Date de Naissance")
	lieu_naissance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lieu")


	pere = models.CharField(max_length=255, blank=True, null=True, verbose_name="Noms et Prénoms du Père")
	mere = models.CharField(max_length=255, blank=True, null=True, verbose_name="Noms et Prénoms de la Mère")
	

	profession = models.CharField(max_length=255, blank=True, null=True, verbose_name="Profession")
	statut = models.CharField(max_length=255, blank=True, null=True, verbose_name="Statut Matrimonial")
	conjoint = models.CharField(max_length=255, blank=True, null=True, verbose_name="Noms et Prénoms conjoint(e)")
	nbre_enfants = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre d'enfants")


	pays_origine = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pays d'origine")
	ville_origine = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ville d'origine")
	ville_residence = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ville de Résidence")
	lieu_residence = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lieu de Résidence")
	nationalite = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nationalité")


	cni = models.CharField(max_length=255, blank=True, null=True, verbose_name="Num. CNI")
	cni_delivre_par = models.CharField(max_length=255, blank=True, null=True, verbose_name="Délivré Par")
	date_cni = models.DateField(blank=True, null=True, verbose_name="Date de Délivrance")

	passport = models.CharField(max_length=255, blank=True, null=True, verbose_name="Num. Passeport")
	passp_delivre_par = models.CharField(max_length=255, blank=True, null=True, verbose_name="Délivré Par")
	date_passp = models.DateField(blank=True, null=True, verbose_name="Date de Délivrance")


	
	date_arr_gab = models.DateField(blank=True, null=True, verbose_name="Date d'arrivée au GABON")
	uploaded_at = models.DateTimeField(auto_now_add=True)

	
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False)

	def __str__(self):
		return self.nom

	@property
	def documents_url(self):
		if self.document and hasattr(self.document, 'url'):
			return self.document.url
			
	class Meta:
		verbose_name_plural = 'Clients'
