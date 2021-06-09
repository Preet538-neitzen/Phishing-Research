# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:35:25 2021

@author: Achyuth
"""
from scipy.io import arff
import pandas as pd
import numpy as np
import tldextract
import requests


#To get page rank 
def get_pagerank(url):
  pageRank = open(r'C:\Users\Achyuth\Desktop\PageRank\Dataset.arff').readline()[:-2]
  extract_res = tldextract.extract(url)
  url_ref = extract_res.domain + "." + extract_res.suffix
  headers = {'API-OPR': pageRank}
  domain = url_ref
  req_url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
  request = requests.get(req_url, headers=headers)
  result = request.json()
  # print(result)
  print(result)
  """
  value = result['response'][0]['page_rank_decimal']
  if type(value) == str:
    value = 0

  if value < 2:
    return -1
  return 1
"""
get_pagerank("https://linked.in")
