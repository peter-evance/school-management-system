from djoser.email import ActivationEmail as DjoserActivationEmail
from djoser.email import ConfirmationEmail as DjoserConfirmationEmail
from djoser.email import (
    PasswordChangedConfirmationEmail as DjoserPasswordConfirmationEmail,
)


class CustomActivationEmail(DjoserActivationEmail):
    template_name = "activation.html"


class CustomConfirmationEmail(DjoserConfirmationEmail):
    template_name = "confirmation.html"


class CustomPasswordConfirmationEmail(DjoserPasswordConfirmationEmail):
    template_name = "password_changed_confirmation.html"
