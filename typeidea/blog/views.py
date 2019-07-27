from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from config.models import SideBar
from .models import Tag, Post, Category


class BaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.objects.filter(status=SideBar.STATUS_SHOW),
        })
        context.update(Category.get_navcate_and_nomalcate())
        return context


class IndexView(BaseView, ListView):
    queryset = Post.objects.filter(status=Post.STATUS_NOMAL).select_related('owner', 'category').prefetch_related('tag')
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(BaseView, DetailView):
    queryset = Post.objects.filter(status=Post.STATUS_NOMAL).select_related('owner', 'category').prefetch_related('tag')
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#     if tag_id:
#         tag = get_object_or_404(Tag, pk=tag_id)
#         post_list = tag.post_set.filter(status=Post.STATUS_NOMAL).select_related('owner', 'category').prefetch_related('tag')
#     elif category_id:
#         category = get_object_or_404(Category, pk=category_id)
#         post_list = category.post_set.filter(status=Post.STATUS_NOMAL).select_related('owner', 'category').prefetch_related('tag')
#     else:
#         post_list = Post.objects.filter(status=Post.STATUS_NOMAL).select_related('owner', 'category').prefetch_related('tag')
#     context = {
#         'tag': tag,
#         'category': category,
#         'post_list': post_list,
#         'sidebars': SideBar.objects.filter(status=SideBar.STATUS_SHOW)
#     }
#     context.update(Category.get_navcate_and_nomalcate())
#     return render(request, 'blog/list.html', context)


# def post_detail(request, post_id=None):
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'post': post,
#     }
#     context.update(Category.get_navcate_and_nomalcate())
#     return render(request, 'blog/detail.html', context)


