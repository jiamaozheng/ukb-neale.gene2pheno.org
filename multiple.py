from subprocess import call
import os, subprocess, glob 


# # source_folder = "MetaXcan_results_2017_10_11"
# destiny_folder = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/MetaXcan_results_2017_10_11_renamed/"

# tissue_list_file = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/tissue_list.txt"
# dictionary = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/codes_phenotypes_UKB_NealeLab.txt"

# inputFileList = glob.glob(destiny_folder + "*.csv")
# print(inputFileList[1])
# print(len(inputFileList))

# source_folder = "MetaXcan_results_2017_10_11"
# destiny_folder = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/MetaXcan_results_2017_10_11_gzipped"

# tissue_list_file = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/tissue_list.txt"
# dictionary = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/codes_phenotypes_UKB_NealeLab.txt"

# with open(tissue_list_file) as TL:
#   tissue_list = []
#   for tissue in TL:
#     tissue_list.append(tissue.strip())
  

# with open(dictionary) as dict:
#   dict.readline()
#   for i, line in enumerate(dict):
#     line = line.split()
#     for tissue in tissue_list:
#       destiny_path = destiny_folder + "/" + line[2] + "_" + tissue + ".gz"

      # msg = "\nUploading: " + destiny_path
      # self.logger.info(msg)
      # print(msg) 

multiple = glob.glob("/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/MetaXcan_results_by_phenotype_2017_10_14/*.tar.gz")
for destiny_path in multiple: 
  call(['aws', 's3',  'cp', destiny_path, "s3://gene2pheno/combined-accross-tissues/"])