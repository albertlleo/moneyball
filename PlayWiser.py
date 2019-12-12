from nl import nlp
import pandas as pd
import random


def greeting():
	print("Hi, My name is Susan and I am the best transfer market bot available")
	name = input("What's your name, Coach?\n")
	print(f"Nice to meet you Coach,{name}. How can I help you?")
	query = input()
	return query


def dialogue(query_intent):
	dialogues = pd.read_csv('dialogue.csv')
	# If buy type is not specified , i.e., we don't know if he wants to buy or rent
	if (query_intent['buy_type'] == 'find') | (query_intent['buy_type'] == ''):
		row = dialogues[dialogues.buy_type == 0]
		# Picks a random dialogue from the same type of attributes
		row = row.iloc[random.randint(0, row.shape[0] - 1)]
		user_dialogue = input(row.dialogue)
		buy_type, attribute, quantifier, player_role = nlp.process(user_dialogue)
		query_intent = populate_intent(verb=buy_type, attribute=attribute, quantifier=quantifier, player_role=player_role)
		print(query_intent)
		# process new tokens

	elif query_intent['buy_type'] == 'buy':
		print(query_intent)
		row = dialogues[dialogues.buy_type == 1]
		# pick a random question to ask


def talk(query_intent):

	if query_intent['buy_type'] == 'find':
		query_intent['buy_type'] = input("Are you looking to buy or rent a player?")
	if query_intent['player_role'] == ['']:
		query_intent['player_role'] = input("What position are you looking for?")


def populate_intent(verb='find', attribute='', quantifier='', player_role=''):
	query_intent = {'buy_type': verb, 'attribute': [], 'quantifier': quantifier, 'player_role': []}
	query_intent[attribute] = query_intent['attribute'].append(attribute)
	query_intent[player_role] = query_intent['player_role'].append(attribute)
	return query_intent


def main():
	query = greeting()
	buy_type, attribute, quantifier, player_role = nlp.process(query)
	query_intent = populate_intent(verb=buy_type, attribute=attribute, quantifier=quantifier, player_role=player_role)
	#talk(query_intent=query_intent)
	dialogue(query_intent)


if __name__ == '__main__':
	main()
