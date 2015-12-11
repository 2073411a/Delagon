def strip(line):
  ret = ""
  for i in line:
     if i not in "_,.?'~`()\n\t\'\"":
      ret += i
     else:
      ret += ' '
  return ret

def numeric(line):
  for i in line.lower():
    if i not in "xiv1234567890\n" or len(line) == 1:
      return False
  return True

def main():
  f = file("Books.txt")
  o = file("OutStep1.txt",'w') #Just needs to write the words in order
  line = f.readline()
  addline = ""
  reading = False
  while line != "":
    if line == "_BOOKEND_\n":
      addline += "\n_BOOKEND_\n"
      o.write(addline)
      addline = ""
      reading = False
    elif numeric(line):
      addline += "\n" + line + "\n"
      o.write(addline)
      addline = ""
      reading = False
    elif '\"' not in line:
      if reading:
        addline += strip(line)
    else:
      s = line.split('\"')
      if reading:
        addline += strip(s[0])
        for i in range(1,len(s)/2):
          addline += strip(s[i*2])
          if i < len(s)/2:
            addline += '\n'
            o.write(addline)
            addline = ""
        reading = len(s)%2 == 1
      else:
        for i in range((len(s) - 1)/2):
          addline += strip(s[i*2 + 1])
          if i < (len(s) - 1)/2:
            addline += '\n'
            o.write(addline)
            addline = ""
        reading = len(s)%2 == 0
    line = f.readline()
  o.write(addline)
  o.close()
  f.close()

if __name__ == "__main__":
  main()
