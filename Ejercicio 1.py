# ==================================================
# CREACIÓN DE LAS IMPORTACIONES
# ==================================================
from abc import ABC, abstractmethod
import logging
from logging.handlers import RotatingFileHandler
import os
import re
import uuid
from datetime import datetime


# ==================================================
# CREACIÓN DE LAS EXCEPCIONES
# ==================================================
class ErrorBaseSistema(Exception):
    def __init__(self, mensaje: str, codigo_error: int = 500):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)


class EntidadNoEncontradaError(ErrorBaseSistema):
    def __init__(self, entidad: str, id_entidad: str | int):
        mensaje = f"No se halló la entidad '{entidad}' con el ID: {id_entidad}."
        super().__init__(mensaje, codigo_error=404)


class ValidacionEntidadError(ErrorBaseSistema):
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error=400)


class ServicioNoDisponibleError(ErrorBaseSistema):
    def __init__(self, nombre_servicio: str):
        mensaje = f"El servicio '{nombre_servicio}' no se encuentra disponible."
        super().__init__(mensaje, codigo_error=409)


class ReservaNoDisponibleError(ErrorBaseSistema):
    def __init__(self, nombre_reserva: str):
        mensaje = f"La Reserva '{nombre_reserva}' no se encuentra disponible."
        super().__init__(mensaje, codigo_error=500)


class ReservaIncorrectaError(ErrorBaseSistema):
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error=400)


# ==================================================
# CONFIGURACIÓN DE LOS LOGS
# ==================================================
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
            maxBytes=8_000_000,
            backupCount=6,
            encoding="utf-8",
        )
        archivo_handler.setLevel(logging.DEBUG)
        archivo_handler.setFormatter(formato)
        logger.addHandler(consola_handler)
        logger.addHandler(archivo_handler)
    return logger


logger = obtener_logger("SoftwareFJ")


# ==================================================
# CLASE ABSTRACTA BASE
# ==================================================
class Entidades(ABC):
    def __init__(self, id_entidades: str | None = None):
        self._id = str(id_entidades) if id_entidades else str(uuid.uuid4())
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = None
        self.activo = True

    @property
    def id(self) -> str:
        return self._id

    def marcar_actualizado(self) -> None:
        self.fecha_actualizacion = datetime.now()

    @abstractmethod
    def obtener_informacion(self) -> str:
        pass

    @abstractmethod
    def es_validar(self) -> bool:
        pass


# ==================================================
# CLASE CLIENTE
# ==================================================
class Cliente(Entidades):
    def __init__(self, id_cliente: str | None, nombre: str, apellido: str, telefono: str, gmail: str, direccion: str = ""):
        super().__init__(id_cliente)
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.gmail = gmail
        logger.info(f"Cliente registrado: {self.nombre} {self.apellido} (ID: {self.id})")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 6:
            mensaje = "El nombre debe tener al menos 6 caracteres."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self._nombre = valor.strip()
        self.marcar_actualizado()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            mensaje = "El apellido debe tener al menos 5 caracteres."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self._apellido = valor.strip()
        self.marcar_actualizado()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip().isdigit() or len(valor.strip()) < 7:
            mensaje = "El teléfono debe tener al menos 7 dígitos."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self._telefono = valor.strip()
        self.marcar_actualizado()

    @property
    def gmail(self) -> str:
        return self.__gmail

    @gmail.setter
    def gmail(self, valor: str) -> None:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(valor, str) or not re.match(patron, valor.strip()):
            mensaje = "El correo electrónico es inválido."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.__gmail = valor.strip().lower()
        self.marcar_actualizado()

    def obtener_informacion(self) -> str:
        return (
            f"Cliente [{self.id}]: {self.nombre} {self.apellido} | "
            f"Dirección: {self.direccion} | Correo: {self.gmail} | Teléfono: {self.telefono}"
        )

    def es_validar(self) -> bool:
        return all([bool(self.id), bool(self.nombre), bool(self.apellido), bool(self.telefono), bool(self.gmail)])


# ==================================================
# CLASE ABSTRACTA SERVICIO
# ==================================================
class Servicio(Entidades, ABC):
    def __init__(self, id_servicio: int | str | None, nombre: str, precio: float, disponibilidad: bool = True):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            mensaje = "El nombre del servicio debe tener al menos 3 caracteres."
            logger.error(mensaje)
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
        self.marcar_actualizado()

    @property
    def disponibilidad(self) -> bool:
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            mensaje = "La disponibilidad se determina con un valor booleano."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self._disponibilidad = estado
        self.marcar_actualizado()

    def verificar_disponibilidad(self) -> None:
        if not self._disponibilidad or not self.activo:
            logger.warning(f"Intento de acceso a servicio no disponible: {self._nombre}")
            raise ServicioNoDisponibleError(self._nombre)

    def aplicar_ajustes_costo(self, subtotal: float, impuesto_pct: float = 0.0, descuento_pct: float = 0.0) -> float:
        if subtotal < 0 or impuesto_pct < 0 or descuento_pct < 0:
            mensaje = "El subtotal, impuesto y descuento no pueden ser negativos."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
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

    def es_validar(self) -> bool:
        return bool(self._nombre) and self._precio > 0


