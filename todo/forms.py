from django.forms import DateInput, FileInput, ModelForm
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
    class Meta:
        model = User
        fields = [
            'email', 'password'
            ]