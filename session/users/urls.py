from django.urls import path
from .views import *


urlpatterns = [
    #TODO: 로그인, 회원가입, 로그아웃 url 추가
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
]