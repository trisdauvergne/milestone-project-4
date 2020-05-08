from django.db import models

# Create your models here.


class Designer(models.Model):

    full_name = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)
    country = models.CharField(max_length=50,
                               null=False,
                               blank=False)
    bio = models.CharField('A few words about the designer',
                           max_length=254,
                           null=False,
                           blank=False)
    email = models.EmailField(max_length=254,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Designer'


class Print(models.Model):

    designer = models.ForeignKey('Designer',
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
