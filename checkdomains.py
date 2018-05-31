import requests
from socket import gethostbyname, gaierror


lines=0
fh = open('names.txt')
out = open('output.txt','w') 
for line in fh:
    lines += 1
    line = line.rstrip()
    try:
        addr1 = gethostbyname(line)
        print "%s,%s" %(addr1,line)
        out.write("%s,%s\n" %(addr1,line))
        if (lines > 10):
                out.flush()
                lines = 0
    except gaierror:
        print "------------,%s" %line
        out.write("------------,%s\n" %line)
        if (lines > 10):
                out.flush()
                lines = 0
fh.close()
out.close()
