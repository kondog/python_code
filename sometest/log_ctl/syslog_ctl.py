import re

src_file = None
dist_file = None

# search all line from src_file.
src_file = open( "syslog", "r")
dist_file = open( "syslog-cut", "w")

for line in src_file:
    # if ( matching some condition from src_file, cutting str. )
    string = re.search( r'Dec 25 08:28.*', line)
    print(string)
    if ( None != string ):
        # cutting str to dist_file.
        dist_file.write(line)

src_file.close()
dist_file.close()
        
