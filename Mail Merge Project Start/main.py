with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as latter_format:
    letter = latter_format.readlines()
    letter = ''.join(letter)
    with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as names:
        for name in names:
            name = name.strip()
            new_latter = letter.replace('[name]', name)
            with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}", mode='w') as file:
                file.write(new_latter)
