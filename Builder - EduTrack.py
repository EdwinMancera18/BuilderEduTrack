from abc import ABC, abstractmethod

# Producto complejo: Alerta
class Alerta:
    def __init__(self):
        # Lista donde se almacenan las partes de la alerta (título, contenido, recomendaciones)
        self.partes = []

    def agregar_parte(self, parte):
        # Agrega una parte al contenido de la alerta
        self.partes.append(parte)

    def mostrar_alerta(self):
        # Muestra la alerta construida en consola
        print("Contenido de la Alerta:")
        for parte in self.partes:
            print(f"- {parte}")

# Interfaz abstracta del Builder
class BuilderAlerta(ABC):
    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def agregar_titulo(self): pass

    @abstractmethod
    def agregar_contenido(self): pass

    @abstractmethod
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
        # Devuelve la alerta construida y resetea el builder
        resultado = self.alerta
        self.reset()
        return resultado


# Director que controla el orden de construcción
class DirectorAlerta:
    def __init__(self, builder):
        self._builder = builder

    def construir_alerta_completa(self):
        # Define la secuencia de pasos para construir la alerta
        self._builder.agregar_titulo()
        self._builder.agregar_contenido()
        self._builder.agregar_recomendaciones()

# Código cliente (main)
if __name__ == "__main__":
    # Se instancia el builder concreto
    builder = BuilderAlertaAcademica()

    # Se pasa el builder al director
    director = DirectorAlerta(builder)

    # El director construye la alerta
    director.construir_alerta_completa()

    # Se obtiene y muestra la alerta
    alerta = builder.obtener_resultado()
    alerta.mostrar_alerta()