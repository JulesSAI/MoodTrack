import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class EmotionStats:
    def __init__(self, emotions_list):
        self.emotions_list = emotions_list
        self.df = self.prepare_data()

    def prepare_data(self):
        
        data = []
        for entry in self.emotions_list:
            parts = entry.split(" | ")
            if len(parts) == 3:
                date, emotion, _ = parts
            elif len(parts) == 2:  # Si falta la nota
                date, emotion = parts
            else:
                return None 
            data.append({"Fecha": date, "Emoción": emotion})

        df = pd.DataFrame(data)
        df["Fecha"] = pd.to_datetime(df["Fecha"], dayfirst=True) 
        df = df.sort_values(by="Fecha")  # Ordenar por fecha
        return df

    def generate_plot(self):
        #Genera un gráfico de emociones con Seaborn.
        if self.df.empty:
            return None  # Si no hay datos, no genera el gráfico

        
        emotion_mapping = {
            "Muy Feliz": 2,
            "Feliz": 1,
            "Neutral": 0,
            "Triste": -1,
            "Muy Triste": -2
        }

        self.df["Valor"] = self.df["Emoción"].map(emotion_mapping)


        plt.figure(figsize=(10, 6))
        sns.set_style("darkgrid")


        sns.lineplot(
            x="Fecha", 
            y="Valor", 
            data=self.df, 
            marker="o", 
            hue="Emoción", 
            palette="coolwarm", 
            legend="full"
        )

        # Línea que une todas las emociones en orden cronológico
        sns.lineplot(
            x="Fecha", 
            y="Valor", 
            data=self.df, 
            color="black", 
            linestyle="--", 
            linewidth=1, 
            legend=False
        )

        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Fecha")
        plt.ylabel("Nivel de Emoción")
        plt.title("Evolución de las Emociones")
        plt.tight_layout()

        return plt
