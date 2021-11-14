def get_unique_words(data, label):
    words_list = []
    for _, v in data[label].items():
        text_list = v.lower().split()
        for word in text_list:
            if word not in words_list:
                words_list.append(word)
    return words_list

def get_word_frequency(data, label, word_list):
    freq_of_word = {}
    total_emails =len(data[label])
    for word in word_list:
        counter=0
        for _, v in data[label].items():
            text_list = v.lower().split()
            if word in text_list:
                counter+=1
        freq_of_word[word] = (counter) / (total_emails)
    return freq_of_word

def get_test_words(data, train_spam_words, train_ham_words):
    test_result = {}
    for label in ['spam', 'ham']:
        temp_dict = {}
        for k,v in data[label].items():
            test_word_list = []

            text_list = v.lower().split()

            for word in text_list:
                if word in train_spam_words:
                    if len(word)>1:
                        test_word_list.append(word)
                elif word in train_ham_words:
                    if len(word)>1:
                        test_word_list.append(word)
                else:
                    pass
            temp_dict[k] = test_word_list
        test_result[label] = temp_dict
    return test_result