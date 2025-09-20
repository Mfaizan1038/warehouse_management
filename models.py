from django.db import models


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class ItemType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    default_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name} ({self.category.name})"



class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.location}"



class ItemInstance(models.Model):
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    location_in_warehouse = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True) 
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.type.name} in {self.warehouse.name} at {self.location_in_warehouse}"
