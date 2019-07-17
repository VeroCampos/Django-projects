from django.db import models

# Create your models here.
class ShowsManager(models.Manager):
        
    def validator(self,postData):
        errors = {} #add keys and values to error dict
        if len(postData['title'])<2:
            errors['title']= "Title should be at least 2 characters"
        if len(postData['netw'])<3:
            errors['netw']= "Network need at least 3 characters"
        if len(postData['desc'])<10:
            errors['desc']= "Description shoul be at least 10 characters"

        #release = postData['release']
        #if release < updated_at.models.DateTimeField():
           # errors['desc']= "Input wrong date"
        
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=200)
    netw = models.CharField(max_length=100)
    release = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowsManager()
    
    def __str__(self):
        return self.title
