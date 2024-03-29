from django.db import models

# Create your models here.

class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=245)
    description = models.TextField()
    image = models.ImageField(upload_to='image_cat',)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class SousCategorie(models.Model):
    """Model definition for SousCategorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=245)
    image = models.ImageField(upload_to='image_sous',)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for SousCategorie."""

        verbose_name = 'SousCategorie'
        verbose_name_plural = 'SousCategories'

    def __str__(self):
        """Unicode representation of SousCategorie."""
        return self.nom


class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom

class Produit(models.Model):

    titre = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='tag')
    image = models.ImageField(upload_to='image_produit')
    sous_cat = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, related_name='sous_cat')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'produit'
        verbose_name_plural = 'produits'
        
    def __str__(self):
        return self.titre
