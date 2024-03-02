import email
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    """ Категории """
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(verbose_name="URL")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_url': self.url})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        # db_table имя таблицы в бд


class Actor(models.Model):
    """ Актеры и Режиссеры """
    name = models.CharField(max_length=255, verbose_name='Актер/Режиссер')
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='actors/')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('staff_single', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Актеры и Режиссеры'
        verbose_name_plural = 'Актеры и Режиссеры'


class Genre(models.Model):
    """ Жанры """
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """ Фильм """
    title = models.CharField(verbose_name=_('title'), max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='movies')
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(
        Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(
        Actor, verbose_name='актер', related_name='film_actor')
    genre = models.ManyToManyField(
        Genre, verbose_name='Жанр')
    world_premiere = models.DateField()
    budget = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    url = models.SlugField(verbose_name="URL", db_index=True, unique=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('single', kwargs={'movie_url': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    """ Кадры из фильма """
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадры из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """ Рейтинг """
    ip = models.CharField(max_length=15) # ip адрес клиента
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


class Reviews(models.Model):
    """ Отзывы """
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    text = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
