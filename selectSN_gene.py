import os
import sys

if len(sys.argv) < 2:
	print '[folder name] needed'
	sys.exit(1)
folder_nm = sys.argv[1]
for folder_find in os.listdir('.'):
	if folder_find.startswith(folder_nm):
		os.chdir(folder_nm)
if 'MicroarrayExpression.csv' in os.listdir('.'):
	MA_data = open('MicroarrayExpression.csv','r')
	Site_data = open('SampleAnnot.csv','r')
	Probe_gene_data = open('Probes.csv','r')
	Probe_to_Exp = dict()
	Site_list = []
	Site_data.readline()
	for line in Site_data:
		Site_list.append(line.strip().split(',')[4].split('"')[1])
	Site_data.close()
	for line in MA_data:
		probe_data = line.strip().split(',')
		probe_name = probe_data[0]
		Probe_to_Exp[probe_name] = dict()
		for num in range(len(probe_data)-1):
			site_name = Site_list[num]
			if site_name not in Probe_to_Exp[probe_name]:
				Probe_to_Exp[probe_name][site_name] = [float(probe_data[num+1])]
			else:
				Probe_to_Exp[probe_name][site_name].append(float(probe_data[num+1]))
		for site_nm in Probe_to_Exp[probe_name]:
			total = sum(Probe_to_Exp[probe_name][site_nm])
			count = len(Probe_to_Exp[probe_name][site_nm])
			Probe_to_Exp[probe_name][site_nm] = float(total)/count
	MA_data.close()
	Probe_to_gene = dict()
	Probe_gene_data.readline()
	for line in Probe_gene_data:
		token = line.strip().split(',')
		probe = token[0]
		gene = token[3].split('"')[1]
		Probe_to_gene[probe] = gene
	gene_candidate = []
	for probe in Probe_to_Exp:
		Top10 = sorted(Probe_to_Exp[probe], key = Probe_to_Exp[probe].get, reverse = True)[:10]
		if 'SNC' in Top10:
			gene_candidate.append(Probe_to_gene[probe])

Probe_gene_data.close()
os.chdir("..")
Gene_candidate = open(folder_nm+'_Gene_candidate.txt','w')
Gene_candidate.write("\t".join(gene_candidate))
Gene_candidate.close()

		
