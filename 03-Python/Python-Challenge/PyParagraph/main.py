
import re

paragraph_data = r"03-Python/Python-Challenge/PyParagraph/paragraph_3.txt"
paragraph_output = r"03-Python/Python-Challenge/PyParagraph/output.txt"

paragraph = ""

with open(paragraph_data) as txt_data:
	paragraph = txt_data.read().replace("\n", " ")

word_split = paragraph.split(" ")
word_count = len(word_split)


sentence_split = re.split("(?<=[.!?]) +", paragraph)
sentence_count = len(sentence_split)


letter_count = []
for word in word_split:
	letter_count.append(len(word))

average_letter_len = round(sum(letter_count)/len(letter_count), 2)

sentence_per_word = []
for sentence in sentence_split:
	sentence_per_word.append(len(sentence.split(" ")))

average_sentence_len = round(sum(sentence_per_word) / len(sentence_per_word), 2)

output = (
	f"\nParagraph Analysis\n"
	f"-----------------\n"
	f"Approximate Word Count: {word_count}\n"
	f"Approximate Sentence Count: {sentence_count}\n"
	f"Average Letter Count: {average_letter_len}\n"
	f"Average Sentence Length: {average_sentence_len}\n"
)

print(output)

with open(paragraph_output, "a") as txt_file:
	txt_file.write(output)