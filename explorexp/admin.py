from django.contrib import admin

# Register your models here.
from explorexp.models import Place, Challenge, Post, Category

admin.site.register(Place)
admin.site.register(Challenge)
admin.site.register(Post)
admin.site.register(Category)