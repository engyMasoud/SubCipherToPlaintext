#Group 6: Engy Masoud, Nicole Perez, Haruka Miyazaki

#prompts user to enter cipher text
cipher = input("Enter cipher text: ")
print()

#sets variable to count the total number of letters (later used to calculate frequency) 
total_count_of_letters = 0

#frequency data found online for english language letters
standard_letter_frequency = {
    'A': 8.17,
    'B': 1.49,
    'C': 2.78,
    'D': 4.25,
    'E': 12.70,
    'F': 2.23,
    'G': 2.02,
    'H': 6.09,
    'I': 6.97,
    'J': 0.15,
    'K': 0.77,
    'L': 4.03,
    'M': 2.41,
    'N': 6.75,
    'O': 7.51,
    'P': 1.93,
    'Q': 0.10,
    'R': 5.99,
    'S': 6.33,
    'T': 9.06,
    'U': 2.76,
    'V': 0.98,
    'W': 2.36,
    'X': 0.15,
    'Y': 1.97,
    'Z': 0.07
}
#inital letter count for the cipher text
cipher_letter_count = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0
}

#loop through the cipher text and count the frequency of each letter
#also counting the total number of letters in the cipher text here as well
for letter in cipher:
    if letter in cipher_letter_count:
        cipher_letter_count[letter] += 1
        total_count_of_letters += 1

#sorts by freq and maps cipher letters to english letters
sorted_cipher_letters = sorted(cipher_letter_count, key=lambda letter: cipher_letter_count[letter], reverse=True)
sorted_english_letters = sorted(standard_letter_frequency, key=lambda letter: standard_letter_frequency[letter], reverse=True)

#prints out the frequency of each letter in the inputted cipher text 
#(frequency is both in counts and percentages)
print(f"Letter | Count | Percent(%)")
print(f"-------|-------|-----------")
for letter in sorted_cipher_letters:
    #doing the calculation for the frequency in percentage here 
    count = cipher_letter_count[letter]
    frequency_in_percent = (count / total_count_of_letters) * 100
    print(f"   {letter}   |   {cipher_letter_count[letter]}   |  {frequency_in_percent:.2f} ")

#mapping the sorted cipher letters to the english for decrypting
mapping = dict(zip(sorted_cipher_letters, sorted_english_letters))

#doing the actual decrypting here and printing out the result 
deciphered = ""
for letter in cipher:
    deciphered = deciphered + mapping.get(letter, letter)

print()
print(f"Deciphered Text Based on Frequency Only: {deciphered}")
print()

#manual replacement feature that prompts user
while True:
    answer = input("Would you like to make a replacement? (y or n)").lower()
    if answer == "n":
        break
    elif answer == "y":
        print()
        print(f"Cipher:     {cipher}")
        print(f"Deciphered: {deciphered}")
        print()
        originalLetter = input("What letter would you like to replace from the original cipher? ").upper()
        replacementLetter = input("What letter would you like to replace it with? ").upper()
        print()
        mapping[originalLetter] = replacementLetter
        deciphered = ""
        for letter in cipher:
            deciphered = deciphered + mapping.get(letter, letter)
        print(f"Deciphered Text: {deciphered}")
    

