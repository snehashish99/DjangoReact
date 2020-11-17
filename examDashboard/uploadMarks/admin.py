from django.contrib import admin
from .models import exam_data

# Register your models here.
class ExamDataAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','gender','physics','chemistry','maths']

admin.site.register(exam_data,ExamDataAdmin)
