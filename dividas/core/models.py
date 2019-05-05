from django.db import models


class Divida(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.CharField(max_length=10)
    motivo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    class Meta:
        verbose_name_plural = 'dividas'
        verbose_name = 'divida'
        db_table = 'divida'

    def __str__(self):
        return f'{self.id} {self.motivo}'
