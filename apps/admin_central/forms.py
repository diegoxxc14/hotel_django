from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
  
class CrearUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']