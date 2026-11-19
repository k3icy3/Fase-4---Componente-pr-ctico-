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
        
import logging
import os
from logging.handlers import RotatingFileHandler

def obtener_logger(nombre_modulo: str) -> logging.Logger:
    """Configura los logger listo para validar cualquier registro."""
  
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
self.





