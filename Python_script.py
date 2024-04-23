import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def remove_stopwords(content):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(content)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def count_letter_frequency(content):
    content = content.replace(" ", "")  # Remove spaces before counting letters
    letter_freq = Counter(content)
    return letter_freq

def print_letter_frequency(letter_freq):
    for letter, freq in letter_freq.items():
        print(f"The letter '{letter}' appears {freq} times.")

def main():
    file_path = "/Assignment 2/random_paragraphs.txt"
    
    # Read the contents of the text file
    content = read_file(file_path)
    
    # Remove stopwords from the text
    filtered_content = remove_stopwords(content)
    
    # Count letter frequency
    letter_freq = count_letter_frequency(filtered_content)
    
    # Print letter frequency
    print_letter_frequency(letter_freq)
    
    # Count of letters in original and filtered content
    count_of_letters_original = sum(1 for char in content if char.isalpha())
    count_of_letters_filtered = sum(1 for char in filtered_content if char.isalpha())

    # Count total number of words before removing stopwords
    total_words_before = len(nltk.word_tokenize(content))
    
    # Count total number of words after removing stopwords
    total_words_after = len(nltk.word_tokenize(filtered_content))
    print()
    print(f"Count of Characters in original article: {count_of_letters_original:,}")
    print(f"Count of Characters in filtered article: {count_of_letters_filtered:,}")
    print()
    print(f"Total number of words before removing stopwords: {total_words_before}")
    print(f"Total number of words after removing stopwords: {total_words_after}")

if __name__ == "__main__":
    main()