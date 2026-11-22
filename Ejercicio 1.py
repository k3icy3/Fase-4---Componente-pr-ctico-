#Creacion de las importaciones 
#aplicacion de la libreria ABC par clases y métodos 
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
class ErrorBaseSistema(Exception):
    #sirve para recibirun mensaje descriptivo o un código numérico
    def __init__(self, mensaje: str, codigo_error: int = 500):
        #sirve para guardar el mensaje con instancia
        self.mensaje = mensaje
        #sirve para guardar el código error 
        self.codigo_error = codigo_error
        # sirve para el constructor de la clase padre
        super().__init__(self.mensaje)

#creacion de la execepcion cuando no se haya alguna de las clases (cliente,servicio y reserva)
class EntidadNoEncontradaError(ErrorBaseSistema):
    #sirve para construir el nombre para la entidad y el identificador
    def __init__(self, entidad: str, id_entidad: str | int):
        #sirve para hallar el error de identidad no encontrado
        mensaje = f"No se hallo la entidad '{entidad}' con el ID: {id_entidad}."
        #sirve para iniciar la clase 404
        super().__init__(mensaje, codigo_error=404)

#creación de la excepción para los datos de entrada
class ValidacionEntidadError(ErrorBaseSistema):
    #sirve para construir el dato del error para validar
    def __init__(self, mensaje: str):
    #sirve para iniciar la clase 400
        super().__init__(mensaje, codigo_error=400)

#creación de la excepción cuando un servicio no está disponible
class ServicioNoDisponibleError(ErrorBaseSistema):
    #sirve para construir el nombre de servicio
    def __init__(self, nombre_servicio: str):
    #sirve para el mensaje de no disponibilidad
        mensaje = f"El servicio {nombre_servicio} no se encuentra disponible."
    #sirve para iniciar la clase 409
        super().__init__(mensaje, codigo_error=409)

#creación de la excepción para los parámetros y reserva
class ReservaNoDisponibleError(ErrorBaseSistema):
    #sirve para construir el error de reserva
    def __init__(self, mensaje: str):
    #sirve para el mensaje de error de reserva
        mensaje = f"La Reseva{nombre_reserva} no se encuentra disponible."
    #sirve para iniciar la clase 500
        super().__init__(mensaje, codigo_error=500)
    
#Creacion de los loggers
def obtener_logger(nombre_modulo: str) -> logging.Logger:
    #sirve para crear las carpetas logs si no existe
    os.makedirs("logs", exist_ok=True)
    #sirve para guardar obtener la instancia
    logger = logging.getLogger(nombre_modulo)
    #sirve para definir el nivel debug en captura 
    logger.setLevel(logging.DEBUG)
    #sirve para evitar los logs duplicados
    if not logger.handlers:
    #sirve para mostrar el formato de salida de log
        formato = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        #sirve para crear el manejador en consola
        consola_handler = logging.StreamHandler()
        #sirve para demostrar el nivel info
        consola_handler.setLevel(logging.INFO)
        #sirve para manejar el formato a consola
        consola_handler.setFormatter(formato)
        #sirve para crear el manejador de logs
        archivo_handler = RotatingFileHandler(
            "logs/sistema.log",
            maxBytes=8_000_000,
            backupCount=6,
            encoding="utf-8",
        )
        #sirve para guardar los archivos debug
        archivo_handler.setLevel(logging.DEBUG)
        #sirve para manejar el formato archivo
        archivo_handler.setFormatter(formato)
        #sirve para manejar por consola el logger
        logger.addHandler(consola_handler)
        #sirve para manejar el archivo logger
        logger.addHandler(archivo_handler)
    #sirve para retornar el logger
    return logger
#sirve para iniciar el logger para todo el software FJ
logger = obtener_logger("SoftwareFJ")

