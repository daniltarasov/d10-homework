from django.db import models

# Create your models here.


class Car(models.Model):
    TRANS_MECH = 1
    TRANS_AUTO = 2
    TRANS_ROBOT = 3

    TRANSMISSION_CHOICES = [
        (TRANS_MECH, "механика"),
        (TRANS_AUTO, "автомат"),
        (TRANS_ROBOT, "робот"),
    ]
    manufacturer = models.CharField("Производитель", max_length=255)
    model = models.CharField("Модель", max_length=255)
    year_of_manufacture = models.IntegerField("Год выпуска", default=1900)
    transmission = models.SmallIntegerField("Коробка передач", choices=TRANSMISSION_CHOICES, default=TRANS_MECH)
    color = models.CharField("Цвет", max_length=30)
    image = models.ImageField(upload_to='car_img', blank=True, null=True)


    def __str__(self):
        return '{} - {}'.format(self.manufacturer, self.model)

    @classmethod
    def get_fields_names(cls):
        names = {}
        have_choices = {}
        fields = cls._meta.get_fields()
        for field in fields:
            names[field.name] = field.verbose_name
            if field.choices:
                have_choices[field.name] = field.choices
        # dict = {field.name: field.verbose_name for field in cls._meta.get_fields()}
        return names, have_choices
    
