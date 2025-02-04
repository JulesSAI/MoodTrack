import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        self.geometry("360x700")

        # Establecer tema visual
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#6200ea", foreground="white", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 11))
        self.style.configure("Custom.TButton", padding=6, font=("Arial", 12), background="#6200ea", foreground="black")

        # Variables
        self.selected_emotion = tk.StringVar()
        self.selected_emotion.set("Muy Feliz")
        self.selected_date = tk.StringVar()
        self.emotion_buttons = []

        self.set_default_date()
        self.create_widgets()

    def set_default_date(self):
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        self.selected_date.set(today)

    def create_widgets(self):
        title_label = ttk.Label(self, text="MoodTrack", font=("Helvetica", 20, "bold"), foreground="purple")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        label = ttk.Label(self, text="Selecciona emoción:")
        label.grid(row=1, column=0, columnspan=2, pady=5)

        # Cargar iconos de emociones
        self.happy_icon = self.load_image("feliz.jpg")
        self.neutral_icon = self.load_image("neutral.jpg")
        self.sad_icon = self.load_image("triste.jpg")
        self.very_happy_icon = self.load_image("muyfeliz.jpg")
        self.very_sad_icon = self.load_image("muytriste.jpg")

        # Botones de emociones
        self.create_emotion_buttons()

        note_label = ttk.Label(self, text="Añadir nota:")
        note_label.grid(row=3, column=0, pady=5)

        self.note_entry = ttk.Entry(self, width=40)
        self.note_entry.grid(row=3, column=1, pady=5, padx=5)

        self.date_label = ttk.Label(self, text=f"Fecha seleccionada: {self.selected_date.get()}")
        self.date_label.grid(row=4, column=0, columnspan=2, pady=5)

        other_day_button = ttk.Button(self, text="Otro día", command=self.show_calendar, style="Custom.TButton")
        other_day_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.calendar = Calendar(self, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.grid(row=6, column=0, columnspan=2, pady=10)
        self.calendar.grid_remove()

        save_button = ttk.Button(self, text="Guardar Emoción", command=self.save_emotion, style="Custom.TButton")
        save_button.grid(row=7, column=0, columnspan=2, pady=5)

        stats_button = ttk.Button(self, text="Ver Estadísticas", command=self.show_statistics, style="Custom.TButton")
        stats_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.display_label = ttk.Label(self, text="Aquí aparecerá la emoción registrada...", foreground="gray")
        self.display_label.grid(row=9, column=0, columnspan=2, pady=5)

        select_date_button = ttk.Button(self, text="Seleccionar Fecha", command=self.select_date, style="Custom.TButton")
        select_date_button.grid(row=10, column=0, columnspan=2, pady=5)
    
    def create_emotion_buttons(self):
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        emotions = [
            ("Muy Feliz", self.very_happy_icon),
            ("Feliz", self.happy_icon),
            ("Neutral", self.neutral_icon),
            ("Triste", self.sad_icon),
            ("Muy Triste", self.very_sad_icon)
        ]
        
        for emotion, icon in emotions:
            button = ttk.Button(button_frame, image=icon, command=lambda e=emotion: self.set_emotion(e))
            button.pack(side="left", padx=5)
            self.emotion_buttons.append(button)
    
    def load_image(self, path):
        img_path = f"Vista/Recursos/{path}"
        img = Image.open(img_path)
        img = img.resize((40, 40))
        return ImageTk.PhotoImage(img)

    def set_emotion(self, emotion):
        self.selected_emotion.set(emotion)
        self.display_label.config(text=f"Emoción seleccionada: {emotion}")
    
    def set_emotion(self, emotion):
        self.selected_emotion.set(emotion)
        self.display_label.config(text=f"Emoción seleccionada: {emotion}")

    def show_calendar(self):
        self.calendar.grid()
        self.date_label.config(text="Seleccione una fecha:")

    def select_date(self):
        selected_date = self.calendar.get_date()
        self.selected_date.set(selected_date)
        self.date_label.config(text=f"Fecha seleccionada: {selected_date}")
        self.calendar.grid_remove()

    def save_emotion(self):
        emotion = self.selected_emotion.get()
        note = self.note_entry.get()
        selected_date = self.selected_date.get()
        
        if self.is_valid_date(selected_date):
            self.controller.insert_emotion(emotion, note, selected_date)
            messagebox.showinfo("Emoción Guardada", f"Emoción: {emotion}\nFecha: {selected_date}\nNota: {note if note else 'Sin nota'}")
            self.display_label.config(text=f"Emoción de {selected_date}: {emotion}\nNota: {note}")

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
