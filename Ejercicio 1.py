#Creacion de las importaciones 
#alicacion de la libreria ABC par clases y métodos 
from abc import ABC, abstractmethod
#sirve para guardar los errores
import logging
#sirve para guardar los archivos
from logging.handlers import RotatingFileHandler
#sirve para guardar los loggs si no existen
import os
#sirve para guardar los correos
import re
#sirve para guardar los identificadores
import uuid
#sirve para guardar las fechas 
from datetime import datetime


#Creacion de las excepciones
#Creacion de la exception 
class ErrorBaseSistema(Exception):
#recibe un mensaje descriptivo o un código numérico
    def __init__(self, mensaje: str, codigo_error: int = 500):
#sirve para guardar el mensaje con instancia
        self.mensaje = mensaje
#sirve para guardar el código error 
        self.codigo_error = codigo_error
# sirve para el constructor de la clase padre
        super().__init__(self.mensaje)

#creacion de la execepcion cuando no se haya alguna de las clases (cliente,servicio y reserva)
class EntidadNoEncontradaError(ErrorBaseSistema):
    def __init__(self, entidad: str, id_entidad: str | int):
        mensaje = f"No se hallo la entidad '{entidad}' con el ID: {id_entidad}."
        super().__init__(mensaje, codigo_error=404)

class ValidacionEntidadError(ErrorBaseSistema):
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error=400)

class ServicioNoDisponibleError(ErrorBaseSistema):
    def __init__(self, nombre_servicio: str):
        mensaje = f"El servicio {nombre_servicio} no se encuentra disponible."
        super().__init__(mensaje, codigo_error=409)

class ReservaNoDisponibleError(ErrorBaseSistema):
    def __init__(self, nombre_reserva: str):
        mensaje = f"La Reseva{nombre_reserva} no se encuentra disponible."
        super().__init__(mensaje, codigo_error=500)
    
#Creacion de los loggers
def obtener_logger(nombre_modulo: str) -> logging.Logger:
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

#Creacion de la clase abstracta cliente
class entidades(ABC):
    def__init__(self, id_entidades: str | None = None):
    self.id = str(id_entidades) if id_entidades else str (uuid.uuid4())
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


class entidades(ABC):
    def__init__(self, id_entidades: str):
    self._id = id_entidades

@abstractmethod 
def obtener_informacion(self): -> str:
    pass

class cliente(entidades):
    def__init__(self, id_cliente:str,nombre:str,apellido:str,telefono:str,gmail:str | None = None,):
    super().__init__(id_cliente)
self.nombre = nombre
self.apellido = apellido
self.telefono = telefono
self.direccion = direccion
self.gmail = gmail
logger.info(f"Cliente registrado: {self.nombre} {self.apellido} (ID: {self.id})")

#Validacion del nombre mediante encapsulación 
@property
def nombre(self)->str:
    return self._nombre
    
@nombre.setter
def nombre(self,valor:str)-> None:
    if not isintance(valor,str) or len(valor.strip())<6:
        raise ValidacionEntidadError("el nombre debe tener 6 caracteres.")
        logger.error(mensaje)
        self._nombre = valor.strip()
        self._marcar_actualizado()
        
#Validacion del apellido mediante la encapsulación 
@property
def apellido(self)->str:
    return self._apellido

@apellido.setter
def apellido(self,valor:str)-> None:
    if not isintance(valor,str) or len(valor.strip()) <5:
        raise ValidacionEntidadError("el apellido debe tener 5 caracteres.")
        logger.error(mensaje)
        self._apellido=valor.strip()
        self.marcar_actualizado()
        
#Validacion del telefono mediante la encapsulación 
    @property
def telefono(self)->str:
    return self._telefono
    
    @telefono.setter
def telefono(self,valor:str)-> None:
    if not isintance(valor,str) or not valor.strip().isdigit()ornot
        raise ValidacionEntidadEror("el telefon debe tener 6 caracteres.")
        logger.error(mensaje)
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
            raise VallidacionEntidadEror("El correo electrónico es inválido.")
            logger.error(mensaje)
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
class servicio(entidades, ABC):
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
            mensaje = f"La tarifa debe ser mayor a 0. Valor recibido: {valor}"
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
            raise ValidacionEntidadError("La disponibilidad se determina por ser booleano.")
        self._disponibilidad = estado
        self.marcar_actualizado()

    def verificar_disponibilidad(self) -> None:
        if not self._disponibilidad or not self.activo:
            logger.warning(f"Intento de ingreso al servicio no disponible: {self._nombre}")
            raise ServicioNoDisponibleError(self._nombre)

    def aplicar_ajustes_costo(
        self,
        subtotal: float,
        impuesto_pct: float = 0.0,
        descuento_pct: float = 0.0,
    ) -> float:
        
