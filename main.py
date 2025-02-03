from Controlador.emotion_controller import EmotionController
from Vista.main_view import MainView

def main():
    # Crear una instancia del controlador
    controller = EmotionController()

    # Crear y mostrar la vista principal
    app = MainView(controller)
    app.mainloop()

if __name__ == "__main__":
    main()