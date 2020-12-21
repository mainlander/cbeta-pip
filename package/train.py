import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
import joblib

import dataload
from features import *

train_sents, test_sents = dataload.load_dataset()

X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

X_test = [sent2features(s) for s in test_sents]
y_test = [sent2labels(s) for s in test_sents]

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
#    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

labels = list(crf.classes_)

y_pred = crf.predict(X_test)
score = metrics.flat_f1_score(y_test, y_pred,
                      average='weighted', labels=labels)

joblib_file = "crfmodel.pkl"
joblib.dump(crf, joblib_file)

print(score)
