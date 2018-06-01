import requests
from socket import gethostbyname, gaierror

fh = open('names.txt')  # Open input file
out = open('output.txt','w',0) # Open output file, the 0 at the end disables buffering
for line in fh: # Iterate through input file, one line a time
    line = line.rstrip() # Remove line ending (CRLF)
    try:
        addr1 = gethostbyname(line) # If domain exist
        print "%s,%s" %(addr1,line) # Print info
        out.write("%s,%s\n" %(addr1,line))
        if (lines > 10):
    except gaierror: # Exception handling if domaing doesn't exist
        print "------------,%s" %line
        out.write("------------,%s\n" %line)
fh.close() # Close both files
out.close()
