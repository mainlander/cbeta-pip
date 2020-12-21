import joblib
import re
import sys
from features import *
from dicts import load_dicts, tag_string3

words = load_dicts()

crf = joblib.load('crfmodel.pkl')

def split_parts(sentence):
    result = []
    sent_parts = re.split(r'(\d+|[a-zA-Z]+|[ \.\(\)\[\]\-　．。，、？！：；「」『』《》＜＞〈〉〔〕［］【】〖〗（）…—◎]+)', sentence)
    result.extend(sent_parts)
    return result

def tag_string(sentence):
    result = []
    sent_parts = re.split(r'(\d+|[a-zA-Z]+|[ \.\(\)\[\]\-　．。，、？！：；「」『』《》＜＞〈〉〔〕［］【】〖〗（）…—◎]+)', sentence)
    sent_lines = ""
    for part in sent_parts:
        sent_lines += tag_string3(part, words)
    for row in sent_lines.split('\n'):
        if row.strip() != '':
            ss = row.strip().split(' ')
            result.append(ss[:-1])
    return result


def tag_string_old(sent):
    result = []
    for s in sent:
        if re.match(r'^\d+$', s):
            result.append([ s, 'num' ])

        if re.match(r'^[a-zA-Z]+$', s):
            result.append([ s, 'en' ])

        if re.match(r'^[ \.\(\)\[\]\-　．。，、？！：；「」『』《》＜＞〈〉〔〕［］【】〖〗（）…—◎]+$', s):
            result.append([ s, 'PUNC' ])
        else:
            result.append([ s, 'zh' ])
    return result

def cut(sentence):
    parts = split_parts(sentence)
    result = []
    for part in parts:
        test_sent = tag_string(part)
        test_sents = [ test_sent ]
        X_test = [sent2features(s) for s in test_sents]
        y_pred = crf.predict(X_test)
        for i in range(len(y_pred[0])):
            label = y_pred[0][i]
            w = part[i]
            if label == 'S':
                result.append(w)
            elif label == 'B':
                result.append(w)
            elif label == 'I' or label == 'E':
                result[-1] += w
    return result

if __name__ == '__main__':
    #test_str = '一時，佛在舍衛國祗樹給孤獨園。與大比丘眾千二百五十人俱。'
    test_str = sys.argv[1]
    res = cut(test_str)
    print(res)

