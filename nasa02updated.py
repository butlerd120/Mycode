#!/usr/bin/env python3

 

import requests ## 3rd party URL lookup

 

## define the main function

def main():

    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL

    st_date = input("Please Enter Start Date")

    en_date = input("Please Enter End Date:")

    startdate = f'start_date={st_date}'  ## start date for data

    enddate = f'end_date={en_date}'

    #st_dateenddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate

    mykey = 'gg29P5Ukk6KWocKWT8Uzdzye0kuGoT2v3EiFbYQr' ## replace this with our API key

 

    neourl = neourl + startdate + enddate + mykey

 

    neojson = (requests.get(neourl)).json()

 

    print(neojson)

 

main()

