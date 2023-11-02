from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
  list_display = ("title","text","score","scores_count")

class ScoreAdmin(admin.ModelAdmin):
  list_display = ("user","post","score")

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Score,ScoreAdmin)