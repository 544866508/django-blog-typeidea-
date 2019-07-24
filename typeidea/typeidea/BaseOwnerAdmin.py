from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner', )

    # 过滤后台数据，让用户只能看到自己的文章
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    # 自动保存owner为当前用户
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)