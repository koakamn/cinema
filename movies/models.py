from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table='genre'
        verbose_name_plural='Жанры'
        verbose_name='Жанр'

class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    duration=models.PositiveIntegerField(verbose_name='Продолжительность')
    release_date=models.DateField()
    poster=models.ImageField(upload_to='movies/',blank=True,null=True)
    genres=models.ManyToManyField(Genre,blank=True,related_name='genres')

    def __str__(self):
        return self.title

    class Meta:
        db_table='movie'
        verbose_name='Фильм'
        verbose_name_plural='Фильмы'



