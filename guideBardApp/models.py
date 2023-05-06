from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class touristSpots(models.Model):
    spot_name = models.CharField(max_length=100)
    spot_details = models.TextField()


class bookings(models.Model):
    bk_start_time = models.DateTimeField()
    bk_end_time = models.DateTimeField()
    bk_amount = models.FloatField()


class emergencyContacts(models.Model):
    station_name = models.CharField(max_length=100)
    em_contact = models.IntegerField()

class payments(models.Model):
    p_method = models.CharField(max_length=50)
    p_trxid = models.CharField(max_length=50)
    p_amount = models.FloatField()
    p_date = models.DateTimeField()


class reviews(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_review = models.TextField()
    r_star = models.FloatField()

class areaTourGuide(models.Model):
    at_id = models.AutoField(primary_key=True)
    at_area_name = models.CharField(max_length=50)
    tg_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ts_id = models.ForeignKey(touristSpots, on_delete=models.CASCADE)
