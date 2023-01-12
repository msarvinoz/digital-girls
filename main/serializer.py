from rest_framework import serializers
from .models import *


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DirectionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionItems
        fields = "__all__"


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"


class TaskItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItems
        fields = "__all__"


class AboutItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutItems
        fields = "__all__"


class ResultItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultItems
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['title_ru', 'title_uz']


class RegistrationTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationTab
        fields = '__all__'
