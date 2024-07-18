from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  excess_shift = shift % 26
  
  #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
    #   if cipher_direction == "encode":
    #     new_position = position + shift_amount
    #   else:
    #     new_position = position - shift_amount
    #   end_text += alphabet[new_position]
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char
    print(f"The {cipher_direction}d text is {end_text}")
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")





# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
