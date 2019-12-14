ID_HELLO_WORLD = 1
ID_EXAMPLE_WITH_PARAMETERS = 2


class DialogManager:
    text = ""

    def test(self):
        params = ["defender", "striker"]
        self.processDialog(ID_EXAMPLE_WITH_PARAMETERS, params)

    def saySomething(self):
        print(self.text)

    def processDialog(self, dial_id, list_parameters):

        if dial_id == ID_HELLO_WORLD:
            self.text = "Hello world!"
        if dial_id == ID_EXAMPLE_WITH_PARAMETERS:
            self.text = "This is an example with parameter {0} and parameter{1}".format(list_parameters[0]
                                                                                        , list_parameters[2])

        self.saySomething()
