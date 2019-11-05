import pickle

with open("model.pkl", "rb") as model_pk:
    model = pickle.load(model_pk)

type(model)

with open("vectorizer.pkl", "rb") as vectorizer_pk:
    vectorizer = pickle.load(vectorizer_pk)

def predict(sent):
    vec = vectorizer.transform([sent]).todense()
    return model.predict(vec)[0]
