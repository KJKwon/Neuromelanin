import os
import sys
import time

number = input("Number of files to union candidate gene: ")

def filtering(file_name):
	
	for file_find in os.listdir('.'):
		if file_find.startswith(file_name):
			candidate_file = open(file_name,'r')
	for line in candidate_file:
		candidate_gene_raw = line.strip().split('\t')
		candidate_gene_list = set(candidate_gene_raw)
	
	candidate_file.close()
	return candidate_gene_list 
	
temp = raw_input("Type file name(1): ")
output = filtering(temp)
for file_num in range(2,number+1):
	temp = raw_input("Type file name(%d): "%(file_num))
	output = output & filtering(temp)

date = time.strftime("%Y%m%d-%H%M%S")
output_file = open('union_file_%s'%(date),'w')
output_file.write('\t'.join(sorted(list(output))))
output_file.close()
		
