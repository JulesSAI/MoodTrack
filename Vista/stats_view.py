import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime

class StatsView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Estadísticas de Emociones")

        # Obtener emociones desde el controlador
        emotions_list = self.controller.get_all_emotions()

        # Convertir emociones en valores numéricos
        dates = []
        values = []
        for entry in emotions_list:
            date, emotion, _ = entry.split(" | ")
            value = self.get_emotion_value(emotion)
            dates.append(date)
            values.append(value)

        # Graficar los datos
        self.plot_graph(dates, values)

    def get_emotion_value(self, emotion):
        if emotion == "Muy Feliz":
            return 2
        elif emotion == "Feliz":
            return 1
        elif emotion == "Neutral":
            return 0
        elif emotion == "Triste":
            return -1
        elif emotion == "Muy Triste":
            return -2
        return 0

    def plot_graph(self, dates, values):
        fig, ax = plt.subplots()
        ax.plot(dates, values, marker='o')

        ax.set(xlabel='Fecha', ylabel='Valor de Emoción',
               title='Evolución de las Emociones')

        ax.grid()

        # Convertir la fecha a formato adecuado
        ax.set_xticklabels(dates, rotation=45, ha="right")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()