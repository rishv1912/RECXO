from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timestamp = models.DateTimeField(blank=True)
    # image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.comment[0:13] + "..." + "by " + self.user.username