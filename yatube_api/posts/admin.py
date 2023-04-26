from django.contrib import admin
from posts.models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'pub_date',
                    'author',
                    'group',
                    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'slug',
                    'description',
                    )
    search_fields = ('description',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'author',
                    'created',
                    )
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'author',
                    )
    search_fields = ('user', 'author',)
    list_filter = ('user', 'author',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
