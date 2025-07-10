def get_book_text(filepath):
	with open(filepath) as f:
		contents = f.read()
	return contents

from stats import count_words
from stats import word_dictionary
import sys

def sort_on(items):
	return items["num"]

def get_sorted_you_bitch_dic(items):
	new_list = []
	for item in items:
		count = items[item]
		new_list.append({"char": item, "num": count})
	return new_list

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	result = get_book_text(filepath)
	num_words = count_words(result)
	char_counts = word_dictionary(result)
	char_counts_list = get_sorted_you_bitch_dic(char_counts)
	char_counts_list.sort(reverse=True, key=sort_on)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in char_counts_list:
		if item["char"].isalpha() == True:
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

main()
