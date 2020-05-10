from django.db import models

# from designers.models import Designers
from django.contrib.auth.models import User


class Print(models.Model):

    designer = models.ForeignKey(User,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=254,
                             null=False,
                             blank=False)
    description = models.CharField('A few words about this work',
                                   max_length=254,
                                   null=False,
                                   blank=False)
    size = models.CharField(max_length=30,
                            null=False,
                            blank=False)
    price = models.DecimalField(max_digits=30,
                                decimal_places=2,
                                null=False,
                                blank=False)
    image = models.ImageField(upload_to='previews/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Print'
