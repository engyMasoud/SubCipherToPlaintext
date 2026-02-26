
cipher = input("Enter cipher text: ")
plaintext = ""

#frequecy dta found online for english language letters
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
for letter in cipher:
    if letter in cipher_letter_count:
        cipher_letter_count[letter] += 1

print("Cipher Letter Count:", cipher_letter_count)
#find the letter with the highest and second highest frequency in the cipher text
largest_letter = max(cipher_letter_count, key=cipher_letter_count.get)
second_largest_letter = max((letter for letter in cipher_letter_count if letter != largest_letter), key=cipher_letter_count.get)

#replace the letter with the highest frequency in the cipher text with 'E' and the second highest with 'T'
print(f"Will replace highest letter count '{largest_letter}' with 'E'")
print(f"Will replace second highest letter count '{second_largest_letter}' with 'T'")

#replace the letters in the cipher text and print the updated cipher text
updated_cipher = cipher.replace(largest_letter, 'E').replace(second_largest_letter, 'T')
print("Updated Cipher:", updated_cipher)

#find the letter with the third highest frequency in the cipher text and replace it with 'A' and update cipher text
third_largest_letter = max((letter for letter in cipher_letter_count if letter != largest_letter and letter != second_largest_letter), key=cipher_letter_count.get)
print(f"Will replace third highest letter count '{third_largest_letter}' with 'A'")
updated_cipher = updated_cipher.replace(third_largest_letter, 'A')
print("Updated Cipher:", updated_cipher)

#find the letter with the fourth highest frequency in the cipher text and replace it with 'O' and update cipher text
fourth_largest_letter = max((letter for letter in cipher_letter_count if letter != largest_letter and letter != second_largest_letter and letter != third_largest_letter), key=cipher_letter_count.get)
print(f"Will replace fourth highest letter count '{fourth_largest_letter}' with 'O'")
updated_cipher = updated_cipher.replace(fourth_largest_letter, 'O')
print("Updated Cipher:", updated_cipher)
