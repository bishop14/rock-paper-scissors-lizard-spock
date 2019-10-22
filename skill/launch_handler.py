from ask_sdk_core.utils import is_request_type
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        card_title = "Welcome"
        speech_text = "Hi! And welcome to rock paper scissors lizard spock! " \
                      "Please choose a shape and throw it."
        reprompt_text = "Please choose a shape and throw it, or say 'help me' and I'll show you the game rules."

        handler_input.response_builder\
            .speak(speech_text)\
            .ask(reprompt_text)\
            .set_card(SimpleCard(card_title, speech_text))\
            .set_should_end_session(False)

        return handler_input.response_builder.response
