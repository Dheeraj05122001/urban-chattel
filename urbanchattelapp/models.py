from django.db import models

# Create your models here.
class Property(models.Model): 
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=[('Apartment', 'Apartment'), ('Villa', 'Villa'), ('House', 'House')])
    image = models.ImageField(upload_to='property/',default='default.jpg') 
    price_min = models.DecimalField(max_digits=10, decimal_places=2,default=10000000)
    price_max = models.DecimalField(max_digits=10, decimal_places=2,default=10000000)
    project_size_units = models.IntegerField(default=100)
    project_size_acres = models.DecimalField(max_digits=5, decimal_places=2,default=1.0)
    configurations = models.CharField(max_length=255, default="2 BHK")  # Example: "3, 4 BHK"
    flat_size_min = models.IntegerField(default=1000)
    flat_size_max = models.IntegerField(default=1000)
    about = models.TextField(default="No description available")
    project_status = models.CharField(max_length=100,default="Pending")
    loaclity = models.CharField(max_length=100, default="Unknown Locality")
    builder = models.CharField(max_length=200,default="Unknown Builder")
    micro_market = models.CharField(max_length=200,default="Unknown Market")
    gymnasium = models.CharField(max_length=300,default="Not avilabe")
    swimming_pool = models.CharField(max_length=300,default="Not avilabe")
    kids_pool = models.CharField(max_length=300,default="not avilable")
    badminton_court = models.CharField(max_length=300,default="not avilable")
    tennis_court = models.CharField(max_length=300,default="not avilable")
    cricket = models.CharField(max_length=200,default="not avilable")
    kid_play_areas = models.CharField(max_length=300,default="not avilable")
    Basketball = models.CharField(max_length=300,default="not avilable")
    Volleyball = models.CharField(max_length=300,default="not avilable")
    yoga_areas = models.CharField(max_length=300,default="not avilable")
    jogging = models.CharField(max_length=300, default="not avilable")
    table_tennis = models.CharField(max_length=200,default="not avilable")
    Power_backup = models.CharField(max_length=100,default="not avilable")
    treated_water_supply = models.CharField(max_length=100,default="not avilable")
    Guest_house = models.CharField(max_length=100,default="not avilable")
    water_supply = models.CharField(max_length=100,default="not avilable")
    lift = models.CharField(max_length=100,default="not avilable")
    party_lawn = models.CharField(max_length=100,default="not avilable")
    
    def __str__(self):
        return self.name 
