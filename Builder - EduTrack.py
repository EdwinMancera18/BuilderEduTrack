from abc import ABC, abstractmethod

# Producto complejo: Alerta
class Alerta:
    def __init__(self):
        # Lista donde se almacenan las partes de la alerta (título, contenido, recomendaciones)
        self.partes = []

    def agregar_parte(self, parte):
        # Agrega una parte al contenido de la alerta (título, contenido, recomendaciones)
        self.partes.append(parte)

    def mostrar_alerta(self):
        # Muestra la alerta construida en consola
        print("Contenido de la Alerta:")
        for parte in self.partes:
            print(f"- {parte}")

# Interfaz abstracta del Builder
class BuilderAlerta(ABC):

    @abstractmethod
    # Reinicia el proceso de construcción de una alerta.
    def reset(self): pass

    @abstractmethod
    # Agrega el encabezado o título de la alerta.
    def agregar_titulo(self): pass

    @abstractmethod
    # Agrega el contenido central o mensaje principal de la alerta.
    def agregar_contenido(self): pass

    @abstractmethod
    # Agrega recomendaciones o acciones sugeridas al final de la alerta.
    def agregar_recomendaciones(self): pass

# Builder concreto para alertas académicas
class BuilderAlertaAcademica(BuilderAlerta):
    def __init__(self):
        self.reset()

    def reset(self):
        # Se crea una nueva alerta vacía
        self.alerta = Alerta()

    def agregar_titulo(self):
        self.alerta.agregar_parte("Alerta Académica")

    def agregar_contenido(self):
        self.alerta.agregar_parte("El estudiante presenta bajo rendimiento en dos asignaturas.")

    def agregar_recomendaciones(self):
        self.alerta.agregar_parte("Se recomienda agendar tutorías y reforzar hábitos de estudio.")

    def obtener_resultado(self):
        # Devuelve el producto final (la alerta completa) y resetea el builder para que esté listo para una nueva construcción
        resultado = self.alerta
        self.reset()
        return resultado


# Director que controla el orden de construcción
class DirectorAlerta:
    def __init__(self, builder):
        self._builder = builder

    def construir_alerta_completa(self):
        # Define la secuencia de pasos para construir la alerta: título -> contenido -> recomendaciones.
        self._builder.agregar_titulo()
        self._builder.agregar_contenido()
        self._builder.agregar_recomendaciones()

# Código cliente (main)
if __name__ == "__main__":
    # Instanciamos el builder concreto para alertas académicas
    builder = BuilderAlertaAcademica()

    # Creamos un director que usará este builder
    director = DirectorAlerta(builder)

    # El director construye una alerta completa
    director.construir_alerta_completa()

    # Obtenemos el resultado final y lo mostramos por consola
    alerta = builder.obtener_resultado()
    alerta.mostrar_alerta()
