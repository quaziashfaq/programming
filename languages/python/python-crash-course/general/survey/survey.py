#!/usr/bin/env python3

class AnonymousSurvey:
    '''Collect anonymous answers to a survey question.'''

    def __init__(self, question):
        '''store a question first. Then prepares to store the answers.'''
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_result(self):
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')

