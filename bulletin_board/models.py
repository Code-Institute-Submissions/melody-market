from django.db import models

class Advert(models.Model):
    title = models.CharField(max_length=200,default="" )
    description = models.CharField(max_length=1000,blank=True)
    
    def __str__(self):
        return str(self.title)
 
class Text(models.Model):
    advert = models.ForeignKey('Advert',blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=False)
    text = models.CharField(max_length=1000)
    phnumber = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.text)