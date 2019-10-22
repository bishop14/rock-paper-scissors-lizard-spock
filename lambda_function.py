from ask_sdk_core.skill_builder import SkillBuilder

from skill.exception_handler import CatchAllExceptionHandler
from skill.help_handler import HelpIntentHandler
from skill.launch_handler import LaunchRequestHandler
from skill.match_handler import PlayMatchHandler
from skill.session_end_handler import SessionEndedRequestHandler
from skill.stop_handler import CancelOrStopIntentHandler

sb = SkillBuilder()

SHAPES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

DEFEAT_SCHEMA = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(PlayMatchHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
