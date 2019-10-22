import unittest

from lambda_function import lambda_handler, DEFEAT_SCHEMA
from tests import new_request, context


class TestRegressions(unittest.TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.maxDiff = None

    def test_launch(self):
        expect = {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>Hi! And welcome to rock paper scissors lizard spock! Please choose a shape and throw "
                        "it.</speak>"
            },
            "shouldEndSession": False,
            "card": {
                "type": "Simple",
                "title": "Welcome",
                "content": "Hi! And welcome to rock paper scissors lizard spock! Please choose a shape and throw it."
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>Please choose a shape and throw it, or say 'help me' and I'll show you the game "
                            "rules.</speak>"
                }
            }
        }

        response = lambda_handler(new_request('LaunchRequest'), context)
        self.assertEqual(response['response'], expect)

    def test_session_end(self):
        response = lambda_handler(new_request('SessionEndedRequest'), context)
        self.assertEqual(response['response'], {})

    def test_help_intent(self):
        expect = {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, "
                        "Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves "
                        "Spock, Spock vaporizes Rock, and, as it always has, Rock crushes Scissors.</speak>"
            },
            "shouldEndSession": False,
            "card": {
                "type": "Simple",
                "title": "Help",
                "content": "Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, "
                           "Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves "
                           "Spock, Spock vaporizes Rock, and, as it always has, Rock crushes Scissors."
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>Please choose a shape and throw it, or say 'help me' one more time.</speak>"
                }
            }
        }

        response = lambda_handler(new_request('AMAZON.HelpIntent'), context)
        self.assertEqual(response['response'], expect)

    def test_stop_intent(self):
        expect = {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>Thank you for playing with me. Have a nice day!</speak>"
            },
            "shouldEndSession": True,
            "card": {
                "type": "Simple",
                "title": "Session Ended",
                "content": "Thank you for playing with me. Have a nice day!"
            }
        }

        response = lambda_handler(new_request('AMAZON.StopIntent'), context)
        self.assertEqual(response['response'], expect)

    def test_throw(self):
        response = lambda_handler(new_request('ThrowIntent', {'SHAPE': 'lizard'}), context)

        self.assertEqual(response['response']['shouldEndSession'], False)
        self.assertEqual(response['response']['outputSpeech']['type'], 'SSML')
        self.assertEqual(response['response']['reprompt'],  {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>Please choose a shape and throw it</speak>"
            }
        })

        self.__check_throw_response(response['response']['outputSpeech']['ssml'], 'lizard')

    def __check_throw_response(self, response_text, shape):
        if shape in response_text:
            self.assertEqual(f"<speak>I choosed {shape}. It's a tie</speak>", response_text)
        elif any(s in response_text for s in DEFEAT_SCHEMA[shape]):
            self.assertIn('You won', response_text)
        else:
            self.assertIn('You lose', response_text)


if __name__ == '__main__':
    unittest.main()
