import requests
import getopt
import json
import sys

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print 'python parse.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
    for opt, arg in opts:
       if opt in ("-i", "--ifile"):
          inputfile = arg
       if opt in ("-o", "--ofile"):
          outputfile = arg

    data = ''
    with open(inputfile,'rb') as inf:
        response = requests.post('https://jobs.lever.co/parseResume', files=dict(resume=inf))
        data = response.json()
        print(data)

    with open(outputfile,'w') as outf:
        json.dump(data, outf, indent=4)

if __name__ == "__main__":
    main(sys.argv[1:])

