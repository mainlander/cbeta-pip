import json
import re

DICT_FILE = "dicts_all.json"
DILA_FILE = "dila.json"

def load_dicts():
    words = {}
    with open(DICT_FILE, 'r', encoding='UTF-8') as f:
        json_str = f.read()
        words = json.loads(json_str)
    return words

def get_features(input_str, char_features, words):
    for dic in words:
        i = 0
        end = len(input_str)
        while i < len(input_str) - 1:
            if i == end:
                i += 1
                end = len(input_str)
                continue
            substr = input_str[i:end]
            if len(substr) <= 1:
                i += 1
                end = len(input_str)
                continue
            if substr in words[dic]:
                for k in range(i, end):
                    if k == i:
                        char_features[k][dic] = 'B'
                    elif k == end - 1:
                        char_features[k][dic] = 'E'
                    else:
                        char_features[k][dic] = 'I' 
                i = end
            else:
                if i == end:
                    i += 1
                    end = len(input_str)
                else:
                    end -= 1


def load_dicts2():
    words = {'dila':[], 'fk':[], 'gy':[], 'ch':[] }
    with open(DICT_FILE, 'r', encoding='UTF-8') as f:
        json_str = f.read()
        dicts = json.loads(json_str)
        for w in dicts:
            terms = dicts[w]
            for t in terms:
                for d in terms[t]:
                    if t not in words[d]:
                        words[d].append(t)

    with open(DILA_FILE, 'r', encoding='UTF-8') as f:
        json_str = f.read()
        dilas = json.loads(json_str)
        for s in dilas:
            terms = s.split('/')
            for t in terms:
                if t not in words['dila']:
                    words['dila'].append(t)
    return words

def get_features2(input_str, char_features, words):
    for i in range(len(input_str) - 1):
        get_features_from_dicts(input_str[i:], char_features[i:], words)

def get_features_from_dicts(input_str, char_features, words):
    first_char = input_str[0]
    if first_char not in words:
        return
    terms = words[first_char]

    for k in terms:
        v = terms[k]
        if len(input_str) < len(k):
            continue
        if not input_str.startswith(k):
            continue
        update_features(char_features[0], v, 'B')
        for i in range(1, len(k) - 2):
            update_features(char_features[i], v, 'I')
        update_features(char_features[len(k) - 1], v, 'E')


def update_features(features, dicts, feature):
    for d in dicts:
        if features[d] == 'B':
            if feature == 'E' or feature == 'I':
                features[d] = 'I'
        elif features[d] == 'E':
            if feature == 'B' or feature == 'I':
                features[d] = 'I'
        elif features[d] == 'I' or features[d] == 'N':
            features[d] = feature

def tag_zh_str(input_str, mode, words):
    if len(input_str) == 1:
        r = "{0} zh N N N N".format(input_str)
        if mode == 'learn':
            r += " S"
        r += '\n'
        return r

    temp_d = {
              'dila' : 'N',
              'fk' : 'N',
              'gy' : 'N',
              'ch' : 'N'
    }
    char_features = [ temp_d.copy()  for i in range(len(input_str)) ] #[temp_d] * len(input_str)
    get_features(input_str, char_features, words)
    r = ''

    for i in range(len(char_features)):
        f = char_features[i]
        r += input_str[i] + " zh"
        r += ' ' + f['dila']
        r += ' ' + f['fk']
        r += ' ' + f['gy']
        r += ' ' + f['ch']
        if mode == 'learn':
            if i == 0:
                r += " B"
            elif i == (len(input_str) - 1):
                r += " E"
            else:
                r += " I"
        r += '\n'
    return r

def tag_string3(s, words, mode='learn'):
    if s is None or len(s) == 0:
        return ''

    r = ''
    if re.match(r'^\d+$', s):
        r = "{0} num N N N N".format(s)
        if mode == 'learn':
            r += " S"
        return r + "\n"

    if re.match(r'^[a-zA-Z]+$', s):
        r = "{0} en N N N N".format(s)
        if mode == 'learn':
            r += " S"
        return r + "\n"

    if re.match(r'^[ \.\(\)\[\]\-　．。，、？！：；「」『』《》＜＞〈〉〔〕［］【】〖〗（）…—◎]+$', s):
        r = "\n{0} PUNC N N N N".format(s)
        if mode == 'learn':
            r += " S"
        return r + "\n\n"

    
    r = tag_zh_str(s, mode, words)
    return r


if __name__ == '__main__':
    words = load_dicts()
#    out_str = json.dumps(words, sort_keys=True, indent=4, separators=(',', ': '))
#    with open('dicts_all.json', 'w', encoding='UTF-8') as outf:
#        outf.write(out_str)
#    print(words['ch'])
    test_str = '佛在舍衛國祗樹給孤獨園'
    res = tag_string3(test_str, words)
    print(res)