#Ejecucion del metodo sobrecargado
if subtotal < 0 or impuesto_pct < 0 or descuento_pct < 0:
            mensaje = "El subtotal, impuesto y descuento no pueden ser negativos."
            logger.error(mensaje)
            raise ValidacionEntidadError(
        descuento = subtotal * (descuento_pct / 100)
        base_imponible = subtotal - descuento
        impuesto = base_imponible * (impuesto_pct / 100)
        return round(base_imponible + impuesto, 2)

    @abstractmethod
    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        pass
        
    @abstractmethod
    def validar_parametros(self, duracion_horas: int) -> None:
        pass
    def es_valido(self) -> bool:
        return bool(self._nombre) and self._precio > 0

        
#Creacion de las clases hijas de servicio
class ReservaSala(Servicio):
      def __init__(self,id_servicio: int | str, nombre: str,  precio: float, cantidad_auditorios: int = 1, disponibilidad: bool = True,) -> None:
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(cantidad_auditorios, int) or cantidad_auditorios <= 0:
            mensaje = "La cantidad de auditorios debe ser un entero mayor a 0."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.cantidad_auditorios = cantidad_auditorios
        logger.info(f"Servicio ReservaSala '{self.nombre}' creado con {self.cantidad_auditorios} auditorio(s).")

    def validar_parametros(self, duracion_horas: int) -> None:
        if duracion_horas > 12:
            raise ValidacionEntidadError("Los auditorios no pueden reservarse por 7 horas seguidas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        return round(self.precio * duracion_horas * self.cantidad_auditorios, 4)

    def obtener_informacion(self) -> str:
        return (
            f"Reserva de Sala [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Auditorios: {self.cantidad_auditorios} | "
            f"Disponible: {self.disponibilidad}"
)

class AlquilerEquipo(Servicio):
def __init__( self, id_servicio: int | str, nombre: str, precio: float cantidad_equipos: int = 1disponibilidad: bool = True, ) -> None:
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(cantidad_equipos, int) or cantidad_equipos <= 0:
            mensaje = "La cantidad de equipos a alquilar debe ser un entero mayor a 0."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.cantidad_equipos = cantidad_equipos
        logger.info(f"Servicio AlquilerEquipo '{self.nombre}' ha sido ejecutado correctamente.")

    def validar_parametros(self, duracion_horas: int) -> None:
         if duracion_horas < 2:
            raise ValidacionEntidadError("El alquiler de equipos requiere un mínimo de 2 horas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        self.validar_parsmetros(duracion_horas)
        seguro_equipo = 10000.0
        return round((self.precio * duracion_horas * self.cantidad_equipos) + seguro_equipo, 2)

    def obtener_informacion(self) -> str:
        """Metodo de poliformismo."""
        return (
            f"Alquiler de Equipos [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Equipos: {self.cantidad_equipos} | "
            f"Disponible: {self.disponibilidad}"
               )

class AsesoriaEspecializada(Servicio):
 def __init__( self,id_servicio: int | str,  nombre: str, precio: float,especialidad: str = "Desarrollo de Software", disponibilidad: bool = True, ) -> None:
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            mensaje = "La especialidad de la asesoría debe tener 3 caracteres."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.especialidad = especialidad.strip()
        logger.info(f"Servicio AsesoriaEspecializada '{self.nombre}' ha sido ejecutado correctamente.")

    def validar_parametros(self, duracion_horas: int) -> None:
        if duracion_horas <= 0:
            raise ValidacionEntidadError("La duración de la asesoría debe ser mayor a 0 horas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        return round(self.precio * duracion_horas, 2)

    def obtener_informacion(self) -> str:
        return (
            f"Asesoría Especializada [{self.id}]: {self.nombre} ({self.especialidad}) | "
            f"Tarifa/h: ${self.precio:,.2f} | Disponible: {self.disponibilidad}"
    )
        

#Creacion de la clase reserva
class Reserva(entidades):
    def __init__(self, in_entidades: str, clientes_obj : cliente, servicio: Servicio, duracion: int):
        super()._intit_(id_entidades)
        if duracion <=0:
            raise ReservaIncorrectaError("Duracion debe ser msyor a 0")
        self.cliente = clientes_obj
        self.sevicio = servicio
        self.duracion = duracion
        self. estado = "PENDIENTE"
        logger.info(f"Reserva {self._id}creada para{cliente_obj.nombre}")

    def obtener_informacion(self) -> str:
        return()
        f"Reserva  [{self.id}] - Cliente: {self.cliente.nombre} {self.cliente.apellido} |"
        f"Servicio: {self.servicio.obtener_informacion()} | Duracion: {self.duracion}h | Estado: {self.estado}"

    def es_validar(self) -> bool:
        return self.duracion > 0 and self.servicio.disponibilidad

    def confirmar(self):
        try:
            self.servicio.verificar_disponibilidad()
            self.servicio.validar_parametros(self.duracion)
        except (ServicioNoDisponibleError, ReservaIncorrectaError, ValidacionEntidadError) as e:
            logger.error(f"Resrva { self.id} fallo: {getattr(e, 'mensaje', e)}")
            raise ResrvaIncorrectaError(f"No se puedo confirmar {self._id}") from e
        else:
            self.estado == "CANCELADA"
            self._marcar_actualizado() 
            logger.info(f"Reserva {self._id} finaliza. Estado: {self.estado}")
            return True
        finally:
            print(f" -> Resserva {self._id} finalizada. Estado: {self.estado}")

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise ReservaIncorrectaError("Ya estaba reservada")    
        self.estado = "CANCELADA"
        self._marcar_actualizado()
        logger.warning(f"Resrva{self._id}cancelada")

class SistemaFJ:
    def __init__(self):   
      self.clientes: list[cliente] = []   
      self.sevicios: list[servicio] = []
      self.reservas: list[Reserva] = []

    def agregar_cliente(self, c: cliente):
        for ex in self.clientes:
            if ex._id == c._id or ex.gmail == c.gmail:
                raise ValidacionEntidadError(f"Cliente duplicado: {c.id}")
        self.clientes.append(c) 
        logger.info(f"Cliente agregado: {c.obtener_informacion()}")

    def buscar_cliente(self, gmail: str):
        for c in self.clientes:
            if c.gmail == gmail:
                return c
        raise EntidadNoEncontradaError("Cliente", gmail)

if __name__ == "__main__":
    sistema = SistemaFJ()
    print("SOFWARE FJ -  10 OPERACIONES - Sistema nunca cae")

    def ejecutar(num, desc, func):
        print(f"\n[OP {num}] {desc}")
        try:
            func()
        except ErrorBaseSistema as e:
            print(f"Controlado: {e.mensaje} Cod: {e.codigo_error} - sigue activo")
            logger.error(f"Op {num}: {e.mensaje}")
        except Exception as e:   
            print(f"Inesperado: {e}")
        else:
            print(f"Exito")
        finally:
            print("Sistema estable...")

# OJO: nombre 6 letras, apellido 5, telefono 6, gmailcon @ - si no, falla a proposito
ejecutar(1, "Cliente Valido", lambda: sistema.agregar_cliente(cliente("101","Laura","Perezs","300123","laura@mail.com", "Calle 10")))
ejecutar(2, "Cliente inválido correo", lambda: sistema.agregar_cliente(cliente("102", "Al", "Ruiz", "300", "correo-malo")))
ejecutar(3, "Cliente válido 2", lambda: sistema.agregar_cliente(cliente("103", "Carlos", "Ruizzz", "310987", "carlos@mail.com")))
ejecutar(4, "Cliente duplicado", lambda: sistema.agregar_cliente(cliente("101", "Lauras", "Perezs", "300123", "laura@mail.com")))
ejecutar(5, "Sala OK 2 auditorios", lambda: sistema.servicios.append(ReservaSala(1, "Sala Juntas", 50000, 2)))
ejecutar(6, "Equipo OK 3 equipos + seguro 10000", lambda: sistema.servicios.append(AlquilerEquipo(2, "Video Beam", 20000, 3)))
ejecutar(7, "Asesoría Especializada + total 1.5x", lambda: print("Total:", AsesoriaEspecializada(3, "Asesoría FJ", 80000, "Desarrollo de Software").calcular_costo_total(2)))
ejecutar(8, "Reserva exitosa Sala 3h", lambda: Reserva("R001", sistema.clientes[0], sistema.servicios[0], 3).confirmar())
ejecutar(9, "Reserva fallida Equipo 1h - minimo 2h", lambda: Reserva("R002", sistema.clientes[0], sistema.servicios[1], 1).confirmar())
ejecutar(10, "Buscar inexistente", lambda: sistema.buscar_cliente("no@mail.com"))

print(f"\nFIN: {len(sistema.clientes)} clientes | {len(sistema.servicios)} servicios")         
