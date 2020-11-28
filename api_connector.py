import requests
import json
import re


class ApiConnector:

    def __init__(self):
        '''
        Handles the connection to the words api and all relevant functionalities to the hangman game
        To learn more about the api, visit:
        https://rapidapi.com/dpventures/api/wordsapi
        '''

        self.url = "https://wordsapiv1.p.rapidapi.com/words/"
        self.headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "1b6e0a8e8dmsh2937f4335207ce5p16bcf5jsn2e9ca9e4cfef"
        }
        self.entry = {}

    def get_entry(self):
        """
    A function that connects to the Words api and returns a dictionary containing a random word, its definition
    and a list of synonyms.

    Args:
    :parameter = None

    Return:
    word (string): the randomly generated word
        """

        querystring = {"random": "true"}
        response = requests.request(
            "GET", self.url, headers=self.headers, params=querystring)
        result = json.loads(response.text)
        search_key = "results"
        word = result['word']
        pattern = "[a-zA-Z\s]+$"

        if search_key in result and re.match(pattern, word):
            self.entry = result
        else:
            self.get_entry()

    def get_definition(self):
        """
        Gets the definition of a given word by connecting to the Words api provided by Rapid api
        Args:
            entry (string): the word to be defined
        Return:
            definitions (list): the definitions of the given words in a list
        """

        definitions_dict = self.entry['results']
        definitions = [sub['definition'] for sub in definitions_dict]
        definition = definitions[0]
        return definition

    def get_word(self):
        word = self.entry['word']
        return word

    def to_string(self):
        return f'entry: {self.entry}'
