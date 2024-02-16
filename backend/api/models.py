from django.db import models


class Currencies(models.Model):
    code = models.CharField(max_length=5, unique=True)

    def __str__(self) -> str:
        return f"{self.code}"