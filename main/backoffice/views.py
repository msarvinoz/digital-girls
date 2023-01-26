from calendar import calendar
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from main.models import *
from django.contrib import messages
from main.serializer import RegisterSerializer
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth
import calendar


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'sign-in.html')


def logout_view(request, pk):
    logout(request)
    return redirect('sign-in')


def home_view(request):
    today = datetime.now() - timedelta(days=1)
    month = datetime.today() - timedelta(days=30)
    day = Register.objects.filter(created__gte=today).count()
    months = Register.objects.filter(created__gte=month).count()
    qs = Register.objects.filter(
        created__gte=month
    ).annotate(
        day=ExtractDay("created"),
        mon=ExtractMonth('created'),
    ).values(
        'day', 'mon'
    ).annotate(
        n=Count('pk')
    ).order_by('mon')
    mon_list = []
    for i in qs:
        i['mon'] = (calendar.month_abbr[i['mon']])
        if len(mon_list) >= 30:
            del mon_list[0]
            mon_list.append(i)
        else:
            mon_list.append(i)
    print(len(mon_list))
    application = Register.objects.all().order_by('-id')
    course = DirectionItems.objects.all().order_by('-id')
    task = TaskItems.objects.all().order_by('-id')
    context = {
        'application': PagenatorPage(application, 2, request),
        'application_list': application,
        'course': PagenatorPage(course, 3, request),
        'task': PagenatorPage(task, 2, request),
        'register_count': Register.objects.all().count(),
        'direction_list': DirectionItems.objects.all(),
        'direction_count': DirectionItems.objects.all().count(),
        'task_list': TaskItems.objects.all(),
        'task_count': TaskItems.objects.all().count(),
        'day': day,
        'month': months,
        "qs": mon_list,
    }

    return render(request, 'dashboard-default.html', context)


global s
def search_applicants(request):
    query = request.GET.get('query', None)
    if query is not None:
        s = Register.objects.filter(name__icontains=query)
        print(323)
        return render(request, 'search-applicant.html', context={'s':s})
    return render(request, 'search-applicant.html')


def direction_title(request):
    titles = Direction.objects.all()
    s_list = []
    for i in titles:
        s_list.append(i)
    context = {
        "titles": titles,
        "active_titles": Direction.objects.last(),
        's_num': len(s_list)
    }
    return render(request, 'direction-title.html', context)


def create_direction_title(request):
    if request.method == "POST":
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        Direction.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
        )
        return redirect("direction-title")
    return redirect("direction-title")


def update_direction_title(request, pk):
    title = Direction.objects.get(pk=pk)
    context = {
        'title': title
    }
    if request.method == "POST":
        title = Direction.objects.get(pk=pk)
        title_ru = request.POST["title_ru"]
        title_uz = request.POST["title_uz"]
        title.title_ru = title_ru
        title.title_uz = title_uz
        title.save()
        return redirect("direction-title")
    return render(request, 'update-direction-title.html', context)


def direction_courses(request):
    course = DirectionItems.objects.all().order_by('-id')
    context = {
        'courses': DirectionItems.objects.all().order_by('-id'),
        'course': PagenatorPage(course, 3, request),
    }
    return render(request, 'direction.html', context)


def banner_view(request):
    banner = MainPage.objects.all()
    s_list = []
    for i in banner:
        s_list.append(i)
    context = {
        "banner": MainPage.objects.all().order_by('-id'),
        'active': MainPage.objects.last(),
        's_num': len(s_list),
    }
    return render(request, 'banner.html', context)


def create_direction(request):
    if request.method == "POST":
        directions_ru = request.POST.get("directions_ru")
        directions_uz = request.POST.get("directions_uz")
        image = request.FILES["image"]
        if directions_ru and directions_uz is not None:
            messages.success(request, 'successfully created!')
        else:
            messages.error(request, 'can not create!')
        direction = DirectionItems.objects.create(
            directions_ru=directions_ru,
            directions_uz=directions_uz,
            image=image,
        )
        direction.save()
        return redirect('direction-courses')
    return redirect('direction-courses')


