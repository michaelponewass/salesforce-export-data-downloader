# COPYRIGHT @ 2021 Simon, Sagstetter
from main import (
loadConfig,
login,
headers,
getFileLink,
downloadFile
)

from settings import (
Result
)

from sendmail import (
send_mail
)

print('#### Starting Salesforce Export Data Downloader ####')
CONFIG = loadConfig()
print('Configuration loaded...')
RESP = login(CONFIG)
print('Login successfull...')
RESULT = Result(RESP.text)
LINK = getFileLink(RESULT, CONFIG)
print('Init download...')
print('Please wait...')
links = LINK.split()
fileList=''
for link in links:  
    fileList+= downloadFile(link, RESULT, CONFIG)
    fileList+=", "
print('Download Completed!')
print('Your file is located: ' + fileList)
send_mail(CONFIG)
