from django.db import models
from django.contrib.auth.models import User

class Coins(models.Model):
# pk - primary key
    name = models.CharField(max_length=500)
    symbol = models.TextField()
    coin_type = models.TextField()
    url = models.TextField()
    icon = models.ImageField(upload_to='images/')
    coin_price = models.DecimalField(max_digits=40, decimal_places=5)
    coin_volume = models.DecimalField(max_digits=40, decimal_places=5)
    market_cap = models.DecimalField(max_digits=40, decimal_places=5)

    def __str__(self):
        return str(self.symbol)

    def as_dict(self):
        return {
            "name": self.name,
            "Symbol": self.symbol
            # other stuff
        }
