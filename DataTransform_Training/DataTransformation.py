from datetime import datetime
from os import listdir
import pandas
from application_logging.logger import App_Logger


class dataTransform:

    """
      This class shall be used for transforming the Good Raw Training Data before loading it in Database!!.
    """

    def __init__(self):
      self.goodDataPath = "Training_Raw_files_validated/Good_Raw"
      self.logger = App_Logger()


    def replaceMissingWithNull(self):
      """
        Method Name: replaceMissingWithNull
        Description: This method replaces the missing values in columns with "NULL" to
                    store in the table. We are using substring in the first column to
                    keep only "Integer" data for ease up the loading.
                    This column is anyways going to be removed during training.
      """
      log_file = open("Training_Logs/dataTransformLog.txt", 'a+')
      try:
        onlyfiles = [filename for filename in listdir(self.goodDataPath)]
        for filename in onlyfiles:
          df = pandas.read_csv(self.goodDataPath+"/" + filename)
          df.fillna('NULL',inplace=True)
          df['Wafer'] = df['Wafer'].str[6:]
          df.to_csv(self.goodDataPath+ "/" + filename, index=None, header=True)
          self.logger.log(log_file," %s: File Transformed successfully!!" % filename)
           
      except Exception as e:
        self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
        log_file.close()
        
      log_file.close()
