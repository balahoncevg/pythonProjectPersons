from django.db import models
from django.conf import settings

# Create your models here.

class Persone(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    bl_gr = models.CharField(max_length=5)
    is_fired = models.BooleanField(null=True)
    is_maried = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.second_name}'

class Mariage(models.Model):
    persone1 = models.ForeignKey(Persone, on_delete=models.CASCADE)
    persone2 = models.ForeignKey(Persone, on_delete=models.CASCADE)
    beginning_of_mariage = models.DateField()
    ending_of_mariage = models.DateField()


class LivingPlace(models.Model):
    owner = models.ForeignKey(Persone, on_delete=models.CASCADE)
    town = models.CharField(max_length=200)
    post_id = models.CharField(max_length=20)
    adresss = models.TextField()
    whos_place = models.CharField(max_length=200)

class Doing(models.Model):
    who_did = models.ForeignKey(Persone, on_delete=models.CASCADE)
    what_did = models.TextField()
    rating = models.IntegerField()
    when_did = models.DateField()

    def __str__(self):
        return self.what_did

#функция
def pers_info(persone_id):
    persone = Persone.objects.get(id=persone_id)
    good_doings = persone.doing_set.filter(rating__gt=5).cont()
    mid_doings = persone.doing_set.filter(rating=5).count()
    bad_doings = persone.doing_set.filter(rating__lt=5).count()
    av_rating = persone.doing__rating.sum() / persone.doing_set.count()
    a = {
        'name': persone.__str__(),
        'good doings': good_doings,
        'mid doings': mid_doings,
        'bad doings': bad_doings,
        'rating': av_rating
    }
    return a

#запрос
Persone.objects.filter(
        is_maried=True,
        is_fired=None,
        livingplace__town=town,
        doing__rating__gt=6,
    ).count()
