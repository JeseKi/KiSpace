from rest_framework import serializers  # 导入DRF的serializers模块
from .models import Portfolio  # 导入你的Portfolio模型

class PortfolioSerializer(serializers.ModelSerializer):  # 创建一个继承自ModelSerializer的序列化器
    class Meta:
        model = Portfolio  # 指定要序列化的模型
        fields = '__all__'  # 指定要序列化的字段，这里选择所有字段
