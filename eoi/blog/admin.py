from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title','auhor','created_date','published_date')
  list_filter = ('created_date', 'auhor','published_date','title')
  search_fields = ('title', 'id' , 'text')
  prepopulated_fields = {'slug' : ('title',)}
  

admin.site.register(Post, PostAdmin)
