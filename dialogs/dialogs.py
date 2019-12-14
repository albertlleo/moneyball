
from tts import tts

ID_HELLO_WORLD = 1
ID_EXAMPLE_WITH_PARAMETERS = 2
ID_WELCOME = 3
ID_SHOW_LIST_OF_STRIKER = 4
ID_NO_VERB = 5
ID_ASK_ATTRIBUTE = 6
ID_FIND_HAS_PLAYER_NAME = 7
ID_ASK_PLAYER_ROLE = 8
ID_ASK_QUANTIFIER = 9
ID_FIND_REQUEST_IS_READY = 10


class DialogManager:
    text = ""

    def test(self):
        params = ["defender", "striker"]
        self.processDialog(ID_EXAMPLE_WITH_PARAMETERS, params)

    def saySomething(self):
        print(self.text)
        tts.processTextToSpeech(self.text)

    def processDialog(self, dial_id, list_parameters=[]):

        if dial_id == ID_HELLO_WORLD:
            self.text = "Hello world!"
        if dial_id == ID_EXAMPLE_WITH_PARAMETERS:
            self.text = "This is an example with parameter {0} and parameter{1}".format(list_parameters[0]
                                                                                        , list_parameters[2])
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
            self.text = "Ok, tell me some quantifiers about the {0} for that {1}".format(list_parameters[0], list_parameters[1])
        if dial_id == ID_FIND_REQUEST_IS_READY:
            self.text = "Ok, I will start searching for a {0} with a {1} {2}".format(list_parameters[0], list_parameters[1], list_parameters[2])

        self.saySomething()
