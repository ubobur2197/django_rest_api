from django.db import models

class Ustoz(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.subject})"


class Guruh(models.Model):
    name = models.CharField(max_length=100)
    ustoz = models.ForeignKey(
        Ustoz, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='guruhlar'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Talaba(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    grade = models.CharField(max_length=10)
    group = models.ForeignKey(
        Guruh, 
        on_delete=models.CASCADE, 
        related_name='talabalar'
    )

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.grade})"
