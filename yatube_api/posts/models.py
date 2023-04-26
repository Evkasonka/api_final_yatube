from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Наименование группы',
        help_text='Наименование группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug для URL',
        help_text='Короткое имя для URL'
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='О чем пишут в данной группе'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст нового поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Сортировка по дате',
        help_text='Сортировка по дате добавления'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Автор поста'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа,к которой относится пост'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Картинка, которая относится к посту',
        upload_to='posts/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        help_text='Комментируемый'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор комментария'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст нового комментария'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время комментария',
        help_text='Дата и время комментария'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.text[:30]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик',
        help_text='пользователь, который подписывается'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='пользователь, на которого подписываются',
        help_text='Автор постов, на которого подписываются'
    )

    class Meta:
        constraints = (UniqueConstraint(
            fields=('user', 'following'), name='unique_follow'),)

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
