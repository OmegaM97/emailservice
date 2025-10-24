from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Client(AbstractUser):
    api_token = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
