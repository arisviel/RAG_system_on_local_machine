import pickle
from sentence_transformers import SentenceTransformer
from scipy import spatial


class text_finder_cos:
    """Основной класс поисковика похожих текстов"""
    def __init__(self) -> None:
        """Чтение корпуса текста и эмбедингов"""
        with open("./data/corpus.pickle", "rb") as handle:
            self.corpus = pickle.load(handle)
        with open("./data/embeds.pickle", "rb") as handle:
            self.embeds = pickle.load(handle)
        self.model = SentenceTransformer("intfloat/multilingual-e5-small")

    def find_text(self, prompt: str) -> str:
        """Выполяет поиск 3х наиболее подходящих кусков текста, склеивает в строку"""
        prompt = self.model.encode(prompt)
        sim_dict = {}
        text = ""

        for emb_key in self.embeds.keys():
            sim = 1 - spatial.distance.cosine(prompt, self.embeds[emb_key])
            sim_dict[emb_key] = sim

        sim_dict = dict(reversed(sorted(sim_dict.items(), key=lambda item: item[1])))
        for ks in list(sim_dict.keys())[:3]:
            text = text + self.corpus[ks]

        print(text)
        return text
