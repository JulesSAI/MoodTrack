from Modelo.database_manager import DatabaseManager

class EmotionController:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def insert_emotion(self, emotion, note, date):
        self.db_manager.insert_emotion(emotion, note, date)

    def get_all_emotions(self):
        return self.db_manager.get_all_emotions()