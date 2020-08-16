from mycroft import MycroftSkill, intent_file_handler


class InserisciMerce(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('merce.inserisci.intent')
    def handle_merce_inserisci(self, message):
    	date2 = message.data.get('date')
		date_str = str(date2)
		if date2:
			self.speak_dialog('Inserisco viaggio per ' + date_str )
		else:
        	self.speak_dialog('merce.inserisci')


def create_skill():
    return InserisciMerce()

