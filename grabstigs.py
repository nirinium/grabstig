###############
##### NTG #####
###############
# PROOF
#  OF 
#  CONCEPT 1/26/18
###############
## NOT FINAL ##
#### 0.0.3 ####

import requests
import wget
import os
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from bs4 import BeautifulSoup, SoupStrainer

cwd = os.getcwd()
newdir = cwd +"\\STIGs"
print "The current Working directory is " + cwd
os.mkdir( newdir, 0777);
print "Created new directory " + newdir
newfile = open('logfile.txt','w')
print newfile

url = 'https://iase.disa.mil/stigs/Pages/a-z.aspx'

file_types = ['.zip','.xls', '.xlsx', '.csv', '.ppt', '.pdf', '.docx', '.doc']

for file_type in file_types:

    response = requests.get(url)

    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if file_type in link['href']:
                wget.download(link['href'])

