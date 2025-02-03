from Modelo.emotion_entry import EmotionEntry

class DatabaseManager:
    def __init__(self):
        self.filename = "emotions.txt"

    def insert_emotion(self, emotion, note, date):
        emotion_entry = EmotionEntry(emotion, note, date)
        with open(self.filename, "a") as file:
            file.write(str(emotion_entry) + "\n")

    def get_all_emotions(self):
        emotions = []
        #print(emotions)
        try:
            with open(self.filename, "r") as file:
                emotions = file.readlines()
        except FileNotFoundError:
            pass  # Si no existe el archivo, regresamos una lista vacía
        return [emotion.strip() for emotion in emotions]