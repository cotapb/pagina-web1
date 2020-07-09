from django.db import models



class Covid(models.Model):
    enfermedad= models.IntegerField()
    def publish(self):
        self.save()

class  Sintoma(models.Model):

    nombre = models.CharField(max_length=200)
    presencia = models.CharField(max_length=200)
    RISK_CHOICES=(
         ('8', 'Alto Riesgo'),
         ('4', 'Medio Riesgo'),
         ('3', 'Bajo Riesgo'),
 
     )

    severidad = models.CharField(max_length=1, choices=RISK_CHOICES)

    def publish(self):
        self.save()

class Resultado(models.Model):
    contacto = models.CharField(max_length=4)
    edad = models.CharField(max_length=5)
    sexo = models.CharField(max_length=7)
    region = models.CharField(max_length=45)
    total = models.CharField(max_length=3)
    def publish(self):
        self.save()


