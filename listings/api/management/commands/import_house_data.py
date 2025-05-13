import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import House

class Command(BaseCommand):
    help = "Import house data from sample-data/data.csv"

    def handle(self, *args, **kwargs):
        csv_path = os.environ.get("CSV_PATH") or os.path.join(settings.BASE_DIR, "sample-data", "data.csv")

        if not os.path.exists(csv_path):
            self.stderr.write(f"File not found: {csv_path}")
            return

        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    House.objects.update_or_create(
                        zillow_id=row["zillow_id"],
                        defaults={
                            "address": row["address"],
                            "city": row["city"],
                            "state": row["state"],
                            "zipcode": row["zipcode"],
                            "bathrooms": float(row["bathrooms"]) if row["bathrooms"] else None,
                            "bedrooms": int(row["bedrooms"]) if row["bedrooms"] else None,
                            "home_size": int(row["home_size"]) if row["home_size"] else None,
                            "property_size": int(row["property_size"]) if row["property_size"] else None,
                            "home_type": row["home_type"] or None,
                            "year_built": int(row["year_built"]) if row["year_built"] else None,
                            "price": row["price"] or None,
                            "zestimate_amount": int(row["zestimate_amount"]) if row["zestimate_amount"] else None,
                            "zestimate_last_updated": row["zestimate_last_updated"] or None,
                            "rent_price": int(row["rent_price"]) if row["rent_price"] else None,
                            "rentzestimate_amount": int(row["rentzestimate_amount"]) if row["rentzestimate_amount"] else None,
                            "rentzestimate_last_updated": row["rentzestimate_last_updated"] or None,
                            "tax_value": float(row["tax_value"]) if row["tax_value"] else None,
                            "tax_year": int(row["tax_year"]) if row["tax_year"] else None,
                            "last_sold_date": row["last_sold_date"] or None,
                            "last_sold_price": int(row["last_sold_price"]) if row["last_sold_price"] else None,
                            "link": row["link"],
                        }
                    )
                except Exception as e:
                    self.stderr.write(f"Error importing row with zillow_id {row.get('zillow_id')}: {e}")

        self.stdout.write(self.style.SUCCESS("House data import completed."))
