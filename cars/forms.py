from django import forms
from cars.models import Car
  
  
class CarSearchForm(forms.ModelForm):  


    TRANS_MECH = 1
    TRANS_AUTO = 2
    TRANS_ROBOT = 3
    TRANS_NONE = None

    TRANSMISSION_CHOICES = [
        (TRANS_MECH, "механика"),
        (TRANS_AUTO, "автомат"),
        (TRANS_ROBOT, "робот"),
        (TRANS_NONE, "не выбрано")
    ]

    manufacturer = forms.CharField(required=False, label="Прозводитель")
    model = forms.CharField(required=False, label="Модель")
    year_of_manufacture = forms.IntegerField(required=False, label="Год выпуска")
    transmission = forms.ChoiceField(required=False,  choices=TRANSMISSION_CHOICES, label="Коробка передач")
    color = forms.CharField(required=False, label="Цвет")
  
    class Meta:  
        model = Car  
        fields = ['manufacturer', 'model', 'year_of_manufacture', 'transmission', 'color']
