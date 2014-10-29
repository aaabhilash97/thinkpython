def countletter(s,x,st,end):
        i=0
	s=s[st:end+1]
	print s
        for l in s:
                if x==l:
                        i=i+1
        return i
print countletter("qwergbvfeq","q",1,9)

