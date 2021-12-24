import csv
import os
class MasterData:
    def validation_MasterData(self,p_lms_MasterData):
        data=None
        try:
            
            passflag=int(p_lms_MasterData[0])
            passflag=int(p_lms_MasterData[1])
            passflag=int(p_lms_MasterData[2])
            passflag=int(p_lms_MasterData[3])
            passflag=float(p_lms_MasterData[4])
            passflag=int(p_lms_MasterData[5])
        except:
            return{'Operation':'validation_MasterData','status':'Failed','message': 'Incorrect one or more field Data : '+', '.join([str(elem) for elem in p_lms_MasterData])} 
        else:
            return{'Operation':'validation_MasterData','status':'success','message':'Valid Data'}
        """
        try:
            passflag=float(lms_MasterData[4])
        except:
            return{'Operation':'validation_MasterData','status':'Failed','message':'Data Error'}
        else:
            return{'Operation':'validation_MasterData','status':'success','message':'Valid Data'}    
        """    

    def buildMasterData(self,p_lms_masterdata_file_path):
        if os.path.exists(p_lms_masterdata_file_path):
            with open(p_lms_masterdata_file_path) as lms_MD_file:
                lms_MD_filereader=csv.reader(lms_MD_file)

                header=[]
                header=next(lms_MD_file)
                print(header)

                lms_MasterData=[]
                for row in lms_MD_filereader:
                    if self.validation_MasterData(row)['status']=='success':
                        lms_MasterData.append({'CS_START':row[0],
                                     'CS_END':row[1],
                                     'LOAN_AMOUNT_START':row[2],
                                     'LOAN_AMOUNT_END':row[3],
                                     'INTEREST':row[4],
                                     'DURATION':row[5],
                                     })
                    else:
                        return self.validation_MasterData(row)
                    
                #print(rows)
            return {'Operation':'buildMasterData','Status':'Success','Data':lms_MasterData}
        else :
            return{'Operation':'buildMasterData','Status':'Failed','message':'File could not find'}

lms_masterdata_file_path="C:/Users/dkc91/OneDrive/Desktop/Python_classes/lms_MasterData.csv"
objMD=MasterData()               
print(objMD.buildMasterData(lms_masterdata_file_path))
