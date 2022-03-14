import json
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .forms import SignForm, TodoForm, UserForm
from .models import Todo, User
from django.core.paginator import Paginator

# Create your views here.
@api_view(['GET'])
def index(request):
    todos = Todo.objects.all()
    
    context = {
        'todos': todos.__len__
    }
    return render(request, 'todo/index.html', context)

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

@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'GET':
        sign_form = SignForm
        context = {
            'signForm': sign_form
        }
        return render(request, 'todo/signin.html', context)
    else:
        error = '1'
        success = '1'
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user'] = {
                    'num': user.num,
                    'id': user.id,
                    'email': user.email,
                    'profile': str(user.profile),
                    'regdate': json.dumps(user.regdate, indent=4, sort_keys=True, default=str),
                }
                print(request.session['user'])
                return redirect('/?succ='+success)
            else:
                return redirect('/signin?error='+error)
        else:
            return redirect('/signin?error='+error)

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        user_form = UserForm
        context = {
            'userForm': user_form
        }
        return render(request, 'todo/signup.html', context)
    else:
        ids = request.POST['id']
        email = request.POST['email']
        password = request.POST['password']
        profile = request.FILES['profile']
        
        user = User(
            id=ids,
            email=email,
            password=password,
            profile=profile,
        )
        
        user.save()
        
        return redirect('index')

@api_view(['POST'])
def signout(request):
    request.session['user'] = None
    return redirect('index')

@api_view(['POST'])
def todo(request):
    title = request.POST['title']
    content = request.POST['content']
    author = request.POST['author']
    tags = request.POST['tags']
    start = request.POST['start']
    end = request.POST['end']
    
    todo = Todo(
        title = title,
        content = content,
        author = author,
        tags = tags,
        start = start,
        end = end,
    )
    
    todo.save()
    
    return redirect('index')

@api_view(['POST'])
def control(request, num):
    if request.POST['_method'] == 'put':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        tags = request.POST['tags']
        start = request.POST['start']
        end = request.POST['end']
        if Todo.objects.filter(num=num):
            todo = Todo.objects.get(num=num)
            
            todo.title = title
            todo.content = content
            todo.author = author
            todo.tags = tags
            todo.start = start
            todo.end = end
            
            todo.save()
    return redirect('index')

@api_view(['GET'])
def form(request):
    context = {
        'todoForm': TodoForm
    }
    return render(request, 'todo/form.html', context)

@api_view(['GET'])
def edit(request, num):
    if Todo.objects.filter(num=num):
        todo = Todo.objects.get(num=num)
        todoForm = TodoForm(instance=todo)
        context = {
            'todoForm': todoForm,
            'todo': todo
        }
    return render(request, 'todo/form.html', context)