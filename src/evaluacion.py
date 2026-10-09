"""Interfaz interactiva de autoevaluación para notebooks."""
from pathlib import Path
from html import escape
import ipywidgets as widgets
from IPython.display import display, Image, Markdown, clear_output


class Examen:
    def __init__(self, directorio_imagenes, total_preguntas=10):
        self.imagenes = Path(directorio_imagenes)
        self.total_preguntas = total_preguntas
        self.aciertos = set()
        self.registradas = set()
        self.salida_final = widgets.Output()
        self._felicitacion_mostrada = False

    def _imagen(self, nombre, ancho):
        ruta = self.imagenes / nombre
        if ruta.is_file():
            display(Image(filename=str(ruta), width=ancho))
        else:
            print(f"[Falta la imagen: {ruta}]")

    def mostrar_pregunta(self, numero, pregunta):
        if not 1 <= numero <= self.total_preguntas:
            raise ValueError("Número de pregunta fuera del rango del examen.")
        if numero in self.registradas:
            raise ValueError(f"La pregunta {numero} ya fue mostrada. Reinicia el examen para repetirla.")
        if len(pregunta["opciones"]) != 3 or pregunta["correcta"] not in (0, 1, 2):
            raise ValueError("Cada pregunta requiere tres opciones y una respuesta válida.")
        self.registradas.add(numero)
        display(Markdown(f"### {numero} · {pregunta['titulo']}\n\n{pregunta['enunciado']}"))
        opciones = widgets.RadioButtons(
            options=[(f"{letra}) {texto}", i) for i, (letra, texto) in enumerate(zip("ABC", pregunta["opciones"]))],
            value=None,
            layout=widgets.Layout(width="100%"),
            style={"description_width": "initial"},
        )
        boton = widgets.Button(description="Comprobar respuesta", button_style="info")
        salida = widgets.Output()

        def comprobar(_):
            with salida:
                clear_output(wait=True)
                if opciones.value is None:
                    print("Selecciona una respuesta antes de comprobar.")
                    return
                if opciones.value == pregunta["correcta"]:
                    self.aciertos.add(numero)
                    #self._imagen("correcto.png", 260)
                    opciones.disabled = True
                    boton.disabled = True
                    self._actualizar_final()
                    print("Correcto")
                else:
                    #self._imagen("incorrecto.png", 260)
                    print("Inténtalo nuevamente.")

        boton.on_click(comprobar)
        display(widgets.VBox([opciones, boton, salida]))

    def mostrar_final(self):
        """Colocar esta salida en la última celda del notebook."""
        display(self.salida_final)
        self._actualizar_final()

    def _actualizar_final(self):
        with self.salida_final:
            clear_output(wait=True)
            if len(self.aciertos) == self.total_preguntas:
                self._imagen("felicidades.png", 450)
                print("¡Felicidades! Completaste todas las preguntas correctamente.")
                self._felicitacion_mostrada = True
            else:
                self._imagen("error.png", 450)
                print(f"Respuestas correctas: {len(self.aciertos)}/{self.total_preguntas}. Completa todas para desbloquear la sorpresa.")
