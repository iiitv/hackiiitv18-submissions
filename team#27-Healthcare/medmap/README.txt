Questions that can be answered

Statistical Questions:
1. Stats of a disease in a given area.
2. Correlation among occurence of disease.
3. Prediction of outbreak based on past history.
4. Severity score of disease in a given area by counting number of tweets per day/hour.
5. Predicting symptoms of certain diseases (For example, ebola occurs mostly in areas where flu is there).


Social questions:
1. Where to establish medical camps?
2. Where to give medicines?
3. Taking early measures.

Major Challenges

1. Relevant tweets.
2. Finding location.


Minor issues

1. Encoding/Decoding.
2. Language Filtering.

To find relevant tweets, we clustered the data using kmeans algorithm. Intuitively, if a cluster contains a lot of data points then that cluster can be considered as a relevant cluster. A hard threshold is decided.
