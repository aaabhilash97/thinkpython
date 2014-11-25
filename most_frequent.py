import string
def mostfrequent(x):

	dic={}
	for x1 in x:
	    if x1 not in string.punctuation+string.whitespace:
		dic[x1]=dic.get(x1,0)+1
	item=dic.items()
	item.sort(key=lambda x:x[1],reverse=True)
	for key,value in item:
		print key,value
mostfrequent("""The frequency of letters in text has often been studied for use in cryptanalysis, and frequency analysis in particular.

No exact letter frequency distribution underlies a given language, since all writers write slightly differently. Linotype machines assumed the letter order, from most to least common, to be etaoin shrdlu cmfwyp vbgkjq xz based on the experience and custom of manual compositors.

Likewise, Modern International Morse code encodes the most frequent letters with the shortest symbols; arranging the Morse alphabet into groups of letters that require equal amounts of time to transmit, and then sorting these groups in increasing order, yields e it san hurdm wgvlfbk opjxcz yq. Similar ideas are used in modern data-compression techniques such as Huffman coding.

Letter frequency was also used by other telegraph system, such as, for instance by Donald Murray, in the Murray Code.""")
