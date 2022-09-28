from django.db import models
# Create your models here.


class District(models.Model):
     name = models.CharField(max_length=40)

     def __str__(self):
            return self.name

class City(models.Model):
    distrct = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
            return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    distrct = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Invoice(models.Model):
    name = models.CharField(max_length=200)

    district= models.ForeignKey(District, on_delete=models.SET_NULL, blank=True,
                                    null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True,
                             null=True)
    def __str__(self):
            return self.name


