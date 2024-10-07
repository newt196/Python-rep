import argparse
import itertools  


# need to define the min | max | and args for what the wordlist will contain
# EX abcd and all iterations on what is defined
def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, 'w') as file:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(characters, repeat=length):
                word = ''.join(combination)
                file.write(word + '\n')
parser = argparse.ArgumentParser(description="Generate a custom wordlist similar to crunch.")

# Need to define some command-line logic and arguments using add_argument method
parser.add_argument("-c", "--characters", type=str, default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                    help="Set of characters to include in the wordlist")
parser.add_argument("-min", "--min_length", type=int, default=1, help="Minimum length of the words")
parser.add_argument("-max", "--max_length", type=int, default=3, help="Maximum length of the words")
parser.add_argument("-o", "--output_file", type=str, default="you_know_what_it_is.txt", help="Output file name")

args = parser.parse_args()

generate_wordlist(args.characters, args.min_length, args.max_length, args.output_file)

print(f"[+] Something was created :) {args.output_file}")

# Output should be that all iterations of letters and numbers if defined are created and thown in a .txt created in the dir where 
# it was ran
# Output is kind of large
# Kind of attack is too broad and should only be ran  if
# There is know information about the target or target hash.
# There is a second computer with 1 GPU we can run overnight
# There is a mining rig we can quickly run through as a preliminary crack
# Not optimal if none of these are had
# This kind of wordlist is over 15gigs plus
