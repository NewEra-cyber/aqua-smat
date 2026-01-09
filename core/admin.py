from django.contrib import admin
from .models import SuccessStory

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'locality')
  search_fields = ('name', 'locality')
