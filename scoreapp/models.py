from django.db import models
from accounts.models import CustomUser
from django.core import validators

class Testtitle(models.Model):
    title = models.CharField(
        verbose_name='テスト名',
        max_length=50
    ) 
    def __str__(self):
        return self.title

class Student(models.Model):    
    user = models.ForeignKey(
        CustomUser,
        verbose_name='氏名',
        on_delete=models.CASCADE
    )

    testtitle = models.ForeignKey(
        Testtitle,
        verbose_name='テスト名',
        on_delete=models.CASCADE
    )
    
    Japanese = models.IntegerField(
        verbose_name='国語',
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100),
                    validators.RegexValidator(
                        message='正しい得点を入力してください',
                    )]
    )

    Math = models.IntegerField(
        verbose_name='数学',
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100),
                    validators.RegexValidator(
                        message='正しい得点を入力してください',
                    )]
    )

    Science = models.IntegerField(
        verbose_name='理科',
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100),
                    validators.RegexValidator(
                        message='正しい得点を入力してください',
                    )]
    )

    Sociology = models.IntegerField(
        verbose_name='社会',
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100),
                    validators.RegexValidator(
                        message='正しい得点を入力してください',
                    )]
    )

    English = models.IntegerField(
        verbose_name='英語',
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100),
                    validators.RegexValidator(
                        message='正しい得点を入力してください',
                    )]
    )
