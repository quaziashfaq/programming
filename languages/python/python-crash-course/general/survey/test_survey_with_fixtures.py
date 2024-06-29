#!/usr/bin/env python3

import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    '''A survey object that will be available to all test functions.'''
    '''Here function name and returned object have to have same names!?!'''
    question = 'What language did you learn first?'
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    '''Test that a single response is stored properly.'''
    #question = 'What language did you learn first?'
    #language_survey = AnonymousSurvey(question)
    language_survey.store_response('Bangla')
    assert 'Bangla' in language_survey.responses


def test_store_three_respones(language_survey):
    '''Test that three responses are stored properly.'''
    #question = 'What language did you learn first?'
    #language_survey = AnonymousSurvey(question)
    responses = ['Bangla', 'English', 'Arabic']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
