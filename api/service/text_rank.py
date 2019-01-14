from textrank4zh import TextRank4Keyword, TextRank4Sentence


class TextRank(object):

    def __init__(self):
        self.tr4w = TextRank4Keyword()
        print("init TextRank")

    def get_highest_rank(self, text, max_sentences):

        self.tr4w.analyze(text=text, lower=True, window=2)

        print("Keywords：")
        for item in self.tr4w.get_keywords(10, word_min_len=2):
            print(item.word, item.weight)

        print("Phrases：")
        for phrase in self.tr4w.get_keyphrases(keywords_num=25, min_occur_num=1):
            print(phrase)

        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')

        print("Summary：")
        summary = []
        for item in tr4s.get_key_sentences(num=max_sentences):
            print(item.index, item.weight, item.sentence)
            summary.append(item.sentence)

        return summary
