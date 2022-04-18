starting_letter_location = "./Input/Letters/starting_letter.txt"
names_location = "./Input/Names/invited_names.txt"

with open(starting_letter_location) as letter_template_original:
    letter_template = letter_template_original.read()

with open(names_location) as list_names:
    names = list_names.read().split("\n")

for all_names in names:
    new_letter = letter_template.replace("[name]", all_names)
    location = f"./Output/ReadyToSend/letter_to_{all_names}.txt"
    with open(location, mode="w") as final_letter:
        final_letter.write(new_letter)

