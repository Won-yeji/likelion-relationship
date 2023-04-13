from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)

    # TODO: author 추가
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # TODO: tag 추가
    tag = models.ManyToManyField('Tag', blank=True)
    

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]


# TODO: Comment 모델 추가
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content + ' | ' + str(self.author)


# TODO: Tag 모델 추가
class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name