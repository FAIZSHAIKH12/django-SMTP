from django.contrib import admin
from  .models import Mymodel

@admin.register(Mymodel)
class MymodelAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile','email','message']


