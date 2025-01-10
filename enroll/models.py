from django.db import models
class user(models.Model):
    class Meta:
        db_table = 'student'
        
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
# Create your models here.
