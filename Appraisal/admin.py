from django.contrib import admin
from .models import Employee, Department, Post, Question

admin.autodiscover()


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Names', 'Branch', 'is_favorite')
    search_fields = ['Names']


admin.site.register(Employee, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Leader', 'is_favorite')
    search_fields = ['Name']


admin.site.register(Department, DepartmentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Department')
    search_fields = ['Title']


admin.site.register(Post, PostAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('About_me', 'Title')


admin.site.register(Question, QuestionAdmin)
