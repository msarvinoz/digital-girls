from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def main_page(request):
    try:
        mainpage = MainPage.objects.last()
        ser = MainPageSerializer(mainpage)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def about_items(request):
    try:
        about_item = AboutItems.objects.all().order_by('-id')[:4]
        ser = AboutItemsSerializer(about_item, many=True)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def about(request):
    try:
        about_us = About.objects.last()
        ser = AboutSerializer(about_us)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def direction_items(request):
    try:
        courses = DirectionItems.objects.all().order_by('-id')
        ser = DirectionItemsSerializer(courses, many=True)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def direction(request):
    try:
        direction = Direction.objects.last()
        ser = DirectionSerializer(direction)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def task_items(request):
    try:
        task = TaskItems.objects.all().order_by('-id')[:10]
        ser = TaskItemsSerializer(task, many=True)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def tasks(request):
    try:
        task = Tasks.objects.last()
        ser = TasksSerializer(task)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def results_items(request):
    try:
        result = ResultItems.objects.all().order_by('-id')[:5]
        ser = ResultItemsSerializer(result, many=True)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def result(request):
    try:
        results = Results.objects.last()
        ser = ResultsSerializer(results)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['GET'])
def info(request):
    try:
        contact = Info.objects.last()
        ser = InfoSerializer(contact)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


@api_view(['POST'])
def register(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    birth = request.POST.get('birth')
    email = request.POST.get('email')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    if Register.objects.filter(email=email, phone=phone).exists():
        return Response("you've applied")
    else:
        registration = Register.objects.create(name=name, surname=surname, birth=birth, email=email, address=address, phone=phone)
        registration.save()
        return Response('successfully submitted!')

