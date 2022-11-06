from django.db import models

class Category(models.Models):
    name = models.CharField(max_length=255) #name of the category
    slug = models.SlugField() #address version of the name

    class Meta:     #order the categories by the name
        ordering = ('name',) #tuple ('name',)

    def __str__(self):    # string representation of the category what type of  object it is
        return self.name

    def get_absolute_url(self): #get the url of the categiry easier to use in frontend later
        return f'/{self.slug}/' #address of the category
     