from textrank4zh import TextRank4Keyword, TextRank4Sentence
import logging

logger = logging.getLogger(__name__)


class TextRank:

    def __init__(self):
        self.tr4w = TextRank4Keyword()
        print(logger)
        logger.info("init TextRank")

    def get_highest_rank(self, text, max_sentences):

        self.tr4w.analyze(text=text, lower=True, window=2)

        logger.info("Keywords：")
        for item in self.tr4w.get_keywords(10, word_min_len=2):
            logger.info("%s %s",item.word, item.weight)

        logger.info("Phrases：")
        for phrase in self.tr4w.get_keyphrases(keywords_num=25, min_occur_num=1):
            logger.info(phrase)

        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')

        logger.info("Summary：")
        summary = []
        for item in tr4s.get_key_sentences(num=max_sentences):
            logger.info("%s %s %s", item.index, item.weight, item.sentence)
            summary.append(item.sentence)

        return summary
