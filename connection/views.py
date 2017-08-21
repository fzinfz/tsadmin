from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PageNumberPaginationDataOnly(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)


from django.views.generic import ListView, DetailView
from .models import *

class PostPublicListView(ListView):
    model = Post
    paginate_by = 10
    template_name ='index.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(status__iexact='PUBLISHED', public=True)
        return queryset

class PostDetailView(DetailView):
    model = Post
