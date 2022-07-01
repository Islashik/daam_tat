from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField
# Register your models here.

class ProductAdminForm(ModelForm):
    description = CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        'name',
        'price',
        'image',
        'is_active',
        'ingredients'
    ]


