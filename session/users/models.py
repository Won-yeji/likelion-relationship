from django.db import models
from django.contrib.auth.models import User

# TODO: Profile 모델 생성
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  nickname = models.CharField(max_length=20, null=True)
  image = models.ImageField(upload_to='profile/', null=True)

  class Meta:
    db_table = 'profile'

  def __str__(self):
    return self.nickname