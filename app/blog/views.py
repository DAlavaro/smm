# app/blog/views.py
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from app.blog.forms import BlogForm
from app.blog.models import Blog


@method_decorator(cache_page(60 * 5), name='dispatch')
class BlogListView(ListView):
    model = Blog


@method_decorator(cache_page(60 * 5), name='dispatch')

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

    def get_object(self):
        """
            Увеличение счетчика просмотров
        """
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.add_blog'


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.change_blog'


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.delete_blog'



