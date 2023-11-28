from django.contrib import admin
from .models import Testtitle,Student

class TesttitleAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','testtitle')
    list_display_links = ('user','testtitle')


admin.site.register(Testtitle, TesttitleAdmin)
admin.site.register(Student, StudentAdmin)