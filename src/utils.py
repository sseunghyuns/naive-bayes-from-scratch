def get_accuracy(result):
    acc = 0
    for k,v in result.items():
        if 's' in k: # true label: spam
            acc += v['pred_label'] == 'spam'
        elif 'h' in k: # true label: ham
            acc+= v['pred_label'] == 'ham'
    return acc / len(result.keys())
