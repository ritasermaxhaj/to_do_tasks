from django.contrib import admin

from tasks.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('title', 'comment')
    list_filter = ('is_completed', 'due_date')
    ordering = ('-created_at',)

    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)