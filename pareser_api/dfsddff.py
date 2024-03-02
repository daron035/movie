import json, os
import sqlite3 as sq

cur_path = os.path.dirname(__file__)
os.chdir(cur_path)
# os.chdir(r'/Users/kamilkusakov/mydoc/PyDocs/PROJECT/mysite:v1:/pareser_api/')

# new_path = os.path.relpath('..\\subfldr1\\testfile.txt', cur_path)


try:
    with open('db.json', 'r', encoding='utf-8') as f: # , 'r', encoding='utf-8'
        data = json.load(f)
except Exception:
    print(Exception)
    
title = data["films"][0]["nameRu"]
# tagline = data["films"][0]["filmId"]

# print(title)
# print(tagline)

for i in data['films']:
    print(i['nameRu'])

    # title = models.CharField(verbose_name=_('title'), max_length=255)
    # tagline = models.CharField(max_length=255)
    # description = models.TextField(verbose_name='Описание')
    # poster = models.ImageField(upload_to='movies')
    # age = models.PositiveSmallIntegerField()
    # country = models.CharField(max_length=255)
    # directors = models.ManyToManyField(
    #     Actor, verbose_name='режиссер', related_name='film_director')
    # actors = models.ManyToManyField(
    #     Actor, verbose_name='актер', related_name='film_actor')
    # genre = models.ManyToManyField(
    #     Genre, verbose_name='Жанр')
    # world_premiere = models.DateField()
    # budget = models.PositiveSmallIntegerField()
    # fees_in_usa = models.PositiveSmallIntegerField()
    # fees_in_world = models.PositiveSmallIntegerField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # url = models.SlugField(verbose_name="URL", db_index=True, unique=True)
    # is_published = models.BooleanField(default=True)
    # time_create = models.DateTimeField(
    #     auto_now_add=True, verbose_name="Дата создания")
    # time_update = models.DateTimeField(
    #     auto_now=True, verbose_name="Дата обновления")

    # def __str__(self):
    #     return self.title
    
    # def get_absolute_url(self):
    #     return reverse('single', kwargs={'movie_url': self.url})

    # class Meta:
    #     verbose_name = 'Фильм'
    #     verbose_name_plural = 'Фильмы'
