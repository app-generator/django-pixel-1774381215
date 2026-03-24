# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Categoria(models.Model):

    #__Categoria_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Categoria_FIELDS__END

    class Meta:
        verbose_name        = _("Categoria")
        verbose_name_plural = _("Categoria")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    puntos = models.CharField(max_length=255, null=True, blank=True)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Mesa(models.Model):

    #__Mesa_FIELDS__
    numero = models.CharField(max_length=255, null=True, blank=True)

    #__Mesa_FIELDS__END

    class Meta:
        verbose_name        = _("Mesa")
        verbose_name_plural = _("Mesa")


class Pedido(models.Model):

    #__Pedido_FIELDS__
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Pedido_FIELDS__END

    class Meta:
        verbose_name        = _("Pedido")
        verbose_name_plural = _("Pedido")


class Producto(models.Model):

    #__Producto_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.CharField(max_length=255, null=True, blank=True)
    costo = models.CharField(max_length=255, null=True, blank=True)
    stock = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    #__Producto_FIELDS__END

    class Meta:
        verbose_name        = _("Producto")
        verbose_name_plural = _("Producto")


class Detalle_Pedido(models.Model):

    #__Detalle_Pedido_FIELDS__
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=255, null=True, blank=True)
    precio_unitario = models.CharField(max_length=255, null=True, blank=True)
    subtotal = models.CharField(max_length=255, null=True, blank=True)

    #__Detalle_Pedido_FIELDS__END

    class Meta:
        verbose_name        = _("Detalle_Pedido")
        verbose_name_plural = _("Detalle_Pedido")



#__MODELS__END
