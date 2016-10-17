import json

import csv

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

with open("/Users/divyasrikanth/Desktop/output.json","r") as t_file:
      reviews = t_file.read()

      
review_parsed = json.loads(reviews)

review_data = review_parsed['review_details']

# open a file for writing

rvw_data = open('/Users/divyasrikanth/Desktop/ReviewData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(rvw_data)

count = 0

for review in review_data:

      if count == 0:

             header = review.keys()

             csvwriter.writerow(header)

             count += 1

             
      csvwriter.writerow(review.values())
       

rvw_data.close()



