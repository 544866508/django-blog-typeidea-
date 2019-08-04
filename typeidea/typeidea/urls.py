"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView
from config.views import links
from user.views import register, login, logout, login_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', IndexView.as_view(), name='home_page'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category_post'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag_post'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('links/', links, name='link'),
    path('search/', SearchView.as_view(), name='search'),

    # 异步提交检查
    path('login_check/', login_check, name='login_check')
]
