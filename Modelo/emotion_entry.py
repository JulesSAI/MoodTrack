class EmotionEntry:
    def __init__(self, emotion, note, date):
        self.emotion = emotion
        self.note = note
        self.date = date

    def __str__(self):
        return f"{self.date} | {self.emotion} | {self.note}"

    def to_dict(self):
        return {
            "emotion": self.emotion,
            "note": self.note,
            "date": self.date
        }