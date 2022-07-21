from django.conf import settings
from django.db import models

from accounts.models import CustomUser

TRANSPORTATION_CHOICE = (
    ('metro','Metro'),
    ('auto', 'Auto'),
    ('camioneta','Camioneta'),
    ('motocicleta','Motocicleta'),
    ('bus-transantiago','Bus Transantiago'),
    ('bus','Bus'),
    ('avion-nacional','Avión (Nacional)'),
    ('avion-internacional','Avión (Internacional)'),
    ('caminando','Caminando'),
)

ROUNDTRIP_CHOICE = (
    ('ida', 'Ida'),
    ('vuelta', 'Vuelta'),
    ('ida-vuelta', 'Ida y Vuelta'),
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address_start_point = models.TextField()
    address_end_point = models.TextField()
    transportation = models.CharField(max_length=100, choices=TRANSPORTATION_CHOICE)
    kilometers = models.IntegerField()
    users = models.ManyToManyField(CustomUser, related_name="Participants")
    round_trip = models.CharField(max_length=100, choices=ROUNDTRIP_CHOICE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address_start_point + " " + self.address_end_point