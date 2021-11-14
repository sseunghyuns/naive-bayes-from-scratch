def mul_probs(probs_list):
    final_prob = 1
    for prob in probs_list:
        final_prob = final_prob * prob
    return final_prob

def bayesian_spam_filters(test_data, train_freq_spam, train_freq_ham, train_emails_number, threshold=0.6):
    p_s = 0.5
    q_s = 0.5
    epsilon = 1e-100
    labels = ['spam', 'ham']
    train_spam_emails, train_ham_emails = train_emails_number
    result = {}

    for label in labels:
        for k, words in test_data[label].items():
            p_w_list = []
            q_w_list = []
            for word in words:
                # Calculate p(word)
                try:
                    p_w = (train_freq_spam[word])
                except:
                    p_w = 1/(100+1) # total spam emails + 1


                # Calculate q(word)
                try:
                    q_w = train_freq_ham[word]
                except:
                    q_w = 1/(100+1) # total ham emails + 1

                p_w_list.append(p_w)
                q_w_list.append(q_w)

            final_p_w = mul_probs(p_w_list)
            final_q_w = mul_probs(q_w_list)
        
            
            r_w = final_p_w / (final_p_w + final_q_w + epsilon)

            num = f"s{k.zfill(2)}" if label == 'spam' else f"h{k.zfill(2)}"

            result[num] = {'r' : r_w,
                           'pred_label' : 'spam' if r_w > threshold else 'ham'}

    return result