from rest_framework import viewsets
from books.api.serializer import BooksSerializer
from books.models import Books


class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all