def update_direction(request, pk):
    courses = DirectionItems.objects.get(pk=pk)
    context = {
        'course': courses
    }
    if request.method == "POST":
        course = DirectionItems.objects.get(pk=pk)
        directions_ru = request.POST["directions_ru"]
        directions_uz = request.POST["directions_uz"]
        image = request.FILES.get('image')
        course.directions_ru = directions_ru
        course.directions_uz = directions_uz
        if image is not None:
            course.image = image
        if directions_ru and directions_uz is not None:
            messages.success(request, 'successfully created!')
            course.save()
        else:
            messages.error(request, 'can not create!')
        return redirect("direction-courses")
    return render(request, 'update-direction.html', context)


def delete_direction(request, pk):
    direction = DirectionItems.objects.get(pk=pk).delete()
    return redirect('banner')


def create_banner_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES["image"]
        text_uz = request.POST.get("text_uz")
        text_ru = request.POST.get("text_ru")
        MainPage.objects.create(
            title=title,
            image=image,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("banner")
    return redirect("banner")


def delete_banner(request, pk):
    banner = MainPage.objects.get(pk=pk).delete()
    context = {
        'item': MainPage.objects.all()
    }
    return redirect('banner')


def about_view(request):
    context = {
        'about_title': About.objects.all(),
        'active_items': About.objects.filter(is_active=True)
    }
    return render(request, 'about-title.html', context)


def create_about_title(request):
    if request.method == "POST":
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        is_active = request.POST.get("is_active")
        a = About.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
            is_active=0
        )
        return redirect("about-title")
    return redirect('about-title')


def update_about_title(request, pk):
    item = About.objects.get(pk=pk)
    context = {
        'about_title': About.objects.all()
    }
    if request.method == "POST":
        item = About.objects.get(pk=pk)
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        is_active = request.POST.get("is_active")
        item.title_ru = title_ru
        item.title_uz = title_uz
        if is_active == 'on':
            is_active = True
        else:
            is_active = False
        if title_ru and title_uz is not None:
            item.save()
        return redirect("about-title")
    return render(request, 'update-about-tit.html', context)


def delete_about_title(request, pk):
    about = About.objects.get(pk=pk).delete()
    context = {
        'item': About.objects.all()
    }
    return redirect('about-title')


def about_project(request):
    project = AboutItems.objects.all().order_by('-id')[4:]
    active = AboutItems.objects.all().order_by('-id')[:4]
    context = {
        'project1': PagenatorPage(project, 2, request),
        'project': project,
        'active1': PagenatorPage(active, 2, request),
        'active': active
    }
    return render(request, 'about-project.html', context)


def create_about_item(request):
    if request.method == "POST":
        text_ru = request.POST.get("text_ru")
        text_uz = request.POST.get("text_uz")
        if 'image' in request.FILES:
            image = request.FILES["image"]
        AboutItems.objects.create(
            text_ru=text_ru,
            text_uz=text_uz,
            image=image
        )
        return redirect("about-project")
    return redirect('about-project')


def update_banner_view(request, pk):
    item = MainPage.objects.get(pk=pk)
    context = {
        'banner': item
    }
    if request.method == "POST":
        item = MainPage.objects.get(pk=pk)
        title = request.POST["title"]
        image = request.FILES.get('image')
        text_uz = request.POST["text_uz"]
        text_ru = request.POST["text_ru"]
        item.title = title
        item.text_ru = text_ru
        item.text_uz = text_uz
        if image is not None:
            item.image = image
        item.save()
        return redirect("banner")
    return render(request, 'update-banner.html', context)


def update_about_items(request, pk):
    items = AboutItems.objects.get(pk=pk)
    context = {
        'item': items
    }
    if request.method == "POST":
        item = AboutItems.objects.get(pk=pk)
        text_ru = request.POST["text_ru"]
        image = request.FILES.get("image")
        text_uz = request.POST["text_uz"]
        item.text_ru = text_ru
        item.text_uz = text_uz
        if image is not None:
            item.image = image
        item.save()
        return redirect("about-project")
    return render(request, 'update-about-item.html', context)


def delete_about_item(request, pk):
    about = AboutItems.objects.get(pk=pk).delete()
    return redirect('about-project')


def about_title_view(request):
    titles = About.objects.filter(is_active=True).order_by('-id')
    s_list = []
    for i in titles:
        s_list.append(i)
    context = {
        "titles": About.objects.all().order_by('-id'),
        "active_titles": About.objects.filter(is_active=True).order_by('-id'),
        's_num': len(s_list),
    }
    return render(request, 'about-title.html', context)


