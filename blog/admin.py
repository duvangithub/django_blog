<<<<<<< HEAD
# Register your models here.

from django.contrib import admin
from blog.models import Category, Comment, Post


#Se registran los modelos para que aparezcan en el backend de admin
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
=======
# Register your models here.

from django.contrib import admin
from blog.models import Category, Comment, Post


#Se registran los modelos para que aparezcan en el backend de admin
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
>>>>>>> 59e61d335a8682aa485311c599a1c739b9736b32
admin.site.register(Comment, CommentAdmin)