__author__ = 'pgrant'

import sh

proj_list = sh.ssh("-p", "29418", "pgrant@10.208.19.146", "gerrit", "ls-projects")

print proj_list

for projDir in proj_list:
    print "cd ", projDir
    print "

