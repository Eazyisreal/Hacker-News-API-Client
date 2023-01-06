# from django.db import models

# #News Model

# class News(models.Model):
#     item_id = models.PositiveIntegerField(unique=True)
#     item_type = models.CharField(max_length=50 )
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     url = models.URLField()
    
#     class meta:
#         verbose_name_plural = 'News'
#         ordering = ['item_id']
        
# def __str__(self):
#         return self.name        

from django.db import models
class News(models.Model):
        title = models.CharField(max_length=200)
        url = models.URLField()
        created_at = models.DateTimeField(auto_now_add=True, null=True)
        type = models.CharField(max_length=20, null=True)
        parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
        api_created = models.BooleanField(default=False)

        def __str__(self):
            return self.title
