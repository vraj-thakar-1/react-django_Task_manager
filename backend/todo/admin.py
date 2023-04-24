from django.contrib import admin
from .models import Todo
# Django Admin is a really great tool in Django, it is actually a CRUD* user interface of all your models!

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
    
