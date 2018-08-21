import sys
import re

from pyspark import SparkContext

sc = SparkContext('local[2]', 'pyspark tutorial') 

def noPunctuations(text):
    """Removes punctuation and convert to lower case
    Args:
        text (str): A string.
    Returns:
        str: The cleaned up string.
    """
    return re.sub('[^a-z| |0-9]', '', text.strip().lower())

lines_rdd = sc.textFile("README.md", 1)
counts = lines_rdd.map(noPunctuations).flatMap(lambda x: x.split()).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y).takeOrdered(20,lambda x : -x[1])
		 
for (word, count) in counts:
   print(word,count)
