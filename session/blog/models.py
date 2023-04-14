from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def summary(self):
        return self.content[:100]
    

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'comment'
    
    def __str__(self):
        return self.content + ' | ' + str(self.author)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'like'
        unique_together = ('user', 'blog')

    def __str__(self):
        return self.blog.title + " | " + self.user.username

    def save(self, *args, **kwargs):
        self.like_count = Like.objects.filter(blog=self.blog).count()
        super(Like, self).save(*args, **kwargs)
