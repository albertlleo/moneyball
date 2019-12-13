from nl import nlp
import pandas as pd
import random
from nl import nlp_context


query_intent = {'buy_type': '', 'attribute': [], 'quantifier': '', 'player_role': []}


def greeting():
	print("Hi, My name is Susan and I am the best transfer market bot available")
	name = input("What's your name, Coach?\n")
	print(f"Nice to meet you Coach,{name}. How can I help you?")
	query = input()
	return query


def dialogue():
	global query_intent
	print("intent1", query_intent)
	dialogues = pd.read_csv('dialogue.csv')
	# If buy type is not specified , i.e., we don't know if he wants to buy or rent
	if (query_intent['buy_type'] == 'find') | (query_intent['buy_type'] == ''):
		row = dialogues[dialogues.buy_type == 0]
		# Picks a random dialogue from the same type of attributes
		row = row.iloc[random.randint(0, row.shape[0] - 1)]
		user_dialogue = input(row.dialogue)
		# process new tokens
		buy_type, attribute, quantifier, player_role = nlp.process(user_dialogue)
		populate_intent(buy_type=buy_type, attribute=attribute, quantifier=quantifier, player_role=player_role)
	print("intent2", query_intent)
	if query_intent['buy_type'] == 'buy':
		row = dialogues[dialogues.buy_type == 1]
		# pick a random question to ask
		row = row.iloc[random.randint(0, row.shape[0] - 1)]
		user_dialogue = input(row.dialogue)
	print("intent3", query_intent)


def populate_intent(buy_type='', attribute='', quantifier='', player_role=''):
	global query_intent
	print("Inside populate", buy_type, attribute, quantifier, player_role)
	query_intent['buy_type'] = buy_type
	query_intent['quantifier'] = quantifier
	query_intent['attribute'].append(attribute)
	query_intent['player_role'].append(player_role)


def main():

	query = greeting()
	request_context = nlp_context.RequestContext()
	request_context = nlp.process(query, request_context)
	buy_type_2 = request_context.category_verb
	print("Hi", buy_type_2)
	attribute_2 = request_context.category_attribute
	print("Hi", attribute_2)
	#print("h main", buy_type, attribute, quantifier, player_role)
	#populate_intent(buy_type=buy_type, attribute=attribute, quantifier=quantifier, player_role=player_role)
	#dialogue()


if __name__ == '__main__':
	main()
