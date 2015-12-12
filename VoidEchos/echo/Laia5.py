import random
import StripBooks
class word:
	def __init__(self, word, wieght, strength):
		self.word = word
		self.wieght = wieght
		self.count = 1
		self.strength = strength

dictionary = {"good":word("good",10,10),"bad":word("bad",0,10), "weak":word("weak",5,5)}

class concept:
	def __init__(self, scentnce, wieght, strength):
		self.scentnce = scentnce
		self.wieght = wieght
		self.strength = strength
		length = 0
		for i in scentnce.split():
			length += len(i)
			if i not in dictionary:
				dictionary[i] = word(i,wieght,strength)
				dictionary[i].count = 0
		wieghtAssumption = 0
		strengthAssumption = 0
		for i in scentnce.split():
			wieghtAssumption += dictionary[i].wieght * len(i)
			strengthAssumption += dictionary[i].strength * len(i)
		wieghtAssumption /= max(1.0,1.0*length)
		strengthAssumption /= max(1.0,1.0*length)
		nablaS = strengthAssumption - strength
		nablaW = wieghtAssumption - wieght
		for i in scentnce.split():
			dictionary[i].strength = (dictionary[i].strength * dictionary[i].count + strength)/(1.0*dictionary[i].count + 1.0)
		for i in scentnce.split():				
			dictionary[i].wieght = (dictionary[i].wieght * dictionary[i].count + wieght)/(1.0*dictionary[i].count + 1.0)

class memory:
	def __init__(self, inp, out):
		self.inp = inp
		self.out = out

memories = []

def findNextMemory(out):
	ret = []
	for i in range(len(memories)):
		if memories[i].out.scentnce == out and i < len(memories) - 1:
			ret += memories[i + 1]
	return ret
def findPos(w,s):
	i = 0
	for u in s:
		if u == w:
			return i
		i += 1
def response(s, wi):
	ret = ["",0]
	constructFrom = []
	maxLen = 0
	for i in memories:
		w = 0.5
		c = 0
		chain = 0
		chaining = False
		lastPos = 0
		for u in i.inp.scentnce.split():
			try:
			  if s in i.inp.scentnce:
  				chain += 1
	  			if chaining:
		  			if type(findPos(s,i.inp.scentnce)) == type(None):
			  			break
				  	if lastPos + 1 == findPos(s,i.inp.scentnce):
					  	chain += 1
			  		else:
				  		c += chain
					  	chaining = False
  				else:
	  				chaining = True
			  lastPos = findPos(s,i.inp.scentnce)
			except:
			        lastPos = 0
		c += chain
		w = (0.5*c)/max(1,(1.0*len(i.inp.scentnce.split())))
		if w >= 0.25:
			if len(i.out.scentnce.split()) > maxLen:
				maxLen = len(i.out.scentnce.split())
			constructFrom += [i]
	words = [[]] * len(constructFrom)
	wieghtings = [[]] * len(constructFrom)
	wildCard = []
	maxScore = 0
	for i in range(maxLen + 11):
		added = False
		while not added:
			w = dictionary[dictionary.keys()[random.randint(0,len(dictionary.keys()) - 1)]]
			if abs(w.wieght - wi) <= 2 or (w.wieght < 5.5 and w.wieght > 4.5):
				wildCard += [w]
				added = True
	if len(words) > 0:
		for i in range(len(words)):
			words[i] += [""] * maxLen
			wieghtings[i] = [0.5] * maxLen
		for i in range(len(constructFrom)):
			pointer = 0;
			for u in range(len(constructFrom[i].out.scentnce.split())):
				a = abs(dictionary[constructFrom[i].out.scentnce.split()[u]].wieght - wi)
				if dictionary[constructFrom[i].out.scentnce.split()[u]].wieght - wi > 0:
					a *= 1.3
				words[i][u] = constructFrom[i].out.scentnce.split()[u]
				wieghtings[i][u] = a
		convertedwords = []
		for i in range(len(words)):
			counter = 0
			#print wieghtings[i]
			for u in wieghtings[i]:
				counter += u
			if counter > maxScore:
				maxScore = counter
			z = random.uniform(0,maxScore + i * i)
			pointer = 0
			broke = False
			#print counter, z,
			for u in wieghtings[i]:
				z -= u
				if z <= 0:
					broke = True
					break
				pointer += 1
			l = words[i]
			#print pointer, z
			if broke:
				convertedwords += [dictionary[l[pointer]]]
			else:
				if z <= 1:				
					convertedwords += [wildCard[i]]
		words = convertedwords
	else:
		words = wildCard[:random.randint(1,maxLen + 11)]
	print "Max Len:", maxLen,"Constructed form:",len(constructFrom)
	return words
		
