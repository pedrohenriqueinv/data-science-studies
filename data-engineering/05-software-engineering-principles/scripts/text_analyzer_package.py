# -*- coding: utf-8 -*-
"""
Modular Text & Telemetry Analyzer Package Implementation
"""
import re
from typing import Dict, List, Optional
from collections import Counter

class DocumentAnalyzer:
    """Analyzes text corpora for vocabulary distribution, word frequency, and metrics."""
    
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("DocumentAnalyzer requires text of type str")
        self._raw_text = text
        self._tokens = self._tokenize()

    def _tokenize(self) -> List[str]:
        """Internal helper to strip punctuation and normalize tokens."""
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", self._raw_text.lower())
        return cleaned.split()

    @property
    def token_count(self) -> int:
        """Returns total number of words in document."""
        return len(self._tokens)

    @property
    def unique_word_count(self) -> int:
        """Returns count of distinct words."""
        return len(set(self._tokens))

    def top_n_words(self, n: int = 5) -> List[tuple]:
        """Returns the most common words and their frequencies."""
        counter = Counter(self._tokens)
        return counter.most_common(n)

class SocialMediaAnalyzer(DocumentAnalyzer):
    """Specialized analyzer extending DocumentAnalyzer to detect hashtags and mentions."""
    
    def extract_hashtags(self) -> List[str]:
        """Extracts all #hashtag occurrences from raw text."""
        return re.findall(r"#\w+", self._raw_text)

    def extract_mentions(self) -> List[str]:
        """Extracts all @mention occurrences from raw text."""
        return re.findall(r"@\w+", self._raw_text)
