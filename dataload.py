TRAIN_FILE = "/home/user/Projects/word-seg/out/crf-train/all.txt"
TEST_FILE = "/home/user/Projects/word-seg/out/crf-test/0.txt"

def load_dataset():
    train_sents = []
    test_sents = []
    temp_sent = []
    with open(TRAIN_FILE, 'r', encoding='UTF-8') as f:
        for line in f:
            if line.strip() != '':
                ss = line.strip().split(' ')
                temp_sent.append(ss)
            else:
                train_sents.append(temp_sent)
                temp_sent = []
    with open(TEST_FILE, 'r', encoding='UTF-8') as f:
        for line in f:
            if line.strip() != '':
                ss = line.strip().split(' ')
                temp_sent.append(ss)
            else:
                test_sents.append(temp_sent)
                temp_sent = []
    return train_sents, test_sents
