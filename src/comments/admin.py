from django.contrib import admin
from comments.models import CommentsBook, CommentsOrder

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user',  'body')
    class Meta:
        model=CommentsBook
admin.site.register(CommentsBook, CommentAdmin)


admin.site.register(CommentsOrder)