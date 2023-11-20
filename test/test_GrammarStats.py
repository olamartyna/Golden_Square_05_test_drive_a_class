from lib.GrammarStats import *

def test_check():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('What is your name?')
    assert result == True

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check('What is your name?')
    grammar_stats.check('hello')
    grammar_stats.check("Its dark now.")
    grammar_stats.check('Ola!')
    result = grammar_stats.percentage_good()
    assert result == 75