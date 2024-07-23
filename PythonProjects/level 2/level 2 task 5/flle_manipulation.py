import re
def read(path) :
  with open(path , "r" ) as file:
      return file.read()
def counting(text) :
    words =text.lower().split()
    counts = {}
    for w in words :
        w = re.sub(r'\W+' , "",w)
        if w in counts :
            counts[w] += 1
        else :
            counts[w] = 1
    return counts
def display(counts):
    for w in sorted(counts):
        print(f"{w} : {counts[w]}")
def main():
    path = "c:\\Users\punee\Desktop\Cognifyz\PythonProject\level 2\level 2 task 5\\text1.txt"
    text = read(path)
    counts = counting(text)
    display(counts)
main()