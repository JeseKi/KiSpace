from django.urls import path , include
from .views import CPUListCreateView, GPUListCreateView

urlpatterns = [
    path('cpus/', CPUListCreateView.as_view(), name='cpu-list-create'),
    path('gpus/', GPUListCreateView.as_view(), name='gpu-list-create'),
]
