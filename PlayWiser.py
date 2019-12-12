from nl import nlp
import pandas as pd


def greeting():
	print("Hi, My name is Susan and I am the best transfer market bot available")
	name = input("What's your name, Coach?\n")
	print(f"Nice to meet you Coach,{name}. How can I help you?")


def dialogue(query_intent):
	dialogues = pd.read_csv('dialogue.csv')
	row = dialogues[dialogues.buy_type == 0]
	dialogue_user = row.dialogue
	print(dialogue_user)


def talk(query_intent):

	if query_intent['buy_type'] == 'find':
		query_intent['buy_type'] = input("Are you looking to buy or rent a player?")
	if query_intent['player_role'] == ['']:
		query_intent['player_role'] = input("What position are you looking for?")


def connect_nlp():
	query = input()
	return nlp.process(query)


def populate_intent(verb='find', attribute='', quantifier='', player_role=''):
	query_intent = {'buy_type': verb, 'attribute': [], 'quantifier': quantifier, 'player_role': []}
	query_intent[attribute] = query_intent['attribute'].append(attribute)
	query_intent[player_role] = query_intent['player_role'].append(attribute)
	return query_intent


def main():
	greeting()
	verb, attribute, quantifier, player_role = connect_nlp()
	query_intent = populate_intent(verb=verb, attribute=attribute, quantifier=quantifier, player_role=player_role)
	#talk(query_intent=query_intent)
	dialogue(query_intent)


if __name__ == '__main__':
	main()
