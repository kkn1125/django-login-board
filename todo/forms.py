from django.forms import DateInput, FileInput, ModelForm, PasswordInput, ValidationError
from django import forms
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title', 'content', 'author', 'tags', 'start', 'end',# 'regdate', 'updates'
            ]
        widgets = {
            'start': DateInput(attrs={'type': 'date'}),
            'end': DateInput(attrs={'type': 'date'})
        }
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'password', 'profile'#, 'regdate','update'#, 'updates'
            ]
        widgets = {
            # 'profile': ImageInput(attrs={'type': 'file'})
        }
        
class SignForm(ModelForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = [
            'email', 'password'
            ]
        widgets = {
            'password': PasswordInput(attrs={'type':'password'})
        }
    
    def clean_mail(self):
        if '@' not in self.cleaned_data['email']:
            return ValidationError('이메일 형식이 아닙니다.')
        else: self.cleaned_data['email']