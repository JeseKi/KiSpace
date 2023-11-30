from rest_framework import generics, filters, status
from rest_framework.response import Response
from .models import CPU, GPU
from .serializers import CPUSerializer, GPUSerializer

class LocalOnlyCreateMixin:
    """
    一个 Mixin，用于确保只有本地 IP 地址可以进行 POST 请求。
    """
    def create(self, request, *args, **kwargs):
        # 获取真实 IP 地址
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        if ip != '127.0.0.1':
            return Response({"detail": "You are not allowed to POST from this IP."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class CPUListCreateView(LocalOnlyCreateMixin, generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class GPUListCreateView(LocalOnlyCreateMixin, generics.ListCreateAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
