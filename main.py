def letter_frequency(message):

    letters_frequency = {}

    if not message:
        return letters_frequency

    for letter in message:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters_frequency:
                letters_frequency[letter] += 1
            else:
                letters_frequency[letter] = 1

    return letters_frequency


def display_frequency(frequency):

    if not frequency:
        print("Your message has no letters!")
        return

    sorted_freq = dict(sorted(frequency.items()))

    print("Letter Frequencies:")
    for letter, count in sorted_freq.items():
        print(f"{letter}: {count}")


def main():

    while True:
        input_message = input("Input your message ").strip()

        if not input_message:
            print("The message field cannot be submitted blank!")
            continue

        freq = letter_frequency(input_message)
        display_frequency(freq)

        submit_another = input("Do you want to analyze another message? (yes/no): ").lower().strip()
        if submit_another == "no":
            print("Program exitted successfully")
            break
        elif submit_another == "yes":
            continue
        else:
            print("Please enter 'yes' or 'no'.")

main()

