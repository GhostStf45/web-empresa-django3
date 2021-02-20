from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    admin.site.enable_nav_sidebar = False
    readonly_fields=('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username',)

    # Categorias separadas por comas
    def post_categories(self, obj):
        return ",".join(c.name for c in obj.categories.all().order_by('name'))
    # Implementar nombre propio a post_categories
    post_categories.short_description = 'Categorías'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)