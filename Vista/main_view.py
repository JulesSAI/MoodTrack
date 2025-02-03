import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk  
import datetime
from Controlador.emotion_controller import EmotionController
from Vista.stats_view import StatsView

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Registro de Emociones")
        self.geometry("500x600")

        title_label = tk.Label(self, text="MoodTrack", font=("Helvetica", 20, "bold"), fg="purple")
        title_label.pack(pady=10)  # Esto agrega espacio arriba del título

        # Variables
        self.selected_emotion = tk.StringVar()
        self.selected_emotion.set("Muy Feliz")
        self.selected_date = tk.StringVar()

        # Establecer fecha por defecto
        self.set_default_date()

        # Etiquetas y componentes
        self.create_widgets()

    def set_default_date(self):
        # Fecha de hoy
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        self.selected_date.set(today)

    def create_widgets(self):

        # Label para seleccionar emoción
        label = tk.Label(self, text="Selecciona emoción:")
        label.pack(pady=5)

        # Cargar iconos de emociones
        self.happy_icon = self.load_image("feliz.jpg")
        self.neutral_icon = self.load_image("neutral.jpg")
        self.sad_icon = self.load_image("triste.jpg")
        self.very_happy_icon = self.load_image("muyfeliz.jpg")
        self.very_sad_icon = self.load_image("muytriste.jpg")

        # Botones de emociones
        self.create_emotion_buttons()


        # Nota
        note_label = tk.Label(self, text="Añadir nota:")
        note_label.pack()

        self.note_entry = tk.Entry(self)
        self.note_entry.pack()

        # Label para fecha seleccionada
        self.date_label = tk.Label(self, text=f"Fecha seleccionada: {self.selected_date.get()}")
        self.date_label.pack()

        # Botón para seleccionar otro día
        other_day_button = tk.Button(self, text="Otro día", command=self.show_calendar)
        other_day_button.pack(pady=5)

        # Mostrar el calendario (inicialmente oculto)
        self.calendar = Calendar(self, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.pack(pady=10)
        self.calendar.pack_forget()  # Ocultar el calendario al inicio

        # Botón de guardar
        save_button = tk.Button(self, text="Guardar Emoción", command=self.save_emotion)
        save_button.pack()

        # Botón de estadísticas
        stats_button = tk.Button(self, text="Ver Estadísticas", command=self.show_statistics)
        stats_button.pack()

        # Etiqueta para mostrar la emoción guardada
        self.display_label = tk.Label(self, text="Aquí aparecerá la emoción registrada...")
        self.display_label.pack()

        select_date_button = tk.Button(self, text="Seleccionar Fecha", command=self.select_date)
        select_date_button.pack(pady=5)
    
    def load_image(self, path):
        # Cargar imagen y redimensionarla
        img_path = f"Vista/Recursos/{path}"
        print(f"Ruta del archivo: {img_path}")  # Para depurar la ruta
        img = Image.open(img_path)
        img = img.resize((40, 40))  # Ajusta el tamaño del icono
        return ImageTk.PhotoImage(img)
    
    def create_emotion_buttons(self):
        # Crear botones con iconos
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Botones de emociones (de izquierda a derecha)
        self.create_emotion_button(button_frame, self.very_happy_icon, "Muy Feliz")
        self.create_emotion_button(button_frame, self.happy_icon, "Feliz")
        self.create_emotion_button(button_frame, self.neutral_icon, "Neutral")
        self.create_emotion_button(button_frame, self.sad_icon, "Triste")
        self.create_emotion_button(button_frame, self.very_sad_icon, "Muy Triste")
    
    def create_emotion_button(self, frame, icon, emotion):
        # Crear un botón y asignarle una acción para cambiar la emoción seleccionada
        button = tk.Button(frame, image=icon, command=lambda e=emotion: self.set_emotion(e, button))
        button.pack(side="left", padx=10)

    def set_emotion(self, emotion, button):
        # Cambiar la emoción seleccionada
        self.selected_emotion.set(emotion)
        
        # Resaltar el botón seleccionado
        self.highlight_selected_button(button)

    def highlight_selected_button(self, button):
        # Cambiar color de fondo del botón seleccionado
        button.config(bg="lightblue")  # Resalta el botón con color azul claro

 

    def show_calendar(self):
        # Mostrar el calendario y actualizar la etiqueta de la fecha
        self.calendar.pack()
        self.date_label.config(text="Seleccione una fecha:")

        # Ocultar el botón de "Otro día"
        self.date_label.pack_forget()

     

    def select_date(self):
        # Obtener la fecha seleccionada
        selected_date = self.calendar.get_date()
        self.selected_date.set(selected_date)

        # Actualizar la etiqueta con la nueva fecha
        self.date_label.config(text=f"Fecha seleccionada: {selected_date}")

        # Ocultar el calendario y el botón de selección de fecha
        self.calendar.pack_forget()
        self.date_label.pack()
        

    def save_emotion(self):
        emotion = self.selected_emotion.get()
        note = self.note_entry.get()
        selected_date = self.selected_date.get()

        # Validar la fecha
        if self.is_valid_date(selected_date):
            self.controller.insert_emotion(emotion, note, selected_date)
            self.display_label.config(text=f"Emoción de: {selected_date}\nEmoción: {emotion}\nNota: {note}")
        else:
            messagebox.showerror("Error", "Fecha inválida")

    def show_statistics(self):
        stats_view = StatsView(self.controller)
        stats_view.mainloop()

    def is_valid_date(self, date):
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
            return True
        except ValueError:
            return False