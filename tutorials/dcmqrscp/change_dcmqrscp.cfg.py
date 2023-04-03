import re,os,sys



if __name__ == '__main__':
	content = ''
	f1 = open(sys.argv[1])
	lines = f1.readlines()
	for i in range(len(lines)):
		if '<put $WORK value here>' not in lines[i]:
			content += lines[i]
		else:
			l = re.sub('<put \$WORK value here>/dcmtk/build/bin', sys.argv[2],  lines[i])
			content += l
	f1.close()
	f2 = open(sys.argv[2] + '/dcmqrscp.cfg', 'w+')
	f2.write(content)
	f2.close()

