from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Scissors cuts Paper, " \
                      "Paper covers Rock, " \
                      "Rock crushes Lizard, " \
                      "Lizard poisons Spock, " \
                      "Spock smashes Scissors, " \
                      "Scissors decapitates Lizard, " \
                      "Lizard eats Paper, " \
                      "Paper disproves Spock, " \
                      "Spock vaporizes Rock, " \
                      "and, as it always has, Rock crushes Scissors."
        reprompt_text = "Please choose a shape and throw it, or say 'help me' one more time."

        handler_input.response_builder\
            .speak(speech_text)\
            .ask(reprompt_text)\
            .set_card(SimpleCard("Help", speech_text))

        return handler_input.response_builder.response
