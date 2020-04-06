# Apriori
A python script that implements Agrawal's and Srikan's A Priori Algorithm for frequent item set mining and association rule learning over transactional databases.

##Apriori 
A python script that implements Agrawal's and Srikant's A Priori Algorithm for frequent item set mining and association rule learning over transactional databases. Input is given in CSV type files with the following format:

item_11, item_12, ..., item_1n
item_21, item_22, ..., item_2n
...
Output is also given in CSV type files with the following format: itemset_1:support;itemset_2:support;...itemset_n:support The script should handle the following arguments:

-n:optional. Input items should be handled as numeric instead of strings.
-p:optional. Support should be considered as a percentage of given baskets.
-o:optional. Output should be saved in a separate file. Otherwise, it should be printed.
