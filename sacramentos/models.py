from django.db import models

class Diocesis(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, default='Ecuador')
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Parroquia(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    diocesis = models.ForeignKey(Diocesis, related_name='parroquias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Sacerdote(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    parroquia = models.ForeignKey(Parroquia, related_name='sacerdotes', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Sacramento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    orden = models.PositiveSmallIntegerField()
    iniciacion = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Celebracion(models.Model):
    sacramento = models.ForeignKey(Sacramento, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    sacerdote = models.ForeignKey(Sacerdote, on_delete=models.SET_NULL, null=True, blank=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    fecha_celebracion = models.DateField()
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.sacramento.nombre} - {self.persona}"
