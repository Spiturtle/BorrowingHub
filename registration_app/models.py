from django.db import models

class TblUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "registration_app_tbluser"  # Changed to match your existing table
        managed = True  # Set to True so Django can work with it