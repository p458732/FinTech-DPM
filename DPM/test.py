import pickle


with open('./27/results', 'rb') as f:
    a = pickle.load(f)
    
    print(a)