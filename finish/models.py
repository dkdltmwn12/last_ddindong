from django.db import models

# Create your models here.

class Duser(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_dttm = models.DateField(auto_now_add=True, verbose_name='가입날짜')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_define_fuser_table'
        verbose_name = '띵동 사용자'
        verbose_name_plural = '띵동 사용자'