from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ("title","text","score")

class ScoreAdmin(admin.ModelAdmin):
  list_display = ("user","post","score")

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Score,ScoreAdmin)