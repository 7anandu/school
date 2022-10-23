from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils.safestring import mark_safe

from sapp.form import PersonCreationForm
from sapp.models import Course, Person


def index(request):
    return render(request, 'base.html')
def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        cpw = request.POST['password1']

        if pw == cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request, 'username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=pw)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password mismatch')

    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return render(request,'button.html')
        else:
            messages.info(request, 'Invalid user')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def button(request):
    return render(request,'button.html')

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, mark_safe("ordered" Click<a href='/'>Here </a> to go to home))

            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})

def Save(request,):
    form1 = Person.objects.all()
    return render(request,'save.html',{'form1':form1})

# AJAX
def load_branches(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)