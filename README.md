# django-login-board

django 연습 테스트

## 사용된 내용

import json  
datetimefield ==> json.dumps(session_user['regdate'], indent=4, sort_keys=True, default=str)

```python
# views.py
from django.core.paginator import Paginator
@api_view(['GET'])
def list(request):
    page = request.GET['page'] if 'page' in request.GET else 1
    
    todos = Todo.objects.order_by('regdate')
    
    paginator = Paginator(todos, 3)
    pages = paginator.get_page(page)
    
    context = {
        'todos': pages
    }
    return render(request, 'todo/list.html', context)

# models.py
ImageField ...  str(session_user['profile'])

# forms.py
class UserForm(ModelForm):
    email = forms.EmailField(required=False)
    # required 설정

    class Meta:
        model = User
        fields = [
            'email', 'password'
            ]
        widgets = {
            'password': PasswordInput(attrs={'type':'password'})
        }
    
    # cleaned_data 값 filter 작업 할 때
    def clean_mail(self):
        if '@' not in self.cleaned_data['email']:
            return ValidationError('이메일 형식이 아닙니다.')
        else: self.cleaned_data['email']

# model객체 dict로 변환
user = User(request.POST)
user.__dict__
```

valid 설정 중에서 ...

```html
{% extends './layout.html' %}
{% load bootstrap5 %}
{% block content %}
<h1>Sign in</h1>
<div>
    <form action="{% url 'signin' %}" method="post" novalidate>
        {% if request.GET.error %}
            <div class="alert alert-danger">
                아이디와 비밀번호를 확인해주세요
            </div>
        {% endif %}
        {% if signForm.errors %}
        <div class="alert alert-danger">
            {% for field in signForm %}
            {% if field.errors %}
            {{field.label}}
            {{field.errors}}
            {% endif %}
            {% endfor %}
        </div>
        {% endif %}
        <div>
            {% comment %} {% bootstrap_form signForm %} {% endcomment %}
            {{ signForm.as_p }}
        </div>
        <button type="submit" class="btn btn-info">sign in</button>
    </form>
</div>
{% endblock %}
```