from django.db import models
from uuid import uuid4

# Criação do modele de API


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    release_year = models.DateField(unique_for_year=True)
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
