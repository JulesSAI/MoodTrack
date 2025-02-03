import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Modelo.estadisticas import EmotionStats  # Importamos la nueva clase

class StatsView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Estadísticas de Emociones")

        # Obtener emociones desde el controlador
        emotions_list = self.controller.get_all_emotions()
        stats = EmotionStats(emotions_list)  # Instancia de EmotionStats
        plot = stats.generate_plot()

        if plot:
            canvas = FigureCanvasTkAgg(plot.gcf(), master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()
        else:
            tk.Label(self, text="No hay datos suficientes para generar el gráfico").pack()
