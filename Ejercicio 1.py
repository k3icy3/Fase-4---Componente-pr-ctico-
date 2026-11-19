#Creacion de las excepciones
class ErrorBaseSistema(Exception):
    """Excepción donde se heredan todos los errores del sistema."""
    def __init__(self, mensaje: str, codigo_error: int = 500):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)

class EntidadNoEncontradaError(ErrorBaseSistema):
    """Se ejecuta cuando no se halla ningun registro o entidad."""
    def __init__(self, entidad: str, id_entidad: str | int):
        mensaje = f"No se hallo la entidad '{entidad}' con el ID: {id_entidad}."
        super().__init__(mensaje, codigo_error=404)

class ValidacionEntidadError(ErrorBaseSistema):
    """Se ejecuta cuando los datos de una entidad no cumplen las reglas de negocio."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error=400)
    
#Creacion de logger
import logging
import os
from logging.handlers import RotatingFileHandler

def obtener_logger(nombre_modulo: str) -> logging.Logger:
    """Configura los logger listo para validar cualquier registro."""

#Creacion de la clase abstracta cliente
from abc import ABC,abstractmethod
from datetime import datetime
import uidd
class entidades(ABC):
    def_init_(self):
    self.id = str(uuid.uuid4())
    self.fecha_creacion = datetime.now()
    self.fecha_actualizacion = None
    self.activo = True
def marcar_actualizada(self):
    self.fecha_actualizacion = datetime.now()
@abstractmethod
def es_validar(self)->bool:
    pass

import re
from abc import ABC, abstractmethod
class entidades(ABC):
    def_init_(self, identidades: str):
    self._id = id_entidades

@abstractmethod 
def obtener_informacion(self): -> str:
    pass
class cliente(entidades):
    def_init_(self, id_entidades:str,nombre:str,apellido:str,telefono:str,gmail:str)
    super()._init_(id_entidades)
    #se ejecuta para modificar la clase con
@setter
self.nombre = nombre
self.apellido = apellido
self.telefono = telefono
self.direccion = direccion

#Validacion del nombre mediante encapsulación 
@property
def nombre(self)->str:
    return self._nombre
    
@nombre.setter
def nombre(self,valor:str):
    if not isintance(valor,str) or len(valor.strip())<6:
        raise ValueError("el nombre debe tener 6 caracteres.")
        self._nombre=valor.strip()
#Validacion del apellido mediante la encapsulación 
@property
def apellido(self)->str:
    return self._apellido

@apellido.setter
def apellido(self,valor:str):
    if not isintance(valor,str) or len(valor.strip())<5:
        raise ValueError("el apellido debe tener 5 caracteres.")
        self._apellido=valor.strip()
        
#Validacion del telefono mediante la encapsulación 
    @property
def telefono(self)->str:
    return self._nombre
    
    @telefono.setter
def telefono(self,valor:str):
    if not isintance(valor,str) or not valor.strip().isdigit()ornot
        raise ValueError("el nombre debe tener 6 caracteres.")
        self._nombre=valor.strip()

    
#Validacion del gmail mediante la encapsulación 
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise ValueError("El correo electrónico es inválido.")
        self.__email = valor.strip().lower()

#Ejecucion del método abstracto
    def obtener_informacion(self) -> str:
        return f"Cliente: {self.__nombre} {self._apellido} | Correo: {self.__email} | Telefono: {self._telefono}"
        return all([
            boll.(self.id_entiades),
            boll.(self.nombre),
            boll.(self.apellido),
            boll.(self.telefono),
            boll.(self.gmail),
])

#Creacion de la clase abstracta servicio
from abc import ABC, abstractmethod

class servicio(ABC):
    def __init__(self, id_servicio: int, nombre: str, precio: float):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad 
        
    @property
    def nombre(self) -> str:
        return self._nombre
        
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValidacionEntidadError(mensaje)
        self._nombre = valor.strip()
        self.marcar_actualizado()

     @property
       def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            mensaje = f"La tarifa base debe ser mayor a 0. Valor recibido: {valor}"
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self._precio = float(valor)
        self.marcar_actualizada()
        
        @property
    def disponibilidad(self) -> bool:
        return self._disponible

    @disponibilidad.setter
    def disponibilidad(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise ValidacionEntidadError("La disponibilidad se define por ser booleano.")
        self._disponibilidad = estado
        self.marcar_actualizada()

    def verificar_disponibilidad(self) -> None:
        """Ejecuta una excepción personalizada para el servicio sino se encuentra habilitado."""
        if not self._disponibilidad or not self.activo:
            logger.warning(f"Intento de ingreso al servicio no disponible: {self._nombre}")
            raise ServicioNoDisponibleError(self._nombre)

    def aplicar_ajustes_costo(
        self,
        subtotal: float,
        impuesto_pct: float = 0.0,
        descuento_pct: float = 0.0,
    ) -> float:


#Creacion de la clase reserva
Class reserva(Entidades):
    def __init__(self, cliente, servicio, duracion):
        super().__init__()

         
