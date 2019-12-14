ID_HELLO_WORLD = 1
ID_EXAMPLE_WITH_PARAMETERS = 2
ID_WELCOME = 3
ID_SHOW_LIST_OF_STRIKER = 4
ID_NO_VERB = 5


class DialogManager:
    text = ""

    def test(self):
        params = ["defender", "striker"]
        self.processDialog(ID_EXAMPLE_WITH_PARAMETERS, params)

    def saySomething(self):
        print(self.text)

    def processDialog(self, dial_id, list_parameters=[]):

        if dial_id == ID_HELLO_WORLD:
            self.text = "Hello world!"
        if dial_id == ID_EXAMPLE_WITH_PARAMETERS:
            self.text = "This is an example with parameter {0} and parameter{1}".format(list_parameters[0]
                                                                                        , list_parameters[2])
        if dial_id == ID_WELCOME:
            self.text = "Great! Let's move on to find a perfect player for you coach."
        if dial_id == ID_SHOW_LIST_OF_STRIKER:
            self.text = "This is the list of the {0} you are looking for".format(list_parameters[0])
        if dial_id == ID_NO_VERB:
            self.text = "I am sorry. I am not really understanding you. Remember that you can always ask me to find " \
                        "or buy football players "

        self.saySomething()
