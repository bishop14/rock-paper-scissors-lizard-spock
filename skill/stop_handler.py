from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        card_title = "Session Ended"
        speech_text = "Thank you for playing with me. Have a nice day!"

        handler_input.response_builder\
            .speak(speech_text)\
            .set_card(SimpleCard(card_title, speech_text))\
            .set_should_end_session(True)

        return handler_input.response_builder.response

