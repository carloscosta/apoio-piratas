
from django.db import models



class Collector(models.Model):
    BOARD = 'BO'
    POINT = 'PO'

    COLLECTOR_TYPE = ( (BOARD, 'Comitê de Coleta'), (POINT, 'Ponto de Coleta'), )

    text_description = models.CharField(max_length=300)
    collector_type   = models.CharField(max_length=2, choices=COLLECTOR_TYPE, default=POINT)
    pub_date         = models.DateTimeField('date published')

    def is_upperclass(self):
        return self.collector_type in (self.BOARD, self.POINT)


class Detail(models.Model):
    collector       = models.ForeignKey(Collector, on_delete=models.CASCADE)
    chairman_name   = models.TextField()
    street_name     = models.TextField()
    street_cep      = models.PositiveIntegerField(default=0,)
    region_place    = models.CharField(max_length=300)
    city_name       = models.TextField() ## TODO: find a pre computed list
    estate_name     = models.TextField() ## TODO: find a pre computed list
    telefone_number = models.PositiveIntegerField(default=0,)
    website_address = models.CharField(max_length=300)
    email_address   = models.CharField(max_length=300)
    coordinates     = models.CharField(max_length=300)

