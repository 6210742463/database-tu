from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class DoSomething(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Foundation(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    title = models.ForeignKey(Title, null=True, blank=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    tel_1 = models.CharField(max_length=20, null=True, blank=True)
    tel_2 = models.CharField(max_length=20, null=True, blank=True)
    tel_3 = models.CharField(max_length=20, null=True, blank=True)
    addess = models.TextField(null=True, blank=True)
    county = models.ForeignKey(County, null=True, blank=True, on_delete=models.CASCADE)
    idAddess = models.CharField(max_length=10, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)
    doSomething = models.ManyToManyField(DoSomething, blank=True)
    birthday = models.DateField()
    

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Year(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return f' ปี {self.name} '

class Money(models.Model):
    personKey = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, blank=True, null=True, on_delete=models.CASCADE)
    money = models.DecimalField(decimal_places=4, max_digits=20)

    def __str__(self):
        return f"{self.money}"

class Donate(models.Model):
    personKey = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    foundation = models.ManyToManyField(Foundation, blank=True)
    bank = models.ManyToManyField(Bank, blank=True)
    donation = models.ManyToManyField(Year, blank=True)
    dayDonate = models.DateField(null=True, blank=True)
    idDonate = models.CharField(max_length=30, blank=True, null=True)
    dayOfIdDonate = models.DateField(null=True, blank=True)
    total = models.DecimalField(decimal_places=4, max_digits=20, blank=True, null=True)

    def __str__(self):
        return self.idDonate