#Creacion de la clase abstracta 
class entidades(ABC):
#sirve para la creación del id
    def __init__(self, id_entidades: str | None = None):
    #sirve para enviar el id en texto o este mismo genera uuid
    self.id = str(id_entidades) if id_entidades else str(uuid.uuid4())
    #sirve para guardar la fecha
    self.fecha_creacion = datetime.now()
    #sirve para iniciar la fecha con None
    self.fecha_actualizacion = None
    #sirve para que la entidad esté activa
    self.activo = True
    
#sirve para la propiedad de lectura para consultar el ID encapsulado
    @property
    def id(self) -> str:
#sirve para retornar el identificador 
        return self._id

#método de actualizar la fecha
def marcar_actualizado(self) -> None:
#sirve para asignar la fecha
    self.fecha_actualizacion = datetime.now()
    
#método abstracto para escribir la identidad
@abstractmethod
def obtener_informacion(self) -> str:
    pass
#método abstracto para validar la integridad
@abstractmethod
def es_validar(self) -> bool:
    pass

#creacion de la clase hija cliente
class cliente(entidades):
#sirve para constructor del cliente con validación
    def __init__(self, id_cliente: str, nombre: str, apellido: str, telefono: str, gmail: str, direccion: str = ""):
    #sirve para llamar al constructor de entidades
    super().__init__(id_cliente)
    #sirve para asignar y validar el nombre,apellido,telefono,direccion,gmail
self.nombre = nombre
self.apellido = apellido
self.telefono = telefono
self.direccion = direccion
self.gmail = gmail
#sirve para registrar el evento con log
logger.info(f"Cliente registrado: {self.nombre} {self.apellido} (ID: {self.id})")

#Validacion del nombre mediante encapsulación con getter
@property
def nombre(self) -> str:
    #sirve para retornar el nombre
    return self._nombre
    
#validación del nombre mediante encapsulación con setter
@nombre.setter
def nombre(self,valor:str)-> None:
    #sirve para validar el nombre que contenga sus 6 caracteres
    if not isintance(valor, str) or len(valor.strip())<6:
        #sirve para guardar el error dentro del log
        logger.error(mensaje
        #sirve para guardar el mensaje de error
        raise ValidacionEntidadError("el nombre debe tener 6 caracteres.")
        #sirve para guardar el nombre
        self._nombre = valor.strip()
        #sirve para actualizar la fecha
        self._marcar_actualizado()
        
#Validacion del apellido mediante la encapsulación con getter
@property
def apellido(self) -> str:
    #sirve para retornar el apellido
    return self._apellido
    
#validación del apellido mediante la cancelación con setter
@apellido.setter
def apellido(self, valor: str) -> None:
    #sirve para validar el apellido que contenga seis caracteres
    if not isintance(valor,str) or len(valor.strip()) <5:
        #sirve para definir el mensaje de error dentro del log
        mensaje = "el apellido debe tener 5 caracteres.")
        #sirve para guardar el error en el log
        logger.error(mensaje)
        #sirve para guardar alguna excepción de validación
        raise ValidacioEntidadError(mensaje)
        #sirve para guardar el apellido
        self._apellido = valor.strip()
        #sirve para actualizar la fecha
        self.marcar_actualizado()
        
#Validacion del telefono mediante la encapsulación getter
    @property
def telefono(self) -> str:
    #sirve para retornar el teléfono
    return self._telefono
    
#validación del teléfono mediante la encapsulación setter
    @telefono.setter
def telefono(self, valor: str)-> None:
    #sirve para validar que el teléfono tenga seis dígitos
    if not isintance(valor,str) or not valor.strip().isdigit() or len(valor.strip()) <7:
    #sirve para definir el mensaje error 
    mensaje = "el teléfono debe 7 dígitos."
        raise ValidacionEntidadEror("el telefono debe tener 7 digitoss.")
        #sirve para guardar el error dentro del log
        logger.error(mensaje)
        #sirve para guardar el teléfono
        self._telefono = valor.strip()
        #sirve para actualizar la fecha
        self.marcar_actualizado()

#Validacion del gmail mediante la encapsulación getter
    @property
    def gmail(self) -> str:
        #sirve para retornar el correo
        return self.__gmail
        
