from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def main_page(request):
    mainpage = MainPage.objects.last()
    ser = MainPageSerializer(mainpage)
    return Response(ser.data)


@api_view(['GET'])
def about_items(request):
    about_item = AboutItems.objects.all().order_by('id')[:4]
    ser = AboutItemsSerializer(about_item, many=True)
    return Response(ser.data)


@api_view(['GET'])
def about(request):
    about_us = About.objects.last()
    ser = AboutSerializer(about_us)
    return Response(ser.data)


@api_view(['GET'])
def direction_items(request):
    courses = DirectionItems.objects.all().order_by('id')[:5]
    ser = DirectionItemsSerializer(courses, many=True)
    return Response(ser.data)


@api_view(['GET'])
def direction(request):
    direction = Direction.objects.last()
    ser = DirectionSerializer(direction)
    return Response(ser.data)


@api_view(['GET'])
def task_items(request):
    task = TaskItems.objects.all().order_by('-id')[:10]
    ser = TaskItemsSerializer(task, many=True)
    return Response(ser.data)


@api_view(['GET'])
def tasks(request):
    task = Tasks.objects.last()
    ser = TasksSerializer(task)
    return Response(ser.data)


@api_view(['GET'])
def results_items(request):
    result = ResultItems.objects.all().order_by('-id')[:5]
    ser = ResultItemsSerializer(result, many=True)
    return Response(ser.data)


@api_view(['GET'])
def result(request):
    results = Results.objects.last()
    ser = ResultsSerializer(results)
    return Response(ser.data)


@api_view(['GET'])
def info(request):
    contact = Info.objects.last()
    ser = InfoSerializer(contact)
    return Response(ser.data)


@api_view(['POST'])
def register(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    birth = request.POST.get('birth')
    email = request.POST.get('email')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    registration = Register.objects.create(name=name, surname=surname, birth=birth, email=email, address=address, phone=phone)
    registration.save()
    return Response('successfully submitted!')


@api_view(['GET'])
def register_tab(request):
    tab = RegistrationTab.objects.last()
    return redirect(direction_items)

