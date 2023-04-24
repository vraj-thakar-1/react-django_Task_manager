from django.db import models

# Create your models here.
# whenever you change model make migrations
# this is the file which concern about the database
# makemigrations : It is used to create a migration file that contains code for the tabled schema of a model.
# migrate : It creates table according to the schema defined in the migration file.
# job of serializer is to basically convert model instances to json 
class Todo(models.Model):
    title= models.CharField(max_length=120)
    description= models.CharField(max_length= 500)
    completed= models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
