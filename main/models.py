from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='Аватар',
                               **NULLABLE)  # null, blank делаем поле необязательным

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)

    is_active = models.BooleanField(default=True, verbose_name='Учится')


class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name='Предмет')
    description = models.TextField(verbose_name='Описание')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
