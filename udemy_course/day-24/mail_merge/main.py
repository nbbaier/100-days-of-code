## get the names
with open("./Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
    names = [name.strip() for name in names]

## get the starting letters
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    base_letter = letter.read()

for name in names:
    new_filename = f"letter_for_{name}.txt"
    new_letter = base_letter.replace("[name]", name)
    with open(f'./Output/ReadyToSend/{new_filename}','w') as f:
        f.write(new_letter)
    