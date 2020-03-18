from django.contrib import admin
from .models import Post, Contact, FAQ, AboutSection
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    display_list = ['email', 'full_name']
admin.site.register(FAQ)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    display_list = ['title', 'display', 'pub_date', 'contains_image']

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    display_list = ['title', 'display']
