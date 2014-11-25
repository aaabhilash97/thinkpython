def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word), word))
	t.sort(key=lambda x:len(x[1]),reverse=True)
#	t.sort(reverse=True)
	print t
	res = []
	for length, word in t:
		res.append(word)
	return res
print sort_by_length(["axs","asa","asa","cfgyui","axs","qwerty"])

