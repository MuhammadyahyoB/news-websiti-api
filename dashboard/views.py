from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db.models import Q


@login_required(login_url='dashboard:log_in')
def index(request):
    category = models.Category.objects.all().count()

    context = {
        'category' : category
    }
    return render(request, 'dashboard/index.html')


#>>>>>>>>> Category create list edit delete detail <<<<<<<<<<<<<


@login_required(login_url='dashboard:log_in')
def create_category(request):
    if request.method == 'POST':
        try:
          name = request.POST['name']
          models.Category.objects.create(
            name=name
         )
          messages.success(request, 'Categoriyalar muvafiqiyatli tugatildi')
        except:
          messages.error(request, 'Categoryalar yaratishda xatolik')
    return render(request, 'dashboard/category/create.html')


@login_required(login_url='dashboard:log_in')
def list_category(request):
    category = models.Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/detail.html', context)

@login_required(login_url='dashboard:log_in')
def edit_category(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        messages.success(request, 'Kategoriyasini  muvoffaqiyatli o`zgartirildi')
        return redirect('dashboard:category-detail', category.id)
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_category(request, id):
    models.Category.objects.get(id=id).delete()
    messages.success(request, 'Categorylar muvafiqiyatli o`chirildi')
    return redirect('dashboard:category-list')

    
# >>>>>>>>>>> registry log_in  log_out query <<<<<<<<<<<<


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            User.objects.create_user(
                username = username,
                password = password
            )
            user = authenticate(
            username = username, 
            password = password
            )
            if user:
                login(request, user)
                messages.success(request, 'Muvoffaqiyatli ro`yxatdan o`tdingiz')
                return redirect('dashboard:index')
            else:
                messages.success(request, 'Muvoffaqiyatsizlik qayta uring')
                return redirect('dashboard:register') 
                
    return render(request, 'dashboard/auth/register.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = User.objects.get(username=username)
        user = authenticate(
            username = username, 
            password = password
            )
        if user:
            login(request, user)
            messages.success(request, 'Muvoffaqiyatli tizimga kirdiz ')
            return redirect('dashboard:index')
        else:
            messages.success(request, 'Muvoffaqiyatsizlik qayta uring ')
            return redirect('dashboard:log_in')

    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')

def query(request):
    q = request.GET['q']
    category = models.Category.objects.filter(Q(name__icontains=q))

    context = {
        'category':category,
    }
    return render(request, 'dashboard/query.html', context)



#>>>>>>>>>Region list detail create edit <<<<<<<<<<<<<



def create_region(request):
    if request.method == 'POST':
        try:
          name = request.POST['name']
          models.Region.objects.create(
            name=name
         )
          messages.success(request, 'Regionalar muvafiqiyatli tugatildi')
        except:
          messages.error(request, 'Regionalar yaratishda xatolik')
    return render(request, 'dashboard/region/create.html')

def list_region(request):
    region = models.Region.objects.all()
    context = {
       'region':region
    }
    return render(request, 'dashboard/region/list.html', context)

def detail_region(request, id):
    region = models.Region.objects.get(id=id)
    context = {
       'region':region
    }
    return render(request, 'dashboard/region/detail.html', context)

def edit_region(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        messages.success(request, 'Regionlar muvafiqiyatli o`zgartirildi')
        return redirect('dashboard:region-detail', region.id)
    return render(request, 'dashboard/region/edit.html')
    
def delete_region(request, id):
    models.Region.objects.get(id=id).delete()
    messages.success(request, 'Regionlar muvafiqiyatli o`chirildi')
    return redirect('dashboard:region-list')





#>>>>>>>>>Post list detail list edit <<<<<<<<<<<


def create_post(request):
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    context = {
        'category':category,
         'region':region
    }
    if request.method == 'POST':
        try:
          title = request.POST['title']
          content = request.POST['content']
          category = request.POST['category']
          region = request.POST['region']
          models.Post.objects.create(
            title=title,
            content=content,
            category=category,
            region=region
         )
          messages.success(request, 'Postlar muvafiqiyatli tugatildi')
        except:
          messages.error(request, 'Postlar yaratishda xatolik')
    return render(request, 'dashboard/post/create.html', context)

def list_post(request):
    """post list"""
    post = models.Post.objects.all()
    context = {
       'post':post
    }
    return render(request, 'dashboard/post/list.html', context)

def detail_post(request, id):
    post = models.Post.objects.get(id=id)
    context = {
       'post':post
    }
    return render(request, 'dashboard/post/detail.html', context)

def edit_post(request, id):
    post = models.Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        post.region = request.POST['region']
        post.save()
        messages.success(request, 'Postlar muvafiqiyatli o`zgartirildi')
        return redirect('dashboard:post-detail', post.id)
    return render(request, 'dashboard/post/edit.html')

def delete_post(request, id):
    models.Post.objects.get(id=id).delete()
    messages.success(request, 'Postlar muvafiqiyatli o`chirildi')
    return redirect('dashboard:post-list')