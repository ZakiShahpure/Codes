def wordSplit(file_path):
    with open(file_path, "r") as f:
        for line in f:
            words = line.split()
            newLine = " # ".join(words)
            print(newLine)
wordSplit("Practice set1 file")
