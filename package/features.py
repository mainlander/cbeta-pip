import sklearn_crfsuite

TRAIN_FILE = "~/Projects/word-seg/out/crf-train.txt"

def word2features(sent, i):
    word = sent[i][0]
    wtype = sent[i][1]
    
    d1 = sent[i][2]
    d2 = sent[i][3]
    d3 = sent[i][4]
    d4 = sent[i][5]
    
    features = {
        'U02':word,
        'U12':wtype,
        #'U31':d1,
        #'U32':d2,
        #'U33':d3,
        #'U34':d4,
    }

    if i > 0:
        prev_word = sent[i - 1][0]
        prev_wtype = sent[i - 1][1]
        prev_d1 = sent[i - 1][2]
        prev_d2 = sent[i - 1][3]
        prev_d3 = sent[i - 1][4]
        prev_d4 = sent[i - 1][5]
        features.update({
            'U01':prev_word,
            'U11':prev_wtype,
            'U05':"{0}/{1}".format(prev_word, word),
            'U16':"{0}/{1}".format(prev_wtype, wtype),
            #'U36':prev_d1,
            #'U37':prev_d2,
            #'U38':prev_d3,
            #'U39':prev_d4,
            #'U40':"{0}/{1}".format(prev_d1, d1),
            #'U41':"{0}/{1}".format(prev_d2, d2),
            #'U42':"{0}/{1}".format(prev_d3, d3),
            #'U43':"{0}/{1}".format(prev_d4, d4),
        })
    else:
        features['BOS'] = True

    if i > 1:
        prev_word = sent[i - 1][0]
        prev_wtype = sent[i - 1][1]
        prev2_word = sent[i - 2][0]
        prev2_wtype = sent[i - 2][1]
        prev_d1 = sent[i - 1][2]
        prev_d2 = sent[i - 1][3]
        prev_d3 = sent[i - 1][4]
        prev_d4 = sent[i - 1][5]
        prev2_d1 = sent[i - 2][2]
        prev2_d2 = sent[i - 2][3]
        prev2_d3 = sent[i - 2][4]
        prev2_d4 = sent[i - 2][5]
        features.update({
            'U00':prev2_word,
            'U10':prev2_wtype,
            'U15':"{0}/{1}".format(prev2_wtype, prev_wtype),
            'U20':"{0}/{1}/{2}".format(prev2_wtype, prev_wtype, wtype),
            #'U44':prev2_d1,
            #'U45':prev2_d2,
            #'U46':prev2_d3,
            #'U47':prev2_d4,
            #'U48':"{0}/{1}".format(prev2_d1, prev_d1),
            #'U49':"{0}/{1}/{2}".format(prev2_d1, prev_d1, d1),
            #'U50':"{0}/{1}".format(prev2_d2, prev_d2),
            #'U51':"{0}/{1}/{2}".format(prev2_d2, prev_d2, d2),
            #'U52':"{0}/{1}".format(prev2_d3, prev_d3),
            #'U53':"{0}/{1}/{2}".format(prev2_d3, prev_d3, d3),
            #'U54':"{0}/{1}".format(prev2_d4, prev_d4),
            #'U55':"{0}/{1}/{2}".format(prev2_d4, prev_d4, d4),
        })

    if i < len(sent) - 1:
        after_word = sent[i + 1][0]
        after_wtype = sent[i + 1][1]
        after_d1 = sent[i + 1][2]
        after_d2 = sent[i + 1][3]
        after_d3 = sent[i + 1][4]
        after_d4 = sent[i + 1][5]
        features.update({
            'U03':after_word,
            'U13':after_wtype,
            'U06':"{0}/{1}".format(word, after_word),
            'U17':"{0}/{1}".format(wtype, after_wtype),
            #'U56':after_d1,
            #'U57':after_d2,
            #'U58':after_d3,
            #'U59':after_d4,
            #'U60':"{0}/{1}".format(d1, after_d1),
            #'U61':"{0}/{1}".format(d2, after_d2),
            #'U62':"{0}/{1}".format(d3, after_d3),
            #'U63':"{0}/{1}".format(d4, after_d4),
        })
    else:
        features['EOS'] = True


    if i < len(sent) - 2:
        after_word = sent[i + 1][0]
        after_wtype = sent[i + 1][1]
        after_d1 = sent[i + 1][2]
        after_d2 = sent[i + 1][3]
        after_d3 = sent[i + 1][4]
        after_d4 = sent[i + 1][5]
        after2_word = sent[i + 2][0]
        after2_wtype = sent[i + 2][1]
        after2_d1 = sent[i + 2][2]
        after2_d2 = sent[i + 2][3]
        after2_d3 = sent[i + 2][4]
        after2_d4 = sent[i + 2][5]
        features.update({
            'U04':after2_word,
            'U14':after2_wtype,
            'U18':"{0}/{1}".format(after_wtype, after2_wtype),
            'U22':"{0}/{1}/{2}".format(wtype, after_wtype, after2_wtype),
            #'U64':after2_d1,
            #'U65':after2_d2,
            #'U66':after2_d3,
            #'U67':after2_d4,
            #'U68':"{0}/{1}".format(after_d1, after2_d1),
            #'U69':"{0}/{1}/{2}".format(d1, after_d1, after2_d1),
            #'U70':"{0}/{1}".format(after_d2, after2_d2),
            #'U71':"{0}/{1}/{2}".format(d2, after_d2, after2_d2),
            #'U72':"{0}/{1}".format(after_d3, after2_d3),
            #'U73':"{0}/{1}/{2}".format(d3, after_d3, after2_d3),
            #'U74':"{0}/{1}".format(after_d4, after2_d4),
            #'U75':"{0}/{1}/{2}".format(d4, after_d4, after2_d4),
        })

    if i > 0 and i < len(sent) - 1:
        prev_wtype = sent[i - 1][1]
        after_wtype = sent[i + 1][1]
        prev_d1 = sent[i - 1][2]
        after_d1 = sent[i + 1][2]
        prev_d2 = sent[i - 1][3]
        after_d2 = sent[i + 1][3]
        prev_d3 = sent[i - 1][4]
        after_d3 = sent[i + 1][4]
        prev_d4 = sent[i - 1][5]
        after_d4 = sent[i + 1][5]
        features.update({
            'U21':"{0}/{1}/{2}".format(prev_wtype, wtype, after_wtype),
            #'U76':"{0}/{1}/{2}".format(prev_d1, d1, after_d1),
            #'U77':"{0}/{1}/{2}".format(prev_d2, d2, after_d2),
            #'U78':"{0}/{1}/{2}".format(prev_d3, d3, after_d3),
            #'U79':"{0}/{1}/{2}".format(prev_d4, d4, after_d4),
        })

    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [ss[-1] for ss in sent]

def sent2tokens(sent):
    return [ss[0] for ss in sent]


