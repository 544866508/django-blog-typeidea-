from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    STATUS_NOMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NOMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    href = models.URLField(verbose_name="链接")   # 默认长度为200
    status = models.PositiveIntegerField(default=STATUS_NOMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    weight = models.PositiveIntegerField(default=1,
                                         choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重",
                                         help_text="权重高展示顺序靠前")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    DISPLAY_HTML = 1
    DISPLAY_LATEST_POST = 2
    DISPLAY_HOT_POST = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = (
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST_POST, '最新文章'),
        (DISPLAY_HOT_POST, '最热文章'),
        (DISPLAY_COMMENT, '最近评论'),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=DISPLAY_HTML,
                                               choices=SIDE_TYPE,
                                               verbose_name="展示类型")
    content = models.TextField(max_length=500, blank=True, verbose_name="内容",
                               help_text="如果设置的不是HTML类型，可为空")
    status = models.PositiveIntegerField(default=STATUS_SHOW,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

