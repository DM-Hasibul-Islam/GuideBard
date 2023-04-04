from django.contrib.auth.models import User

#user creation form
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
