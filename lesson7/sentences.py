#poscitat i vyvest kolicestbo predlojeni v tekste
#vyvud
#"hello. My name is kaium. I am python programmer."
#vyvod:
#3

#1

#txt = input()
#q = 0
#for s in txt:
#   if s in [".", "!", "?"]:
#        q += 1

#print(q)


2 
txt = input()  #"hello. My name is kaium. I am python programmer."
sentences = txt.split(".")   #["hello",  "My name is kaium",  "I am python programmer", ""]
print(sentences)
print(len(sentences)-1)

#3
#txt = input()
#print(txt.count('.'))

