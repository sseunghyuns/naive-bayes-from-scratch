from src.load_data import read_csv
from src.preprocess import get_unique_words, get_word_frequency, get_test_words
from src.naive_bayes import bayesian_spam_filters
from src.utils import get_accuracy

if __name__ == '__main__':
    
    # path
    train_spam_path = './datasets/train/dataset_spam_train100.csv'
    train_ham_path = './datasets/train/dataset_ham_train100.csv'

    test_spam_path = './datasets/test/dataset_spam_test20.csv'
    test_ham_path = './datasets/test/dataset_ham_test20.csv'

    # Threshold
    threshold=0.6
    
    # Data shape
    train_emails_number = (100, 100) # (spam emails, ham emails)
    
    # Load Train data
    train_spam = read_csv(train_spam_path)
    train_ham = read_csv(train_ham_path)
    train_spam.update(train_ham) # concat two dictionaries

    # Load Test data
    test_spam = read_csv(test_spam_path, 'test')
    test_ham = read_csv(test_ham_path, 'test')
    test_spam.update(test_ham)  # concat two dictionaries

    # Get unique words from train data.
    train_spam_words = get_unique_words(train_spam, 'spam')
    train_ham_words = get_unique_words(train_spam, 'ham')

    # Compute frequency(P(E|S), P(E|H)) of train data. 
    train_freq_spam = get_word_frequency(train_spam, 'spam', train_spam_words)
    train_freq_ham = get_word_frequency(train_ham, 'ham', train_ham_words)

    # Get words from test data.
    test_words = get_test_words(test_spam, train_spam_words, train_ham_words)

    # Compute spam probability from bayesian rule.  
    result = bayesian_spam_filters(test_words,train_freq_spam, train_freq_ham, train_emails_number, threshold=threshold)
    acc = get_accuracy(result)
    
    print(f"Threshold: {threshold}\n")
    print(result)
    print(f"\nAccuracy: {acc}")
