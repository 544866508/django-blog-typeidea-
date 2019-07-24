from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.adminforms import PostAdminForm
from typeidea.BaseOwnerAdmin import BaseOwnerAdmin
from .models import Post, Category, Tag


# 自定义过滤器只展示用户当前分类
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # list_page
    def post_count(self, obj):  # custom_display
        return obj.post_set.count()
    post_count.short_description = '文章数量'
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')

    # edit_page
    fields = ('name', 'status', 'is_nav')


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    # list_page
    list_display = ('name', 'status', 'created_time')
    # edit_page
    fields = ('name', 'status')


@admin.register(Post)
class PostAdmin(BaseOwnerAdmin):
    # list_page
    list_display = ('title', 'category', 'status', 'created_time', 'operator')
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']
    actions_on_top = True
    actions_on_bottom = True
    # edit_page
    form = PostAdminForm
    save_on_top = True
    # fields = (
    #     ('category', 'title'), 'desc', 'status', 'content', 'tag',
    # )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag',),
        })
    )
    # 多对多字段可用的前端样式，直观好用一些
    filter_horizontal = ('tag',)

    # custom_part
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id, ))
        )
    operator.short_description = '操作'

