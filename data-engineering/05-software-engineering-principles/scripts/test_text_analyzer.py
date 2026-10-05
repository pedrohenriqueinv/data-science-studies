# -*- coding: utf-8 -*-
"""
Automated Unit Test Suite for TextAnalyzer using pytest
"""
import pytest
from text_analyzer_package import DocumentAnalyzer, SocialMediaAnalyzer

@pytest.fixture
def sample_corpus():
    return "Data engineering with Python makes pipelines fast, scalable, and fast!"

@pytest.fixture
def social_post():
    return "Learning #ApacheAirflow and #Python with @DataCamp! #DataEngineering"

def test_document_analyzer_token_count(sample_corpus):
    analyzer = DocumentAnalyzer(sample_corpus)
    assert analyzer.token_count == 9

def test_document_analyzer_unique_count(sample_corpus):
    analyzer = DocumentAnalyzer(sample_corpus)
    # 'fast' is repeated twice
    assert analyzer.unique_word_count == 8

def test_top_n_words(sample_corpus):
    analyzer = DocumentAnalyzer(sample_corpus)
    top = analyzer.top_n_words(1)
    assert top[0][0] == "fast"
    assert top[0][1] == 2

def test_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        DocumentAnalyzer(12345)

def test_social_media_analyzer(social_post):
    analyzer = SocialMediaAnalyzer(social_post)
    tags = analyzer.extract_hashtags()
    mentions = analyzer.extract_mentions()
    assert "#ApacheAirflow" in tags
    assert "#Python" in tags
    assert "@DataCamp" in mentions
