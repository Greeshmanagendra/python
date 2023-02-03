def is_triple_double(word):
    i=0
    count=0
    while i<len(word)-1:
      if word[i]==word[i+1]:
         count=count+1
         if count==3:
            return True
         i=i+2
      else:
         i=i+1
    return False
def find_triple_double():
    fin=input("enter a word")
    res=is_triple_double(fin)
    if res:
      print("three consecutive",fin)
    else:
      print("three ",fin)