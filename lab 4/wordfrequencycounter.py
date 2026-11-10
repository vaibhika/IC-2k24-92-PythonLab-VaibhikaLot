
# Word Frequency Counter using Dictionary

# Take paragraph input
paragraph = input("Enter a paragraph: ")

# Check empty input
if paragraph.strip() == "":
    print("Please enter a valid paragraph!")

else:

    # 1. Convert into lowercase
    paragraph = paragraph.lower()

    # Remove punctuation without using any library
    punctuation = ".,!?;:'\"()[]{}-"

    clean_text = ""

    for ch in paragraph:
        if ch not in punctuation:
            clean_text += ch

    # Split paragraph into words
    words = clean_text.split()

    # 2. Count frequency using dictionary and get()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Frequencies:")
    print(frequency)


    # 3. Print Top N words
    n = int(input("\nEnter N for top N words: "))

    # Sort by frequency (highest first)
    # If frequency is same, sort alphabetically
    sorted_words = sorted(
        frequency.items(),
        key=lambda x: (-x[1], x[0])
    )

    print("\nTop", n, "Words:")

    for word, count in sorted_words[:max(0, n)]:
        print(word, "->", count)


    # 4. Words appearing exactly once
    once_words = sorted([
        word for word, count in frequency.items()
        if count == 1
    ])

    print("\nWords Appearing Exactly Once:")
    print(once_words)


    # 5. Invert dictionary
    inverted = {}

    for word, count in frequency.items():

        if count not in inverted:
            inverted[count] = []

        inverted[count].append(word)

    # Sort each list alphabetically
    for count in inverted:
        inverted[count].sort()

    print("\nInverted Dictionary:")
    print(inverted)


    # 6. Group words by length
    length_groups = {}

    for word in frequency:

        length = len(word)

        if length not in length_groups:
            length_groups[length] = []

        length_groups[length].append(word)

    # Sort words in each group
    for length in length_groups:
        length_groups[length].sort()

    print("\nWords Grouped by Length:")
    print(length_groups)


    # 7. Search for a word
    search_word = input("\nEnter word to search: ").lower()

    # Remove punctuation from search word
    clean_search = ""

    for ch in search_word:
        if ch not in punctuation:
            clean_search += ch

    search_word = clean_search.strip()

    if search_word in frequency:
        print(search_word, "appears",
              frequency[search_word], "times.")
    else:
        print("Word not found!")
