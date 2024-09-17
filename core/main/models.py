from django.db import models

# Create your models here.


class Home(models.Model):
    name = models.CharField('home page name' , max_length=50)
    img = models.ImageField('home page img' , upload_to='media')


    def __str__(self):
        return self.name
    

class About(models.Model):
    About1 = models.TextField('about1')
    About2 = models.TextField('about2')
    img = models.ImageField('about' , upload_to='media')
    paragraf = models.TextField('paragraf', max_length=100)

    def __str__(self):
        return self.About1