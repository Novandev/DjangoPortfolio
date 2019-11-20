from django.db import models



class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    asset_type = models.TextField(max_length=100)
    asset_id = models.TextField(max_length=100)