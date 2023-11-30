from django.db import models

class Portfolio(models.Model):
    # 1. 简介
    introduction = models.TextField(help_text="对作品的简要介绍")
    # 2. 标题
    title = models.CharField(max_length=100, help_text="作品的标题")
    # 4. 跳转链接
    redirect_link = models.CharField(
        max_length=255,  # 根据你的需要选择合适的最大长度
        help_text="用于内部导航到作品详细页面的链接",
    ) 
    # 5. 图片
    image = models.FileField(upload_to='media/portfolio_images/', help_text="作品的展示图片或图标")

    # 反色展示图片
    inverted_image = models.FileField(upload_to='media/portfolio_images_inverted/', help_text="作品的反色展示图片")    

    # 6. 是否为精选作品

    is_featured = models.BooleanField(default=False, help_text="是否为精选作品")
    def __str__(self):
        return self.title
    
# 创建一个新的模型用于存储反色图片


# 创建一个新的模型用于存储外部链接
class ExternalLink(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='external_links', on_delete=models.CASCADE)  # 关联到Portfolio模型
    url = models.URLField()  # 存储外部链接
    description = models.CharField(max_length=100)  # 链接的描述，如"GitHub", "哔哩哔哩"
    def __str__(self):
        return self.description
    
