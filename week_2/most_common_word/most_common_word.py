import collections
import re

WORD_SEPERATORS = re.compile(r"[!?',;.]*(\w+)[!?',;.]*")

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        raw_words = WORD_SEPERATORS.findall(paragraph)
        words: list[str] = [raw_word.lower() for raw_word in raw_words]

        common_words = collections.Counter(words)

        for (common_word, _) in common_words.most_common():
            if common_word not in banned:
                return common_word

        return ''
