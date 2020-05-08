from django.db import models


class Designers(models.Model):

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
