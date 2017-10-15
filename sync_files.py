from subprocess import call
import os, subprocess

__author__ = "Jiamao Zheng <jiamaoz@yahoo.com>"
__version__ = "Revision: 0.0.2"
__date__ = "Date: 2017-10-11"

class BulkFilesS3UPLoading(object):
    def __init_(self):
        # logger 
        self.logger = ' '

        # log path 
        self.log_path = ''

        # input path
        self.input_path = ''

        # bucket path
        self.bucket_path = ''

    # Logging function 
    def getLog(self):
        log_file_name = ''
        if self.log_path != 'l':
            if self.log_path[-1] != '/':
                self.log_path = self.log_path + '/'
            log_file_name = self.log_path + str(myuuid.uuid4()) + '.log'
        else: 
            currentPath = os.path.abspath(os.path.abspath(sys.argv[0]))[:-35]
            currentPath = currentPath[:-(len(currentPath.split('/')[-2]) + 1)]
            log_file_name = currentPath + 'log/' + datetime.now().strftime('%Y-%m-%d')

            if not os.path.exists(log_file_name):
                os.makedirs(log_file_name)
            log_file_name = log_file_name + '/' + str(myuuid.uuid4()) + '.log'

        self.logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=log_file_name, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        self.logger.addHandler(fhandler)
        self.logger.setLevel(logging.INFO)

    # Funtion to get a pretty string for a given number of seconds.
    def timeString(self, seconds):
      tuple = time.gmtime(seconds);
      days = tuple[2] - 1;
      hours = tuple[3];
      mins = tuple[4];
      secs = tuple[5];
      if sum([days,hours,mins,secs]) == 0:
        return "<1s";
      else:
        string = str(days) + "d";
        string += ":" + str(hours) + "h";
        string += ":" + str(mins) + "m";
        string += ":" + str(secs) + "s";
      return string;

    # Get arguments 
    def get_args(self):
        # setup commond line arguments 
        parser = argparse.ArgumentParser()

        # bucket path 
        parser.add_argument('-b', '--bucket_path', required=True, default='b', type=str, help='a s3 bucket/subfolder (e.g. gene2pheno/by-tissue/) you choosen to bulk upload files')

        # inputput 
        parser.add_argument('-i', '--input_path', required=False, default='i', type=str, help='a input directory path where files exists')

        # log path 
        parser.add_argument('-l', '--log_path', required=False, default='l', type=str, help='a directory path you choosen to store log')

        # parse the arguments 
        args = parser.parse_args()
        self.input_path = args.input_path.strip()
        self.log_path = args.log_path.strip()
        self.bucket_path = args.bucket_path.strip()
        
        if self.bucket_path[-1] != '/':
            self.bucket_path = self.bucket_path + '/'
        if self.log_path != 'l' and not os.path.exists(self.log_path):
            os.makedirs(self.log_path)  

    def upload_bulk_files(self):  
		# source_folder = "MetaXcan_results_2017_10_11"
		destiny_folder = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/MetaXcan_results_2017_10_11_gzipped"

		tissue_list_file = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/tissue_list.txt"
		dictionary = "/Volumes/im-lab/nas40t2/rbonazzola/UK_Biobank/UKB_NealeLab/codes_phenotypes_UKB_NealeLab.txt"

		with open(tissue_list_file) as TL:
		  tissue_list = []
		  for tissue in TL:
		    tissue_list.append(tissue.strip())
		  

		with open(dictionary) as dict:
		  dict.readline()
		  for i, line in enumerate(dict):
		    line = line.split()
		    for tissue in tissue_list:
		      destiny_path = destiny_folder + "/" + line[2] + "_" + tissue + ".gz"

              # msg = "\nUploading: " + destiny_path
              # self.logger.info(msg)
              # print(msg) 

              call(['aws', 's3',  'cp', destiny_path, "s3://gene2pheno/by-tissue/"])

def main():
    # Instantial class
    start_time = time.time() 
    bulkFilesS3UPLoading = BulkFilesS3UPLoading()
    # bulkFilesS3UPLoading.get_args()
    # bulkFilesS3UPLoading.getLog()

    # run upload_bulk_files function
    bulkFilesS3UPLoading.upload_bulk_files()

    # msg = "\nElapsed Time: " + bulkFilesS3UPLoading.timeString(time.time() - start_time) # calculate how long the program is running
    # bulkFilesS3UPLoading.logger.info(msg)
    # print(msg) 

    # msg = "\nDate: " + datetime.now().strftime('%Y-%m-%d') + "\n"
    # bulkFilesS3UPLoading.logger.info(msg)
    # print(msg)   

# INITIALIZE
if __name__ == '__main__':
    sys.exit(main())