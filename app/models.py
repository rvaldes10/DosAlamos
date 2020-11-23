from django.db import models

# Create your models here.

class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    Rut_Cliente = models.CharField(max_length=15, unique=True)
    Nombre_Completo = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Completo

    class Meta:
        db_table = "Cliente"

class Orden_Compra(models.Model):
    ID_Compra = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    Fecha_Emision = models.DateTimeField()
    Valor_Total = models.IntegerField()

    class Meta:
        db_table = "Orden_de_Compra"

class Despacho(models.Model):
    ID_Despacho = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    Orden_Compra = models.ForeignKey(Orden_Compra, on_delete=models.PROTECT)
    Fecha_Entrega = models.DateField()

    class Meta:
        db_table = "Despacho"
