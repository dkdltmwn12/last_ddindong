from django import forms
from .models import Duser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디", error_messages={'required':"아이디를 입력하세요"})
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput, error_messages={'required':"비밀번호를 입력하세요"})

    def clean(self):
        clean_data = super().clean()

        username = clean_data.get('username')
        password = clean_data.get('password')

        if username and password :
            finish = Duser.objects.get(username=username)

            if not check_password(password, finish.password) :
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else :
                self.user_id = finish.id    