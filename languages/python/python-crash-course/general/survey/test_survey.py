#!/usr/bin/env python3

from survey import AnonymousSurvey

def test_store_single_response():
    '''Test that a single response is stored properly.'''
    question = 'What language did you learn first?'
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('Bangla')
    assert 'Bangla' in language_survey.responses


def test_store_three_respones():
    '''Test that three responses are stored properly.'''
    question = 'What language did you learn first?'
    language_survey = AnonymousSurvey(question)
    responses = ['Bangla', 'English', 'Arabic']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
