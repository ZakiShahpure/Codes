import pickle

# Object to pickle
data = {'name':'Name1', 'age':'30', 'city':'Uganda'}

# Pickeling - saving the object to a file
with open('data.pickle', 'wb') as file:
    a=pickle.dump(data, file)

print(a)

# Unpickeling - loading the object from the file
with open("data.pickle", 'rb') as file:
    loaded_data = pickle.load(file)

# Displaying the unpickled data
print(loaded_data)