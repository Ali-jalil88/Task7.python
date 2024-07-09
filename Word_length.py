words=["Hallo","Wie","Geths","Ihnen","Heute","Is","Dienstag"]
def words_list(n):
  for k in n:
    print(k,len(k))
words_list(words)
dictionary_comprehension ={k:len(k) for k in words}
print(dictionary_comprehension)