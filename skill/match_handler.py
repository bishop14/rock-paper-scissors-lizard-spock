import random

from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


SHAPES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

DEFEAT_SCHEMA = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}


class PlayMatchHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ThrowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        user_shape = handler_input.request_envelope.request.intent.slots['SHAPE'].value.lower()
        alexa_shape = random.choice(SHAPES)

        if user_shape == alexa_shape:
            result = "It's a tie"
        elif user_shape in DEFEAT_SCHEMA[alexa_shape]:
            result = "You lose"
        else:
            result = "You won"

        speech_text = f"I choosed {alexa_shape}. {result}"
        reprompt_text = "Please choose a shape and throw it"

        handler_input.response_builder\
            .speak(speech_text)\
            .ask(reprompt_text)\
            .set_card(SimpleCard(result, speech_text))

        return handler_input.response_builder.response
