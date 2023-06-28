from django.db import models

# Create your models here.

class Municipio(models.Model):
    """Model definition for Municipio."""
    municipio = models.CharField('Municipio', max_length=35)
    seccion = models.IntegerField()
    casilla = models.IntegerField()
    ln21 = models.IntegerField()
    

    class Meta:
        """Meta definition for Municipio."""

        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        """Unicode representation of Municipio."""
        return str(self.id)+'-'+self.municipio
    
  

class DipLocales(models.Model):
    cabecera = models.CharField('Municipio', max_length=35)
    partido = models.CharField('Municipio', max_length=150)
    siglas = models.CharField('Municipio', max_length=35)
    nombre = models.CharField('Municipio', max_length=200)
    mun = models.ManyToManyField(Municipio)
    
    class Meta:
        verbose_name = 'Diputado Local'
        verbose_name_plural = 'Diputados Locales'
        

class DipFederales(models.Model):
    cabecera = models.CharField('Municipio', max_length=35)
    nombre = models.CharField('Municipio', max_length=200)
    partido = models.CharField('Municipio', max_length=150)
    mun = models.ManyToManyField(Municipio)
    
    class Meta:
        verbose_name = 'Diputado Federal'
        verbose_name_plural = 'Diputados Federales'