# ==================================================
# CLASES HIJAS DE SERVICIO
# ==================================================
class ReservaSala(Servicio):
    def __init__(self, id_servicio: int | str | None, nombre: str, precio: float, cantidad_auditorios: int = 1, disponibilidad: bool = True):
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(cantidad_auditorios, int) or cantidad_auditorios <= 0:
            mensaje = "La cantidad de auditorios debe ser un entero mayor a 0."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.cantidad_auditorios = cantidad_auditorios
        logger.info(f"Servicio ReservaSala '{self.nombre}' creado con {self.cantidad_auditorios} auditorio(s).")

    def validar_parametros(self, duracion_horas: int) -> None:
        if duracion_horas > 10:
            raise ValidacionEntidadError("Los auditorios deben reservarse entre 1 y 10 horas seguidas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        return round(self.precio * duracion_horas * self.cantidad_auditorios, 2)

    def obtener_informacion(self) -> str:
        return (
            f"Reserva de Sala [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Auditorios: {self.cantidad_auditorios} | "
            f"Disponible: {self.disponibilidad}"
        )


class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio: int | str | None, nombre: str, precio: float, cantidad_equipos: int = 1, disponibilidad: bool = True):
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(cantidad_equipos, int) or cantidad_equipos <= 0:
            mensaje = "La cantidad de equipos a alquilar debe ser un entero mayor a 0."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.cantidad_equipos = cantidad_equipos
        logger.info(f"Servicio AlquilerEquipo '{self.nombre}' ha sido creado correctamente.")

    def validar_parametros(self, duracion_horas: int) -> None:
        if duracion_horas < 3:
            raise ValidacionEntidadError("El alquiler de equipos requiere un mínimo de 3 horas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        self.validar_parametros(duracion_horas)
        seguro_equipo = 15000.0
        return round((self.precio * duracion_horas * self.cantidad_equipos) + seguro_equipo, 2)

    def obtener_informacion(self) -> str:
        return (
            f"Alquiler de Equipos [{self.id}]: {self.nombre} | "
            f"Tarifa/h: ${self.precio:,.2f} | Equipos: {self.cantidad_equipos} | "
            f"Disponible: {self.disponibilidad}"
        )


class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio: int | str | None, nombre: str, precio: float, especialidad: str = "Desarrollo de Software", disponibilidad: bool = True):
        super().__init__(id_servicio, nombre, precio, disponibilidad)
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            mensaje = "La especialidad de la asesoría debe tener al menos 3 caracteres."
            logger.error(mensaje)
            raise ValidacionEntidadError(mensaje)
        self.especialidad = especialidad.strip()
        logger.info(f"Servicio AsesoriaEspecializada '{self.nombre}' ha sido creado correctamente.")

    def validar_parametros(self, duracion_horas: int) -> None:
        if duracion_horas <= 0:
            raise ValidacionEntidadError("La duración de la asesoría debe ser mayor a 0 horas.")

    def calcular_costo_total(self, duracion_horas: int = 1) -> float:
        return round(self.precio * duracion_horas * 1.8, 2)

    def obtener_informacion(self) -> str:
        return (
            f"Asesoría Especializada [{self.id}]: {self.nombre} ({self.especialidad}) | "
            f"Tarifa/h: ${self.precio:,.2f} | Disponible: {self.disponibilidad}"
        )


# ==================================================
# CLASE RESERVA
# ==================================================
class Reserva(Entidades):
    def __init__(self, id_reserva: str, cliente_obj: Cliente, servicio: Servicio, duracion: int):
        super().__init__(id_reserva)
        if duracion <= 0:
            raise ReservaIncorrectaError("La duración debe ser mayor a 0 horas.")
        self.cliente = cliente_obj
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"
        logger.info(f"Reserva {self.id} creada para {self.cliente.nombre}")

    def obtener_informacion(self) -> str:
        return (
            f"Reserva [{self.id}] - Cliente: {self.cliente.nombre} {self.cliente.apellido} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion}h | Estado: {self.estado}"
        )

    def es_validar(self) -> bool:
        return self.duracion > 0 and self.servicio.disponibilidad

    def confirmar(self):
        try:
            self.servicio.verificar_disponibilidad()
            self.servicio.validar_parametros(self.duracion)
        except (ServicioNoDisponibleError, ReservaIncorrectaError, ValidacionEntidadError) as e:
            logger.error(f"Reserva {self.id} falló: {getattr(e, 'mensaje', str(e))}")
            raise ReservaIncorrectaError(f"No se pudo confirmar la reserva {self.id}") from e
        else:
            self.estado = "CONFIRMADA"
            self.marcar_actualizado()
            logger.info(f"Reserva {self.id} confirmada. Estado: {self.estado}")
            return True
        finally:
            print(f"-> Reserva {self.id} finalizada. Estado: {self.estado}")

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise ReservaIncorrectaError("La reserva ya estaba cancelada")
        self.estado
