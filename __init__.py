from mycroft import MycroftSkill, intent_file_handler


class InserisciMerce(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('merce.inserisci.intent')
    def handle_merce_inserisci(self, message):
        self.speak_dialog('merce.inserisci')


def create_skill():
    return InserisciMerce()

