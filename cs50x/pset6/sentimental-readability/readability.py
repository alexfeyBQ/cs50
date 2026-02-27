from cs50 import get_string


def main():
    # Ask for text
    text = get_string("Text: ")

    # Give the grade level of the text
    grade(text)


def grade(text):
    # Parameters
    words = 0
    letters = 0
    sentences = 0

    # Update parameters for calculations (1/2)
    if len(text) > 0:
        words += 1

    # Update parameters for calculations (2/2)
    for _, c in enumerate(text):
        if c.isalpha():
            letters += 1
        if c == " ":
            words += 1

        if c in ['.', '?', '!']:
            sentences += 1

    # Determine grade level
    L = letters / words * 100  # Average number of letters per 100 words
    S = sentences / words * 100  # Average number of sentences per 100 words

    index = 0.0588 * L - 0.296 * S - 15.8  # Coleman-Liau index
    grade_level = round(index)

    # Print grade level
    if grade_level < 1:
        print("Before Grade 1")
    elif grade_level > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade_level}")


if __name__ == "__main__":
    main()
