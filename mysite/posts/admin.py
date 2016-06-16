from django.contrib import admin

# Register your models here.
from .models import Post


# customising admin panel
class PostModelAdmin(admin.ModelAdmin):
    # pass
    list_display = ['title', 'timestamp']
    list_filter = ['timestamp']

    class Meta:
        model = Post


admin.site.register(Post,PostModelAdmin)