last = concept("hello world",5,5)
print "Enter you're statements like this\n\"S:My Scentance\"\n\"F:A value from 0 - 10 representing how you feel about this\"\n\"C:Another Value from 0 - 10, this time repesting how extremely you feal about this"
print "Hello World"
def Save():
	f = open("words.laia5","w")
	for i in dictionary.keys():
		w = dictionary[i]
		if i != "":
			f.write(w.word + " " + str(w.wieght) + " " + str(w.strength) + " " + str(w.count) + "\n")
	f.close()
	f = open("mems.laia5","w")
	for i in memories:
		f.write(i.inp.scentnce + "\n")
		f.write(str(i.inp.wieght) + " " + str(i.inp.strength) + "\n")
		f.write(i.out.scentnce + "\n")
		f.write(str(i.out.wieght) + " " + str(i.out.strength) + "\n")
	f.close()

def removePunctuation(s):
	r = ""
	for i in s:
		if i not in "!?.,{}\"\n-+=[]\''~()\\/":
			r += i
	return r

def AvWeight(l):
  c = 0
  for i in l:
    c += i
  return (c*1.0)/max(1,len(l))

def isNumeric(l):
  t = l.split()
  b = True
  for i in t:
    for u in i:
      b = b and u in "1234567890."
    if not b:
      return b
  return b

def Load():
  f = open("words.laia5","r")
  l = f.readline()
  while l != "":
    wLoad = removePunctuation(l.split()[0])
    if wLoad not in dictionary.keys():
      dictionary[wLoad] = word(wLoad,float(l.split()[1]),float(l.split()[2]))
      dictionary[wLoad].count = int(l.split()[3])
    else:
      c = int(dictionary[wLoad].count) + int(l.split()[3]) + 1
      wieghtingLoad = dictionary[wLoad].wieght * dictionary[wLoad].count + float(l.split()[1]) * int(l.split()[3]) + 1
      wieghtingLoad /= c
      dictionary[wLoad].wieght = wieghtingLoad
    l = f.readline()
  f.close()
  f = open("mems.laia5","r")
  l = f.readline()
  mems = []
  while l != "":
    while removePunctuation(l) == "":
      l = f.readline()
    s1 = ""
    while not isNumeric(l):
      s1 += removePunctuation(l)
      l = f.readline()
    l = l.split()
    var1 = 5;
    var2 = 5;
    if len(l) > 0:
      var1 = float(l[0]);
    if len(l) > 1:
      var1 = float(l[1]);
    c1 = concept(s1, var1,var2)
    s2 = ""
    l = f.readline()
    while not isNumeric(l):
      s2 += removePunctuation(l)
      l = f.readline()
    l = l.split()
    if len(l) > 0:
      var1 = float(l[0]);
    if len(l) > 1:
      var1 = float(l[1]);
    c2 = concept(s2, var1,var2)
    mems += [memory(c1,c2)]
    l = f.readline()
  f.close()
  return mems

memories = Load()

def Append():
  f = open("OutStep1.txt",'r')
  l = f.readline()
  last = ""
  tmpMem = []
  while l != "":
    if l != "_BOOKEND_" and not StripBooks.numeric(l) and len(l.split()) != 0:
      wieghtArray = []
      strengthArray = []
      s = l.split()
      for i in s:
        if i in dictionary.keys():
          wieghtArray += [dictionary[i].wieght]
          strengthArray += [dictionary[i].strength]
        else:
          wieghtArray += [5]
      w = 5
      s = 5
      if len(wieghtArray) != 0:
        w = AvWeight(wieghtArray)
        s = AvWeight(strengthArray)
      current = concept(l,w,s)
      if last != "":
        mem = memory(last,current)
        tmpMem += [mem]
      last = current
    else:
      last = ""
    l = f.readline()
  f.close()
  return tmpMem

if False:
  #if __name__ == "__main__":
  while True:
    inp1 = removePunctuation(raw_input("S:").lower())
    if(inp1 in ["quit","save","save()","quit()"]):
      Save()
      break
    elif(inp1.split()[0] == ":"):
		  a = 0
    elif(inp1 == "appened"):
      Save()
      memories += Append()
      Save()
      Load()
    elif(inp1 != "debug"):
      inp2 = input("F:")
      inp3 = input("C:")
      s = concept(inp1,inp2,inp3)
      memories += [memory(last,s)]
      last = s
      words = response(inp1, inp2)
      se = ""
      for i in words:
        se += i.word + " "
      print se,
      wi = 0
      st = 0
      for i in words:
        wi += i.wieght
        st += i.strength
      wi /= len(words)
      st /= len(words)
      print wi, st
      s = concept(se,wi,st)
      memories += [memory(last,s)]
      last = s
    else:
      for i in memories:
        print i.inp.scentnce, ",",
        print i.out.scentnce
      for i in dictionary.keys():
        print dictionary[i].word, dictionary[i].wieght, dictionary[i].strength
