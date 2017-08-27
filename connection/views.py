from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPaginationDataOnly(PageNumberPagination):
    """
    This model is for api. It's placed here because DEFAULT_PAGINATION_CLASS can't be correctly loaded.
    """

    def get_paginated_response(self, data):
        return Response(data)


from django.views.generic import ListView, DetailView
from .models import Post, Node


class PostPublicListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(status__iexact='PUBLISHED', public=True, list=True)
        return queryset


class PostPublicDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(public=True)


from django.contrib.auth.mixins import LoginRequiredMixin


class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    paginate_by = 100
    template_name = 'profile.html'