from django.urls import path, include  # 导入Django的路径和包含模块
from rest_framework.routers import DefaultRouter  # 导入DRF的默认路由器
from . import views  # 导入你的视图

router = DefaultRouter()  # 创建一个默认路由器
router.register(r'portfolio', views.PortfolioViewSet)  # 注册你的Portfolio视图到路由器

urlpatterns = [
    path('portfolio/', include(router.urls)),  # 包含API的URL路径
]
