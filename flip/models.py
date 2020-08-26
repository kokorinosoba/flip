from django.db import models

class Flip(models.Model):
    team_name = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    is_front = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.team_name} : {self.text}'
