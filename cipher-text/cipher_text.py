import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
lower_set = set(lowercase)
upper_set = set(uppercase)

def cipher(message, shift):
    result = ''
    for char in message:
        if char in lower_set:
            idx = lowercase.index(char)
            result += lowercase[(idx + shift) % 26]
        elif char in upper_set:
            idx = uppercase.index(char)
            result += uppercase[(idx + shift) % 26]
        else:
            result += char
    return result

def get_shift():
    while True:
        value = input('Number of shifts: ')
        if value.lower() == 'exit':
            exit('\n👋 Exiting program.')
        try:
            return int(value)
        except ValueError:
            print('❌ Please enter a valid number or type "exit".\n')

def main():
    while True:
        to_do = input("\nEnter 'e' for encryption, 'd' for decryption or 'exit': ").lower()
        if to_do == 'exit':
            print('\n' + ' Thank you '.center(30, '*'))
            break
        if to_do not in ['e', 'd']:
            print('❌ Invalid response. Try again.')
            continue

        message = input('Enter the message: ')
        shift = get_shift()
        if to_do == 'd':
            shift = -shift

        result = cipher(message, shift)
        print(f"\n🔐 Text after {'encryption' if to_do == 'e' else 'decryption'}: {result}")

        again = input("\nDo you want to continue? [y/n]: ").lower()
        if again != 'y':
            print('\n' + ' Thank you '.center(30, '*'))
            break

# Run the program
main()