#validación del gmail mediante la encapsulación setter
    @gmail.setter
    def gmail(self, valor: str): -> None
        #sirve para definir la expresión del correo
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        #sirve para validar el formato del correo
        if not isinstance(valor, str) or not re.match(patron, valor.strip()):
            #sirve para definir el mensaje error 
            mensaje = "el correo electrónico es inválido."
            #sirve para guardar el mensaje de error 
            logger.error(mensaje)
            #sirve para escribir la excepción de validación 
            raise VallidacionEntidadEror("El correo electrónico es inválido.")
         #sirve para guardar el gmail
        self.__gmail = valor.strip().lower()
        #sirve para actualizar la fecha
        self.marcar_actualizado()
        
#Ejecucion de los metodos heredados con obtener_informacion
   def obtener_informacion(self) -> str:
       #sirve para retornar la cadena de los datos del cliente
        return (
            f"Cliente [{self.id}]: {self.nombre} {self.apellido} | "
            f"Correo: {self.email} | Teléfono: {self.telefono}"
               )
    
#Ejecucion del método abstracto de es_validar
    def es_validar(self) -> bool:
        #sirve para comprobar los campos
        return all([
            boll.(self.id),
            boll.(self.nombre),
            boll.(self.apellido),
            boll.(self.telefono),
            boll.(self.gmail),
])

#Creacion de la clase abstracta servicio
class servicio(entidades, ABC):
#sirve para construir servicio 
    def __init__(self, id_servicio: int | str, nombre: str, precio: float, disponibilidad: bool = True) -> None:
        #sirve para llamar al constructor padre
        super().__init__(id_servicio)
        #sirve para asignar los atributos
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad 
        
#validación del nombre mediante la encapsulación getter
    @property
    def nombre(self) -> str:
        #sirve para retornar el nombre del servicio
        return self._nombre
        
#validación del nombre mediante la encápsulación settee
    @nombre.setter
    def nombre(self, valor: str) -> None:
        #sirve para validar que el nombre tenga tres caracteres
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            #sirve para definir el mensaje error 
            mensaje = "el servicio de tener tres caracteres"
            #sirve para registrar el error dentro del log
            logger.error(mensaje)
            #sirve para agregar la excepción de validación
            raise ValidacionEntidadError(mensaje)
        #sirve para guardar el nombre del servicio
        self._nombre = valor.strip()
        #sirve para actualizar la fecha
        self.marcar_actualizado()
        
#validación de precio mediante la encapsulación getter
     @property
       def precio(self) -> float:
        #sirve para retornar el precio
        return self._precio
           
#validación de precio mediante la encapsulación setter
    @precio.setter
    def precio(self, valor: float) -> None:
        #sirve para validar su tarifa positiva
        if not isinstance(valor, (int, float)) or valor <= 0:
            #sirve para definir el mensaje error
            mensaje = f"La tarifa debe ser mayor a 0. Valor recibido: {valor}"
            #sirve para registrar el error
            logger.error(mensaje)
            #sirve para generar la excepción de validación
            raise ValidacionEntidadError(mensaje)
        #sirve para guardar el precio
        self._precio = float(valor)
        #sirve para actualizar la fecha
        self.marcar_actualizado()

#validación de la disponibilidad mediante la encapsulación getter
        @property
    def disponibilidad(self) -> bool:
        #sirve para retornar la disponibilidad
        return self._disponibilidad
        
#validación de la disponibilidad mediante la encapsulación setter
    @disponibilidad.setter
    def disponibilidad(self, estado: bool) -> None:
        #sirve para validar la disponibilidad
        if not isinstance(estado, bool):
            #sirve para generar la excepción de validación
            raise ValidacionEntidadError("La disponibilidad se determina por ser booleano.")
        #sirve para guardar la disponibilidad
        self._disponibilidad = estado
        #sirve para actualizar la fecha
        self.marcar_actualizado()
        
