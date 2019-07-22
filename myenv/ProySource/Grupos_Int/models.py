from django.db import models

# Create your models here.


class Universidad (models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)


class Pais (models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return "{0}".format(self.nombre)


class Requerimiento (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    area = models.CharField(max_length=50)

    def __str__(self):
        return "{0} : {1}".format(self.nombre, self.descripcion)


class Facultad (models.Model):
    universidad = models.ForeignKey(
        Universidad, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)


class Departamento (models.Model):
    pais = models.ForeignKey(
        Pais, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.nombre)


class Autoridad (models.Model):
    facultad = models.ForeignKey(
        Facultad, null=False, blank=False, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    grado = models.CharField(max_length=30)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return "{0} : {1} {2}, {3}".format(self.cargo, self.apellidoPaterno, self.apellidoMaterno, self.nombres)


class Escuela(models.Model):
    facultad = models.ForeignKey(
        Facultad, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)


class Provincia (models.Model):
    departamento = models.ForeignKey(
        Departamento, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)


class Distrito (models.Model):
    provincia = models.ForeignKey(
        Provincia, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)


class Institucion (models.Model):
    distrito = models.ForeignKey(
        Distrito, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    paginaWeb = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ruc = models.CharField(max_length=20)

    def __str__(self):
        return "{0} : {1}".format(self.nombre, self.descripcion)


class Perfil (models.Model):
    institucion = models.ForeignKey(
        Institucion, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return "{0}".format(self.descripcion)


class PerfilRequerimiento (models.Model):
    requerimiento = models.ForeignKey(
        Requerimiento, null=False, blank=False, on_delete=models.CASCADE)
    perfil = models.ForeignKey(
        Perfil, null=False, blank=False, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=80)

    def __str__(self):
        return "{0}".format(self.prioridad)


class Representante (models.Model):
    institucion = models.ForeignKey(
        Institucion, null=False, blank=False, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return "{0} : {1} {2}, {3}".format(self.cargo, self.apellidoPaterno, self.apellidoMaterno, self.nombres)


class Convenio (models.Model):
    escuela = models.ForeignKey(
        Escuela, null=False, blank=False, on_delete=models.CASCADE)
    institucion = models.ForeignKey(
        Institucion, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return "{0} <> {1}".format(self.institucion, self.escuela)


class PlanDeCapacitacion (models.Model):
    convenio = models.ForeignKey(
        Convenio, null=False, blank=False, on_delete=models.CASCADE)
    denominacion = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.denominacion)


class Actividad (models.Model):
    capacitacion = models.ForeignKey(
        PlanDeCapacitacion, null=False, blank=False, on_delete=models.CASCADE)
    funcionPrincipal = models.CharField(max_length=50)
    tareasDerivadas = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(self.funcionPrincipal)

class Objetivo (models.Model):
    capacitacion = models.ForeignKey(
        PlanDeCapacitacion, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)    
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return "{0} : {1}".format(self.nombre, self.descripcion)

class Beneficio (models.Model):
    convenio = models.ForeignKey(
        Convenio, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    beneficiado = models.CharField(max_length=100)

    def __str__(self):
        return "{0} => {1}".format(self.descripcion, self.beneficiado)


class Competencia (models.Model):
    capacitacion = models.ForeignKey(
        PlanDeCapacitacion, null=False, blank=False, on_delete=models.CASCADE)
    compEspecificas = models.CharField(max_length=200)
    compGenericas = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(self.compEspecificas)


class Condicion (models.Model):
    convenio = models.ForeignKey(
        Convenio, null=False, blank=False, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipoSeguroCobertura = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=50)


class Horario (models.Model):
    condicion = models.ForeignKey(
        Condicion, null=False, blank=False, on_delete=models.CASCADE)
    dias_trabajar = models.CharField(max_length=200)
    minimo_horas = models.CharField(max_length=200)
    maximo_horas = models.CharField(max_length=200)
    hora_salida = models.CharField(max_length=200)
    hora_entrada = models.CharField(max_length=200)

    def __str__(self):
        return "{0} => {1} - {2}".format(self.dias_trabajar, self.hora_entrada, self.hora_salida)