def modal_about(request, pk):
    if request.method == "POST":
        modal_1 = request.POST["modal_id"]
        modal_project = About.objects.get(id=modal_1)
        project = About.objects.get(id=pk)
        project.is_active = True
        project.save()
        modal_project.is_active = False
        modal_project.save()
    return redirect('about-title')


def info_view(request):
    info = Info.objects.all()
    s_list = []
    for i in info:
        s_list.append(i)
    context = {
        'information': Info.objects.last(),
        's_num': len(s_list),
    }
    return render(request, 'info.html', context)


def create_info(request):
    if request.method == "POST":
        title_ru = request.POST["title_ru"]
        title_uz = request.POST["title_uz"]
        website = request.POST["website"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        address_ru = request.POST["address_ru"]
        address_uz = request.POST["address_uz"]
        map = request.POST["map"]
        logo = request.FILES["logo"]
        instagram = request.POST["instagram"]
        telegram = request.POST["telegram"]
        you_tube = request.POST["you_tube"]
        facebook = request.POST["facebook"]
        a = Info.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
            website=website,
            phone=phone,
            email=email,
            address_ru=address_ru,
            address_uz=address_uz,
            map=map,
            logo=logo,
            instagram=instagram,
            telegram=telegram,
            you_tube=you_tube,
            facebook=facebook
        )
        a.save()
        return redirect("info")
    return redirect('info')


def all_info(request):
    context = {
        'information': Info.objects.last()
    }
    return render(request, 'all-info.html', context)


def update_info(request, pk):
    info = Info.objects.get(pk=pk)
    context = {
        'info': info
    }
    if request.method == "POST":
        website = request.POST["website"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        address_ru = request.POST["address_ru"]
        address_uz = request.POST["address_uz"]
        logo = request.FILES.get('logo')
        map = request.POST["map"]
        instagram = request.POST["instagram"]
        telegram = request.POST["telegram"]
        you_tube = request.POST["you_tube"]
        facebook = request.POST["facebook"]
        info.website = website
        info.phone = phone
        info.email = email
        info.address_ru = address_ru
        info.address_uz = address_uz
        if logo is not None:
            info.logo = logo
        info.map = map
        info.instagram = instagram
        info.telegram = telegram
        info.you_tube = you_tube
        info.facebook = facebook
        info.save()
        return redirect("info")
    return render(request, 'update-info.html', context)


def task_title(request):
    titles = Tasks.objects.all()
    s_list = []
    for i in titles:
        s_list.append(i)
    context = {
        "titles": titles,
        "active_titles": Tasks.objects.last(),
        's_num': len(s_list)
    }
    return render(request, 'task-title.html', context)


def create_task_title(request):
    if request.method == "POST":
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        Tasks.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
        )
        return redirect("task-title")
    return redirect("task-title")


def update_task_title(request, pk):
    title = Tasks.objects.get(pk=pk)
    context = {
        'titles': title
    }
    if request.method == "POST":
        item = Tasks.objects.get(pk=pk)
        title_ru = request.POST["title_ru"]
        title_uz = request.POST["title_uz"]
        item.title_ru = title_ru
        item.title_uz = title_uz
        item.save()
        return redirect("task-title")
    return render(request, 'update-task-title.html', context)


def tasks_view(request):
    task = TaskItems.objects.all().order_by('id')
    task_list = []
    for i in task:
        task_list.append(i)
    context = {
        'task': PagenatorPage(task, 2, request),
        'active_tasks': TaskItems.objects.all().order_by('id')[:10],
        'list_num': len(task_list),
    }
    return render(request, 'task.html', context)


def create_task(request):
    if request.method == 'POST':
        number = request.POST.get("number")
        requirements_ru = request.POST.get("requirements_ru")
        requirements_uz = request.POST.get("requirements_uz")
        t = TaskItems.objects.create(
            number=number,
            requirements_ru=requirements_ru,
            requirements_uz=requirements_uz
        )
        if requirements_ru and requirements_uz is not None:
            messages.success(request, 'successfully created!')
            t.save()
        else:
            messages.error(request, 'can not create!')
        return redirect("task-page")
    return redirect('task-page')


