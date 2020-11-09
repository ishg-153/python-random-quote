import random

def primary():
   print("Keep it logically awesome.")

f = open("quotes.txt")
quotes = f.readlines()
f.close()
last = 13
rnd = random.randint(0, last) 
if rnd <= 11:
  rnd2 = rnd + 2
else:
  rnd2 = rnd - 2
print(quotes[rnd],quotes[rnd2])

if __name__== "__main__":
  primary()
