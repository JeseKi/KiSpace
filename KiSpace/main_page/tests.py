from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse
from django.conf import settings
import os

def check_image(request, image_path):
    # 拼接图片的完整路径
    full_path = os.path.join(settings.MEDIA_ROOT, image_path)
    
    # 检查文件是否存在
    if os.path.exists(full_path):
        return HttpResponse(f"The image exists at: {full_path}")
    else:
        return HttpResponse(f"The image does not exist at: {full_path}")
