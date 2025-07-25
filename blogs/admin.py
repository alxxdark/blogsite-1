from django.contrib import admin
from .models import Category, Blog, Comment, Profile
from .models import ContactMessage
from .models import StaticPage

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title" , "category" , "author","status", "is_featured")
    search_fields = ("id","title","category__category_name","status")   
    list_editable = ("is_featured",)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(ContactMessage)
admin.site.register(StaticPage)