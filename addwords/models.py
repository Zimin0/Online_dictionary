from django.db import models


class Word(models.Model):
    TYPE = (
        (None, "Выберите тип слова"),
        ('v', 'Verb (сущ.)' ),
        ('n', 'Noun (глаг.)'),
        ('a', 'Adjective (прил.)'),
    )
    word = models.CharField(max_length=20, null=True, blank=False, verbose_name="Слово")
    language = models.ForeignKey("Language", on_delete=models.PROTECT, verbose_name="Язык")
    type = models.CharField(max_length=1, choices=TYPE, blank=True)
    translation = models.CharField(max_length=25, verbose_name="Перевод")
    discription = models.TextField(blank=True, verbose_name="Доп. комментарий к переводу")

    def __str__(self):
        return self.word


class Language(models.Model):
    name =  models.CharField(max_length=30, null=True, blank=False, verbose_name="Язык")
    def __str__(self):
        return self.name

