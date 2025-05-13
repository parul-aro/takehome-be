from django.db import models

class House(models.Model):
    zillow_id = models.BigIntegerField(unique=True)  # Add this at the top

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    home_size = models.IntegerField(null=True, blank=True)
    property_size = models.IntegerField(null=True, blank=True)
    home_type = models.CharField(max_length=50, null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)

    price = models.CharField(max_length=20, null=True, blank=True)
    zestimate_amount = models.IntegerField(null=True, blank=True)
    zestimate_last_updated = models.CharField(max_length=20, null=True, blank=True)

    rent_price = models.IntegerField(null=True, blank=True)
    rentzestimate_amount = models.IntegerField(null=True, blank=True)
    rentzestimate_last_updated = models.CharField(max_length=20, null=True, blank=True)

    tax_value = models.FloatField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)

    last_sold_date = models.CharField(max_length=20, null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)

    link = models.URLField()

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zipcode}"