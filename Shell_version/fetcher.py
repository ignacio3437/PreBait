import urllib2


prefix = "http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=fasta&id="
id_per_request = 20


def getSeq (id_list):
    url = prefix + id_list[:len(id_list)-1]

    temp_content = ""
    try:
        temp_content += urllib2.urlopen(url).read()

### if there is a bad apple, try one by one
    except:
        for id in id_list[:len(id_list)-1].split(","):
            url = prefix + id
    #print url
            try:
                temp_content += urllib2.urlopen(url).read()
            except:
            #print id
                pass
    return temp_content


content = ""
counter = 0
id_list = ""

#make list of genbank accesions from textfile
with open('Lgig500_Accession.txt','rU') as accession_file:
    accs=[f.strip('\n') for f in accession_file]

for acc in accs:

    id_list += acc + ","
    counter += 1

    if counter == id_per_request:
        counter = 0
        content += getSeq(id_list)
        id_list = ""

if id_list != "":
    content += getSeq(id_list)
    id_list = ""


print content
if len(content) < 2:
 	print "Nothing downloaded. Check internet connection!"