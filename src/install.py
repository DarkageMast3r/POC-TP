import nltk

import model



classifier = model.create(n_classes = 1)
model.save(classifier, model.default_save_filename)

nltk.download("wordnet")
print("Installation succeeded");
