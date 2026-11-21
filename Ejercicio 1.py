#Creacion de las importaciones 
from abc import ABC, abstractmethod
import logging
import os
from logging.handlers import RotatingFileHandler
import re
import uuid
import datetime


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

class ServicioNoDisponibleError(ErrorBaseSistema):
    """Se ejecuta cuando un servicio no está disponible o está inactivo."""
    def __init__(self, nombre_servicio: str):
        mensaje = f"El servicio {nombre_servicio} no se encuentra disponible."
        super().__init__(mensaje, codigo_error=409)

class ReservaNoDisponibleError(ErrorBaseSistema):
    """Se ejecuts cuando una reserva no está disponible."""
    def __init__(self, nombre_reseva: str):
        mensaje = f"La Reseva{nombre_reseva} no se encuentra disponible."
        super().__init__(mensaje, codigo_error=500)
    
#Creacion de los loggers
def obtener_logger(nombre_modulo: str) -> logging.Logger:
    """Al ejecutarlo se puede configurar y devolver un logger listo para registrar eventos y errores."""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(nombre_modulo)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        consola_handler = logging.StreamHandler()
        consola_handler.setLevel(logging.INFO)
        consola_handler.setFormatter(formato)

        archivo_handler = RotatingFileHandler(
            "logs/sistema.log",
            maxBytes=5_000_000,
            backupCount=3,
            encoding="utf-8",
        )
        archivo_handler.setLevel(logging.DEBUG)
        archivo_handler.setFormatter(formato)

        logger.addHandler(consola_handler)
        logger.addHandler(archivo_handler)

    return logger


logger = obtener_logger("SoftwareFJ")

def obtener_logger(nombre_modulo: str) -> logging.Logger:
    """Configura los logger listo para validar cualquier registro."""

#Creacion de la clase abstracta cliente
class entidades(ABC):
    def__init__(self, id_entidad: str | None = None):
    self.id = str(id_entidad) if id_entidad else str (uuid.uuid4())
    self.fecha_creacion = datetime.now()
    self.fecha_actualizacion = None
    self.activo = True
    
def marcar_actualizado(self) -> None:
    self.fecha_actualizacion = datetime.now()
    
@abstractmethod
def obtener_informacion(self)-> str:
    pass
    
def es_validar(self)->bool:
    pass

import re
from abc import ABC, abstractmethod
class entidades(ABC):
    def__init__(self, identidades: str):
    self._id = id_entidades

@abstractmethod 
def obtener_informacion(self): -> str:
    pass

class cliente(entidades):
    def__init__(self, id_cliente:str,nombre:str,apellido:str,telefono:str,gmail:str | None = None,):
    super()._init_(id_cliente)
    #se ejecuta para modificar la clase con
@setter
self.nombre = nombre
self.apellido = apellido
self.telefono = telefono
self.direccion = direccion
self.gmail = gmail

#Validacion del nombre mediante encapsulación 
@property
def nombre(self)->str:
    return self._nombre
    
@nombre.setter
def nombre(self,valor:str)-> None:
    if not isintance(valor,str) or len(valor.strip())<6:
        raise ValueError("el nombre debe tener 6 caracteres.")
        self._nombre = valor.strip()
        self._marcar_actualizado()
        
#Validacion del apellido mediante la encapsulación 
@property
def apellido(self)->str:
    return self._apellido

@apellido.setter
def apellido(self,valor:str)-> None:
    if not isintance(valor,str) or len(valor.strip()) <5:
        raise ValueError("el apellido debe tener 5 caracteres.")
        self._apellido=valor.strip()
        self.marcar_actualizado()
        
#Validacion del telefono mediante la encapsulación 
    @property
def telefono(self)->str:
    return self._telefono
    
    @telefono.setter
def telefono(self,valor:str)-> None:
    if not isintance(valor,str) or not valor.strip().isdigit()ornot
        raise ValueError("el telefon debe tener 6 caracteres.")
        self._telefono = valor.strip()
        self.marcar_actualizado()

#Validacion del gmail mediante la encapsulación 
    @property
    def gmail(self) -> str:
        return self.__gmail

    @gmail.setter
    def gmail(self, valor: str):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise ValueError("El correo electrónico es inválido.")
        self.__gmail = valor.strip().lower()
        self.marcar_actualizado()
#Ejecucion de los metodos heredados
   def obtener_informacion(self) -> str:
        return (
            f"Cliente [{self.id}]: {self.nombre} {self.apellido} | "
            f"Correo: {self.email} | Teléfono: {self.telefono}"
               )
    
#Ejecucion del método abstracto
    def obtener_informacion(self) -> str:
        return f"Cliente: {self.__nombre} {self._apellido} | Correo: {self.__gmail} | Telefono: {self._telefono}"
        return all([
            boll.(self.id_entiades),
            boll.(self.nombre),
            boll.(self.apellido),
            boll.(self.telefono),
            boll.(self.gmail),
])

#Creacion de la clase abstracta servicio
class servicio(ABC):
    def __init__(self, id_servicio: int, nombre: str, precio: float, disponibilidad: bool,)-> None:
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
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise ValidacionEntidadError("La disponibilidad se define por ser booleano.")
        self._disponibilidad = estado
        self.marcar_actualizado()

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
        descuento = subtotal * (descuento_pct / 100)
        base_imponible = subtotal - descuento
        impuesto = base_imponible * (impuesto_pct / 100)
        return round(base_imponible + impuesto, 2)

    @abstractmethod
    def calcular_costo_total(self) -> float:
        """Método abstracto que las clases hijas deberán implementar."""
        pass
        
#Creacion de las clases hijas de servicio
Class servicio_seguridad(servicio):
def __init__(self, id_servicio: int | str, nombre: str, precio: float, cantidad_registroa: int = 1 disponibilidad: bool = True,
    ):
super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(cantidad_registros, int) or cantidad_registros <= 0:
            raise ValidacionEntidadError("La cantidad de registros debe ser un entero mayor a 0.")
        self.cantidad_registros = cantidad_registros

Class servicio_logistica(servicio):
def __init__(self, id_servicio: int | str, nombre: str,  precio: float, cantidad_mercancia: int = 2 disponibilidad: bool = True,
            ):
super().__init__(id_servicio, nombre, precio, disponibilidad)
         if not isinstance(cantidad_mercancia, int) or cantidad_mercancia <=0:
             raise ValidacionEntidadError("La cantidad de mercancia en la empresa deber ser mayor a 0.")
         self.cantidad_mercancia = cantidad_mercancia

Class servicio_mantenimiento(servicio):
def __init__(self, id_servicio: int | str, nombre: str,  precio: float, cantidad_fallos_electricos: int = 4 disponibilidad: bool = True,
            ):
super().__init__(id_servicio, nombre, precio, disponibilidad)
         if not isinstance(cantidad_fallos_electricos, int) or cantidad_fallos_electricos<=0:
             raise ValidacionEntidadError("La cantidad de fallos electricos en la empresa deber ser mayor a 0.")
         self.cantidad_fallos_electricos = cantidad_fallos_electricos

            
#Creacion de la clase reserva
Class reserva(Entidades):
    def __init__(self, cliente, servicio, duracion):
        super().__init__()

         
