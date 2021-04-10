from  django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class MEta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
