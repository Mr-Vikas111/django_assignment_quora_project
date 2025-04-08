from django.contrib import admin
from .models import *


class QuestionDataAdmin(admin.ModelAdmin):
    list_display = ['id','question','user','is_active','created']
    ordering=['-created']
admin.site.register(QuestionData,QuestionDataAdmin)


class QuestionAnswerDataAdmin(admin.ModelAdmin):
    list_display = ['id','question','answer','commented_by','created']
    ordering=['-created']
admin.site.register(QuestionAnswerData,QuestionAnswerDataAdmin)

class QuestionLikesDataAdmin(admin.ModelAdmin):
    list_display = ['id','question','liked_by','created']
    ordering=['-created']
admin.site.register(QuestionLikesData,QuestionLikesDataAdmin)