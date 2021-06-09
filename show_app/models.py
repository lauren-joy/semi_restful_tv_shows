from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters long"
        if len(postData['network']) <3:
            errors["network"] = "Network should be at least 3 characters long"
        if len(postData['description']) <10:
            errors["description"] = "Description should be at least 10 characters long "
        return errors

class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateTimeField() 
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= ShowManager()

    def __repr__(self):
        return f"<Show object: {self.title} ({self.network}) ({self.release_date}) ({self.description})>"

