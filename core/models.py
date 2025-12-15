from django.db import models
from cloudinary.models import CloudinaryField
import tinify
from django.core.files.base import ContentFile
import requests

tinify.key = "TA_CLE_API_TINIFY"

class MembreEquipe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='equipe/', blank=True, null=True)
    #photo = CloudinaryField('image', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # def compress_image(self):
    #     if self.photo and hasattr(self.photo, 'file'):
    #         try:
    #             # Lire le fichier uploadé AVANT Cloudinary
    #             original = self.photo.file.read()

    #             # Compression Tinify
    #             source = tinify.from_buffer(original)
    #             compressed = source.to_buffer()

    #             # Remplacer le fichier par la version compressée
    #             self.photo.save(self.photo.name, ContentFile(compressed), save=False)

    #             print("✅ Image compressée avec Tinify")

    #         except Exception as e:
    #             print("❌ Erreur Tinify :", e)

    # def save(self, *args, **kwargs):
    #     # Si nouvelle image → compresser avant upload Cloudinary
    #     if self.pk is None or 'photo' in self.__dict__:
    #         self.compress_image()

    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Équipe"
        ordering = ['-nom']

    def __str__(self):
        return self.nom


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    categorie = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    #image = CloudinaryField('image', blank=True, null=True)
    lien_demo = models.URLField(blank=True, null=True)
    lien_github = models.URLField(blank=True, null=True)
    date_publication = models.DateField(auto_now_add=True)

    # def compress_image(self):
    #     if self.image and hasattr(self.image, 'file'):
    #         try:
    #             original = self.image.file.read()
    #             source = tinify.from_buffer(original)
    #             compressed = source.to_buffer()
    #             self.image.save(self.image.name, ContentFile(compressed), save=False)
    #             print("✅ Image projet compressée avec Tinify")
    #         except Exception as e:
    #             print("❌ Erreur Tinify :", e)

    # def save(self, *args, **kwargs):
    #     if self.pk is None or 'image' in self.__dict__:
    #         self.compress_image()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre
