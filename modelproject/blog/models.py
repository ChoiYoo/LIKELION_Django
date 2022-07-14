
from django.db import models
from account.models import CustomUser

# Create your models here.
class Blog(models.Model):
    TYPE_CHOICES = {
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Etc', 'Etc')
    }
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=200)
    time = models.DateTimeField()
    body = models.TextField('내용')
    image = models.ImageField('이미지 첨부', upload_to="blog/", blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=5, null=True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    content = models.CharField('', max_length=500)
    time = models.DateTimeField()

    def __str__(self):
        return self.content
