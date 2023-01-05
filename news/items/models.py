from django.db import models

#News Model

class News(models.Model):
    item_id = models.PositiveIntegerField(unique=True)
    item_type = models.CharField(max_length=50 )
    title = models.CharField(max_length=200)
    body = models.TextField()
    url = models.URLField()
    
    class meta:
        verbose_name_plural = 'News'
        ordering = ['item_id']
        
def __str__(self):
        return self.name        
