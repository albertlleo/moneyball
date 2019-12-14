from tts.tts import *
import random

ID_FIND_REQUEST_IS_READY = 1
ID_ASK_FOR_BUDGET = 2
ID_WELCOME = 3
ID_SHOW_LIST_OF_STRIKER = 4
ID_NO_VERB = 5
ID_ASK_ATTRIBUTE = 6
ID_FIND_HAS_PLAYER_NAME = 7
ID_ASK_PLAYER_ROLE = 8
ID_ASK_QUANTIFIER = 9
ID_BUDGET_NOT_VALID = 10
ID_THANKS = 11
ID_GOODBYE = 12
ID_INTENT_NOT_CLEAR = 13


class DialogManager:
    text = ""
    voice = VoiceTTS()

    def saySomething(self):
        print(self.text)
        self.voice.processTextToSpeech(self.text)

    def processDialog(self, dial_id, list_parameters=[]):

        if dial_id == ID_INTENT_NOT_CLEAR:
            self.text = "I am really understanding you. Could you repeat? "
        if dial_id == ID_GOODBYE:
            self.text = "Ok,see you!"
        if dial_id == ID_THANKS:
            self.text = "Ok, thanks!"
        if dial_id == ID_BUDGET_NOT_VALID:
            self.text = "Budget value seems not valid. Please remember to use only digits"
        if dial_id == ID_ASK_FOR_BUDGET:
            self.text = "Please type the budget you have in million"
        if dial_id == ID_WELCOME:
            self.text = "Great! Let's move on to find a perfect player for you, coach."
        if dial_id == ID_SHOW_LIST_OF_STRIKER:
            self.text = "This is the list of the {0} you are looking for".format(list_parameters[0])
        if dial_id == ID_NO_VERB:
            self.text = "I am sorry. I am not really understanding you. Remember that you can always ask me to find " \
                        "or buy football players "
        if dial_id == ID_ASK_ATTRIBUTE:
            self.text = "Please tell me the attribute for the {0} you are looking for".format(list_parameters[0])
        if dial_id == ID_FIND_HAS_PLAYER_NAME:
            self.text = "Ok, here you have all the information for {0} ".format(list_parameters[0])
        if dial_id == ID_ASK_PLAYER_ROLE:
            self.text = "What player role do you need?"
        if dial_id == ID_ASK_QUANTIFIER:
            self.text = "Ok, tell me some quantifiers about the {0} for that {1}".format(list_parameters[0],
                                                                                         list_parameters[1])
        if dial_id == ID_FIND_REQUEST_IS_READY:
            case = random.randint(0, 2)
            if 0 == case:
                self.text = "Ok, I will start searching for a {0} with a {1} {2}".format(list_parameters[0],
                                                                                         list_parameters[1],
                                                                                         list_parameters[2])
            elif 1 == case:
                self.text = "Ok, I search for a {1} {2} {0}".format(list_parameters[0], list_parameters[1],
                                                                    list_parameters[2])

        self.saySomething()
