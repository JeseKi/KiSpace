from .models import Portfolio
from .serializers import PortfolioSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def create(self, request, *args, **kwargs):
        # 获取真实 IP 地址
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # 如果 IP 地址不是 127.0.0.1，则返回一个禁止响应
        if ip != '127.0.0.1':
            return Response({"detail": "You are not allowed to POST from this IP."},
                            status=status.HTTP_403_FORBIDDEN)

        # 如果 IP 地址是 127.0.0.1，则继续常规的 POST 处理逻辑
        return super(PortfolioViewSet, self).create(request, *args, **kwargs)