#verificación del servicio si está disponible
    def verificar_disponibilidad(self) -> None:
        #sirve para comprobar la disponibilidad
        if not self._disponibilidad or not self.activo:
            #sirve para registrar la advertencia
            logger.warning(f"Intento de ingreso al servicio no disponible: {self._nombre}")
            #sirve para generar la excepción del servicio no disponible
            raise ServicioNoDisponibleError(self._nombre)
            
#aplicación de los ajustes de costo
    def aplicar_ajustes_costo(
        self,
        subtotal: float,
        impuesto_pct: float = 0.0,
        descuento_pct: float = 0.0,
    ) -> float:
        
#Ejecucion del metodo sobrecargado
if subtotal < 0 or impuesto_pct < 0 or descuento_pct < 0:
            #sirve para definir el mensaje de error
            mensaje = "El subtotal, impuesto y descuento no pueden ser negativos."
            #sirve para registrar el error
            logger.error(mensaje)
            raise ValidacionEntidadError(
        #sirve para calcular el descuento
        descuento = subtotal * (descuento_pct / 100)
        #sirve para restar el subtotal del descuento
        base_imponible = subtotal - descuento
        #sirve para calcular el impuesto imponible
        impuesto = base_imponible * (impuesto_pct / 100)
        #sirve para retornar el redondeo a dos decimales
        return round(base_imponible + impuesto, 2)

    #metodo abstracto para calcular el costo
    @abstractmethod
    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        pass
    #método abstracto para evaluar la duración de cada servicio
    @abstractmethod
    def validar_parametros(self, duracion_horas: int) -> None:
        pass
    #Inclusion del metodo abstracto es_validar
    def es_validar(self) -> bool:
        return bool(self._nombre) and self._precio > 0

        
#Creacion de la clase hija reserva sala de servicio
class ReservaSala(Servicio):
      #sirve para construir la cantidad de auditorios
      def __init__(self,id_servicio: int | str, nombre: str,  precio: float, cantidad_auditorios: int = 1, disponibilidad: bool = True,) -> None:
      #sirve para llamar el constructor de servicio 
        super().__init__(id_servicio, nombre, precio, disponibilidad)
      #sirve para validar la cantidad de auditorios
        if not isinstance(cantidad_auditorios, int) or cantidad_auditorios <= 0:
            mensaje = "La cantidad de auditorios debe ser un entero mayor a 0."
            #sirve para definir el mensaje error
            logger.error(mensaje)
            #sirve para generar la excepción de validación
            raise ValidacionEntidadError(mensaje)
        #sirve para guardar la cantidad de auditorios
        self.cantidad_auditorios = cantidad_auditorios
        #sirve para registrar la creación dentro del log
        logger.info(f"Servicio ReservaSala '{self.nombre}' creado con {self.cantidad_auditorios} auditorio(s).")
          
    #sirve para validar la duración en los auditorios mediante el poliformismo
    def validar_parametros(self, duracion_horas: int) -> None:
        #sirve para comprobar la duración entre las horas
        if duracion_horas > 10:
            #sirve parael precio en las horas de los auditorios
            raise ValidacionEntidadError("Los auditorios deben reservarse entre 1 y 10 horas seguidas.")
            
    #sirve para calcular el costo por hora mediante el poliformismo
    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        #sirve para retornar el precio por horas de los auditorios
        return round(self.precio * duracion_horas * self.cantidad_auditorios, 2)
        
    #sirve para escribir el servicio reserva sala
    def obtener_informacion(self) -> str:
        #sirve para retornar la información de sala
        return (
            f"Reserva de Sala [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Auditorios: {self.cantidad_auditorios} | "
            f"Disponible: {self.disponibilidad}"
            )
        
#creación de la clase hija alquiler de equipo de servicio
class AlquilerEquipo(Servicio):
#sirve para construir la cantidad de equipos
def __init__( self, id_servicio: int | str, nombre: str, precio: float cantidad_equipos: int = 1disponibilidad: bool = True, ) -> None:
        #sirve para llamar al constructor de servicio
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        #sirve para validar la cantidad de equipos
        if not isinstance(cantidad_equipos, int) or cantidad_equipos <= 0:
            #sirve para definir el mensaje error
            mensaje = "La cantidad de equipos a alquilar debe ser un entero mayor a 0."
            #sirve para registrar el error dentro del log
            logger.error(mensaje)
            #sirve para agregar la excepción de validación
            raise ValidacionEntidadError(mensaje)
        #sirve para guardar la cantidad de equipos
        self.cantidad_equipos = cantidad_equipos
        #sirve para registrar la creación del log
        logger.info(f"Servicio AlquilerEquipo '{self.nombre}' ha sido ejecutado correctamente.")

    #sirve para validar mínimo dos horas para alquilar equipos mediante el poliformismo
    def validar_parametros(self, duracion_horas: int) -> None:
        #sirve para verificar el alquiler en menos de tres horas
         if duracion_horas < 3:
             #sirve para agregar error si es menor a  tres horas
            raise ValidacionEntidadError("El alquiler de equipos requiere un mínimo de 3 horas.")
             
    #sirve para calcular el costo por hora más seguro de prestación de equipo
    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        #sirve para validar los parámetros de duración
        self.validar_parametros(duracion_horas)
        #sirve para definir el costo fijo
        seguro_equipo = 15000.0
        #sirve para retornar el costo total del equipo
        return round((self.precio * duracion_horas * self.cantidad_equipos) + seguro_equipo, 2)
        
    #sirve para escribir el servicio de alquiler equipos 
    def obtener_informacion(self) -> str:
        #sirve para retornar la información del alquiler
        return (
            f"Alquiler de Equipos [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Equipos: {self.cantidad_equipos} | "
            f"Disponible: {self.disponibilidad}"
               )
        
#creación de la clase hija asesoría especializada de servicio
class AsesoriaEspecializada(Servicio):
#sirve para construir la especialidad tecnica
 def __init__( self,id_servicio: int | str,  nombre: str, precio: float,especialidad: str = "Desarrollo de Software", disponibilidad: bool = True, ) -> None:
#sirve para llamar al constructor de servicio
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        #sirve para validar el nombre de la especialidad
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            #sirve para definir el mensaje error
            mensaje = "La especialidad de la asesoría debe tener 3 caracteres."
            #sirve para registrar el error dentro del log
            logger.error(mensaje)
            #sirve para generar la excepción de validación
            raise ValidacionEntidadError(mensaje)
        #sirve para guardar la especialidad
        self.especialidad = especialidad.strip()
        #sirve para registrar la creación del log
        logger.info(f"Servicio AsesoriaEspecializada '{self.nombre}' ha sido ejecutado correctamente.")
     
    #sirve para validar la la duración mayor a cero horas mediante el poliformismo
    def validar_parametros(self, duracion_horas: int) -> None:
        #sirve para comprobar las horas mayores a cero
        if duracion_horas <= 0:
            #sirve para generar una excepción de validación 
            raise ValidacionEntidadError("La duración de la asesoría debe ser mayor a 0 horas.")
            
    #sirve para calcular el costo total de la especialidad con 1.8x
    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        #sirve para retornar el multiplicado
        return round(self.precio * duracion_horas, * 1.8, 2)
    #sirve para escribir el servicio asesoría especializada
        
    def obtener_informacion(self) -> str:
        #sirve para retornar la información de asesoría
        return (
            f"Asesoría Especializada [{self.id}]: {self.nombre} ({self.especialidad}) | "
            f"Tarifa/h: ${self.precio:,.2f} | Disponible: {self.disponibilidad}"
    )
        

#Creacion de la clase reserva
class Reserva(entidades):
    #sirve para construir la reserva con el cliente servicio y duración
    def __init__(self, in_entidades: str, clientes_obj : cliente, servicio: Servicio, duracion: int):
        #sirve para iniciar la clase padre entidades 
        super()._intit_(id_entidades)
        #sirve para validar la duración
        if duracion <=0:
            #sirve para generar error si la oración es inválida
            raise ReservaIncorrectaError("Duracion debe ser msyor a 0")
        self.cliente = clientes_obj
        self.sevicio = servicio
        self.duracion = duracion
        self. estado = "PENDIENTE"
        #sirve para registrar la creación dentro del log
        logger.info(f"Reserva {self._id}creada para{cliente_obj.nombre}")

    #sirve para retornar los datos de la reserva
    def obtener_informacion(self) -> str:
        #sirve para formatear la descripción de reserva
        return()
        f"Reserva  [{self.id}] - Cliente: {self.cliente.nombre} {self.cliente.apellido} |"
        f"Servicio: {self.servicio.obtener_informacion()} | Duracion: {self.duracion}h | Estado: {self.estado}"
    #sirve para verificar la reserva si cumple sus funciones
    def es_validar(self) -> bool:
        #sirve para retornar su duración y su servicio disponible
        return self.duracion > 0 and self.servicio.disponibilidad

    #sirve para confirmar la reserva usada a través de las excepciones
    def confirmar(self):
        #sirve para intentar la validación la disponibilidad y parámetros
        try:
            #sirve para validar si el servicio está disponible
            self.servicio.verificar_disponibilidad()
            #sirve para validar las reglas del servicio
            self.servicio.validar_parametros(self.duracion)
        #sirve para capturar las excepciones y encadenarlas
        except (ServicioNoDisponibleError, ReservaIncorrectaError, ValidacionEntidadError) as e:
            #sirve para registrar el fallo dentro log
            logger.error(f"Resrva { self.id} fallo: {getattr(e, 'mensaje', e)}")
            #sirve para encadenar la excepción
            raise ResrvaIncorrectaError(f"No se puedo confirmar {self._id}") from e

        #sirve para confirmar la reserva
        else:
            #sirve para cambiar el estado
            self.estado == "CANCELADA"
            #sirve para actualizar la fecha
            self._marcar_actualizado() 
            #sirve para registrar el log
            logger.info(f"Reserva {self._id} finaliza. Estado: {self.estado}")
            #sirve para retornar el true
            return True
        #sirve para ejecutar el cierre del procedimiento
        finally:
            #sirve para imprimir el estado
            print(f" -> Resserva {self._id} finalizada. Estado: {self.estado}")

    #sirve para cancelar una reserva
    def cancelar(self):
        #sirve para verificar si está cancelada
        if self.estado == "CANCELADA":
            #sirve para generar error si ya está cancelada
            raise ReservaIncorrectaError("Ya estaba reservada")  
        #sirve para cambiar el estado de cancelar
        self.estado = "CANCELADA"
        #sirve para actualizar la fecha
        self._marcar_actualizado()
        #sirve para registrar la advertencia
        logger.warning(f"Resrva{self._id}cancelada")

#sirve para gestionar clientes servicios y reservas
class SistemaFJ:
    #sirve para iniciar las listas internas
    def __init__(self):   
      #sirve para crear las listas de clientes, servicios y reservad
      self.clientes: list[cliente] = []   
      self.sevicios: list[servicio] = []
      self.reservas: list[Reserva] = []

    #sirve para agregar un cliente que no esté duplicado
    def agregar_cliente(self, c: cliente):
        #sirve para recorrer la lista de cliente que ya existen
        for ex in self.clientes:
            #sirve para comprobar el ID o el Gmail g ya existe
            if ex._id == c._id or ex.gmail == c.gmail:
                #sirve para generar la excepción por existir un cliente duplicado
                raise ValidacionEntidadError(f"Cliente duplicado: {c.id}")
        #sirve para agregar el cliente válido hacia la lista
        self.clientes.append(c) 
        #sirve para registrar el log un cliente agregado
        logger.info(f"Cliente agregado: {c.obtener_informacion()}")

    #sirve para buscar un cliente por su correo
    def buscar_cliente(self, gmail: str):
        #sirve para recorrer la lista de los clientes
        for c in self.clientes:
            #sirve para comparar el correo
            if c.gmail == gmail:
                #sirve para retornar el cliente
                return c
        #sirve para lanzar la excepción hacia el cliente que tal vez no existe
        raise EntidadNoEncontradaError("Cliente", gmail)
        
#Ejecucion de las 10 operaciones de prueba en el sistema
if __name__ == "__main__":
    #sirva para distanciar el sistema software FJ 
    sistema = SistemaFJ()
    #sirve para imprimir el encabezado
    print("SOFWARE FJ -  10 OPERACIONES - Sistema nunca cae")

    #sirve para ejecutar cada operación evitando tantos errores
    def ejecutar(num, desc, func):
        #sirve para imprimir el número y la descripción de esta operación
        print(f"\n[OP {num}] {desc}")
        #sirve para intentar ejecutar la función
        try:
            func()
        #sirve para capturar las excepciones
        except ErrorBaseSistema as e:
            #sirve para mostrar el error controlado
            print(f"Controlado: {e.mensaje} Cod: {e.codigo_error} - sigue activo")
            #sirve para registrar el archivo logs
            logger.error(f"Op {num}: {e.mensaje}")
        #sirve para capturar cualquier error inesperado 
        except Exception as e:   
            #sirve para imprimir este error
            print(f"Inesperado: {e}")
        #sirve para informar la operación cuando sea exitosa
        else:
            #sirve para imprimir el mensaje
            print(f"Exito")
        #sirve para confirmar el sistema tras cada operación
        finally:
            #sirve para imprimir el estado continuo
            print("Sistema estable...")

# OJO: nombre 6 letras, apellido 5, telefono 6, gmailcon @ - si no, falla a proposito
#ejecución de la operación registro de cliente válido
ejecutar(1, "Cliente Valido", lambda: sistema.agregar_cliente(cliente("101","Laura","Perezs","3001234","laura@mail.com", "Calle 10")))
#ejecución de la operación para el registro de cliente de datos inválido
ejecutar(2, "Cliente inválido correo", lambda: sistema.agregar_cliente(cliente("102", "Al", "Ruiz", "300", "correo-malo")))
#ejecución de la operación de registro de de cliente válido
ejecutar(3, "Cliente válido 2", lambda: sistema.agregar_cliente(cliente("103", "Carlos", "Ruizzz", "3109876", "carlos@mail.com")))
#ejecución de la operación para el registro del cliente duplicado
ejecutar(4, "Cliente duplicado", lambda: sistema.agregar_cliente(cliente("101", "Lauras", "Perezs", "3001234", "laura@mail.com")))
#ejecución de la operación para la creación válida de un servicio reserva sala
ejecutar(5, "Sala OK 2 auditorios", lambda: sistema.servicios.append(ReservaSala(1, "Sala Juntas", 50000, 2)))
#ejecución de la operación para la creación válida de un servicio de alquiler equipo
ejecutar(6, "Equipo OK 3 equipos + seguro 20000", lambda: sistema.servicios.append(AlquilerEquipo(2, "Video Beam", 20000, 3)))
#ejecución de la operación para hallar el cálculo de una asesoría especializada
ejecutar(7, "Asesoría Especializada + total 1.5x", lambda: print("Total:", AsesoriaEspecializada(3, "Asesoría FJ", 80000, "Desarrollo de Software").calcular_costo_total(2)))
#ejecución de la operación para hacer una reserva exitosa de sala por 3 horas
ejecutar(8, "Reserva exitosa Sala 3h", lambda: Reserva("R001", sistema.clientes[0], sistema.servicios[0], 3).confirmar())
#ejecución de la operación para una reserva fallida de equipo por no cumplir con un mínimo de 2 horas 
ejecutar(9, "Reserva fallida Equipo 1h - minimo 2h", lambda: Reserva("R002", sistema.clientes[0], sistema.servicios[1], 1).confirmar())
#ejecución de la operación de búsqueda para un cliente inexistente
ejecutar(10, "Buscar inexistente", lambda: sistema.buscar_cliente("no@mail.com"))
#ejecución para imprimir un resumen final de clientes y servicios dentro de la memoria del sistema
print(f"\nFIN: {len(sistema.clientes)} clientes | {len(sistema.servicios)} servicios")         
