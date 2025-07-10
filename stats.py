def count_words(text):
        number = 0
        words = text.split()
        for word in words:
                number += 1
        return number

def word_dictionary(text):
	character_count = {}
	mod_text = text.lower()
	characters = list(mod_text)
	for character in characters:
		if character in character_count:
			character_count[character] +=1
		else: character_count[character] = 1
	return character_count
