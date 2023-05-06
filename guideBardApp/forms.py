from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from guideBardApp.models import touristSpots
from guideBardApp.models import bookings
from guideBardApp.models import emergencyContacts
from guideBardApp.models import payments
from guideBardApp.models import reviews
from guideBardApp.models import areaTourGuide


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]


class touristSpot(forms.ModelForm):
    class Meta:
        model = touristSpots
        fields = [
            'spot_name',
            'spot_details',
        ]


class bookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = [
            'bk_start_time',
            'bk_end_time',
            'bk_amount',
        ]


class emergencyContactsForm(forms.ModelForm):
    class Meta:
        model = emergencyContacts
        fields = [
            'station_name',
            'em_contact',
            # 'ts_id',
        ]


class paymentForm(forms.ModelForm):
    class Meta:
        model = payments
        fields = [
            'p_method',
            'p_trxid',
            'p_amount',
            'p_date',
        ]


class reviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = [
            'tg_id',
            't_id',
            'r_review',
            'r_star',
        ]

class areaTourGuideForm(forms.ModelForm):
    class Meta:
        model = areaTourGuide
        fields = [
            'at_area_name',
            'tg_id',
            'ts_id',
        ]