
import random

# Helper: Luhn algorithm to generate a valid credit card number
def generate_luhn_number():
    def completed_number(prefix, length):
        number = prefix
        while len(number) < (length - 1):
            number += str(random.randint(0, 9))
        digits = [int(d) for d in number]
        odd_sum = sum(digits[-1::-2])
        even_sum = 0
        for d in digits[-2::-2]:
            d2 = d * 2
            if d2 > 9:
                d2 -= 9
            even_sum += d2
        checksum = (odd_sum + even_sum) % 10
        check_digit = (10 - checksum) % 10
        return number + str(check_digit)
    # Use a random prefix (Visa, MasterCard, etc.)
    prefixes = ['4', '5', '51', '52', '53', '54', '55', '6011', '34', '37']
    prefix = random.choice(prefixes)
    return completed_number(prefix, 16)

# Helper: Format credit card number as '1234 5678 9012 3456'
def format_cc_number(cc_number):
    return ' '.join([cc_number[i:i+4] for i in range(0, 16, 4)])

# Sentence templates with a placeholder for the credit card number
SENTENCE_TEMPLATES_WITH_NUMBER = [
    "My new credit card with the number {cc} arrived in the mail yesterday afternoon.",
    "Please use the credit card number {cc} for processing the payment transaction.",
    "The sixteen-digit number {cc} was clearly printed on the front of the envelope.",
    "I carefully memorized my new credit card number: {cc} for future reference.",
    "The cashier at the store entered the card number {cc} during the checkout process.",
    "I received an important message containing the credit card number {cc} in the text.",
    "For your official records, my primary credit card number is {cc} for billing purposes.",
    "The security code {cc} is now active and ready for online transactions.",
    "I wrote down the card number {cc} in my notebook just in case I forget it.",
    "The package delivery included the receipt with the card number {cc} printed clearly.",
    "My backup credit card with the number {cc} is stored safely in my wallet.",
    "The fraud detection system flagged the card number {cc} as potentially suspicious activity.",
    "I successfully used the credit card {cc} to book the hotel room for our vacation.",
    "The customer service agent asked for the card number {cc} over the secure phone line.",
    "I noticed an unusual charge on my statement for the card ending in {cc}.",
]

# Sentence templates with no numbers
SENTENCE_TEMPLATES_NO_NUMBER = [
    "The weather was absolutely perfect for taking a long walk in the beautiful city park.",
    "She finally finished reading her favorite novel last night before going to bed.",
    "The fluffy cat slept peacefully on the warm windowsill throughout the entire afternoon.",
    "He decided to try a completely new recipe for dinner that he found online.",
    "The important business meeting was unexpectedly rescheduled to next week due to conflicts.",
    "They thoroughly enjoyed a quiet and relaxing evening at home with their family.",
    "The beautiful garden is currently blooming with colorful flowers of various species.",
    "She carefully painted a stunning landscape yesterday using watercolors and brushes.",
    "The highly anticipated movie received excellent reviews from professional critics worldwide.",
    "He eventually found his lost keys hidden under the comfortable living room couch.",
    "The energetic children played outside in the backyard until the sun finally set.",
    "She thoughtfully wrote a heartfelt letter to her best friend who lives overseas.",
    "The popular coffee shop was extremely busy this morning with many customers.",
    "He quietly listened to classical music while working on his important project.",
    "The friendly dog barked loudly at the passing car that drove down the street.",
]

def generate_sentence(with_number=True):
    if with_number:
        template = random.choice(SENTENCE_TEMPLATES_WITH_NUMBER)
        cc_number = format_cc_number(generate_luhn_number())
        return template.format(cc=cc_number)
    else:
        return random.choice(SENTENCE_TEMPLATES_NO_NUMBER)

def get_num_sentences():
    while True:
        try:
            n = int(input("How many sentences to generate? (100-200): "))
            if 100 <= n <= 200:
                return n
            else:
                print("Please enter a number between 100 and 200.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    num_sentences = get_num_sentences()
    # Decide at which indices to insert numberless sentences
    sentences = []
    i = 0
    while i < num_sentences:
        # Decide if this should be a numberless sentence
        if len(sentences) == 0:
            next_no_number = random.randint(3, 7)
        if (i == next_no_number):
            sentences.append(generate_sentence(with_number=False))
            # Schedule next numberless sentence
            next_no_number += random.randint(3, 7)
        else:
            sentences.append(generate_sentence(with_number=True))
        i += 1
    for s in sentences:
        print(s)

if __name__ == "__main__":
    main()

