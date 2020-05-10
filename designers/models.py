from django.db import models

from django.contrib.auth.models import User


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


# class DesignerProfile(models.Model):

#     user = models.OneToOneField(User,
#                                 on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=50,
#                                  null=False,
#                                  blank=False)
#     country = models.CharField(max_length=50,
#                                null=False,
#                                blank=False)
#     bio = models.CharField('A few words about the designer',
#                            max_length=254,
#                            null=False,
#                            blank=False)

#     def __str__(self):
#         return self.full_name

#     class Meta:
#         verbose_name = 'Designer Profile'