def update_tasks(request, pk):
    task = TaskItems.objects.get(pk=pk)
    context = {
        'items': task
    }
    if request.method == "POST":
        task = TaskItems.objects.get(pk=pk)
        requirements_ru = request.POST["requirements_ru"]
        requirements_uz = request.POST["requirements_uz"]
        task.requirements_ru = requirements_ru
        task.requirements_uz = requirements_uz
        task.save()
        return redirect("task-page")
    return render(request, 'update-task.html', context)


def delete_task(request, pk):
    task = TaskItems.objects.get(pk=pk).delete()
    return redirect('task-page')


def result_title(request):
    titles = Results.objects.all()
    s_list = []
    for i in titles:
        s_list.append(i)
    context = {
        "titles": titles,
        "active_titles": Results.objects.last(),
        's_num': len(s_list)
    }
    return render(request, 'result-title.html', context)


def create_result_title(request):
    if request.method == "POST":
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        text_ru = request.POST.get('text_ru')
        text_uz = request.POST.get('text_uz')
        Results.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
            text_ru=text_ru,
            text_uz=text_uz
        )
        return redirect("result-title")
    return redirect("result-title")


def update_result_title(request, pk):
    title = Results.objects.get(pk=pk)
    context = {
        'titles': title
    }
    if request.method == "POST":
        item = Results.objects.get(pk=pk)
        title_ru = request.POST["title_ru"]
        title_uz = request.POST["title_uz"]
        text_ru = request.POST["text_ru"]
        text_uz = request.POST["text_uz"]
        item.title_ru = title_ru
        item.title_uz = title_uz
        item.text_ru = text_ru
        item.text_uz = text_uz
        item.save()
        return redirect("result-title")
    return render(request, 'update-result-title.html', context)


def result_view(request):
    result = ResultItems.objects.all().order_by('-id')
    result_list = []
    for i in result:
        result_list.append(i)
    context = {
        'result': PagenatorPage(result_list, 2, request),
        'active_results': ResultItems.objects.all().order_by('-id')[:5],
        'list_num': len(result_list),
    }
    return render(request, 'result.html', context)


def create_result(request):
    if request.method == 'POST':
        title_ru = request.POST.get("title_ru")
        title_uz = request.POST.get("title_uz")
        image = request.FILES['image']
        result = ResultItems.objects.create(
            title_ru=title_ru,
            title_uz=title_uz,
            image=image
        )
        if title_ru and title_uz is not None:
            messages.success(request, 'successfully created!')
            result.save()
        else:
            messages.error(request, 'can not create!')
        return redirect("result-page")
    return redirect('result-page')


def update_result(request, pk):
    result = ResultItems.objects.get(pk=pk)
    context = {
        'items': result
    }
    if request.method == "POST":
        result = ResultItems.objects.get(pk=pk)
        title_ru = request.POST["title_ru"]
        title_uz = request.POST["title_uz"]
        image = request.FILES.get("image")
        result.title_ru = title_ru
        result.title_uz = title_uz
        if image is not None:
            result.image = image
        result.save()
        return redirect("result-page")
    return render(request, 'update-result.html', context)


def delete_result(request, pk):
    result = ResultItems.objects.get(pk=pk).delete()
    return redirect('result-page')


def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'user-detail.html', context)


def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image = request.FILES.get('image')
        email = request.POST['email']
        bio = request.POST['bio']
        user.username = username
        user.first_name = first_name
        if image is not None:
            user.image = image
        user.bio = bio
        user.last_name = last_name
        user.email = email
        if image is not None:
            user.image = image
        user.save()
        return redirect('user-detail', user.pk)
    context = {
        'user': user
    }
    return render(request, 'user-update.html', context)


def user_password_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        new_password = request.POST.get('new_password')
        password_confirm = request.POST.get('password_confirm')
        if new_password is not None:
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
            else:
                print('dont match')
        else:
            print(111)
        return redirect('user-detail', user.pk)
    return render(request, 'user-password-update.html')


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


@login_required(login_url='sign-in')
def approach_item_paginator(request):
    approach = DirectionItems.objects.all().order_by('-id')
    context = {
        'approach': PagenatorPage(approach, 2, request)
    }
    return render(request, 'direction.html', context)

