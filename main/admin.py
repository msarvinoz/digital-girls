from django.contrib import admin
from .models import *

admin.site.register(MainPage)
admin.site.register(About)
admin.site.register(AboutItems)
admin.site.register(Direction)
admin.site.register(DirectionItems)
admin.site.register(Tasks)
admin.site.register(TaskItems)
admin.site.register(Results)
admin.site.register(ResultItems)
admin.site.register(Info)
admin.site.register(User)


class RegisterAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'birth', 'email', 'address', 'phone', 'created')

    #list of fields to display in django admin
    list_display = ['name', 'surname', 'birth', 'email', 'address', 'phone', 'created']


    #if you want django admin to show the search bar, just add this line
    search_fields = ['name', 'birth', 'created']

    #to define model data list ordering
    ordering = ('id','name', 'surname', 'birth', 'email', 'address', 'phone', 'created')
    readonly_fields = ['created']


admin.site.register(Register, RegisterAdmin)
