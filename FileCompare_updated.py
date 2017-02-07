import filecmp
import csv
import sys
import os
import shutil
import re
regex = r"^[last_author|$][a-zA-Z]+"
##regex = r"^[$][a-zA-Z]+"
cmpt1=''
cmpt2=''
list_dummy=[]
list_dummy2=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
path1=str(raw_input("Please Enter First Folder Path:"))
sPath1=path1.lstrip(' ')
path2=str(raw_input("Please Enter Second Folder Path:"))
sPath2=path2.lstrip(' ')
Retrived_path=str(raw_input('Please Enter Output Destination Path:'))
print("In progress . . . please wait")
if not os.path.exists(Retrived_path):
        os.makedirs(Retrived_path)

def First_directory_contents(sPath1):
    """Getting entire ".py" files in given first file path"""
    for sChild1 in os.listdir(sPath1):
        sChildPath1 = os.path.join(sPath1, sChild1)
        if os.path.isdir(sChildPath1):
            First_directory_contents(sChildPath1)
        else:
            pass
        if sChildPath1.endswith(".py"):
            list1.append(sChildPath1)


def Second_directory_contents(sPath2):
    """Getting entire ".py" files in given second file path"""
    for sChild2 in os.listdir(sPath2):
        sChildPath2 = os.path.join(sPath2, sChild2)
        if os.path.isdir(sChildPath2):
            Second_directory_contents(sChildPath2)
        else:
            pass
        if sChildPath2.endswith(".py"):
            list2.append(sChildPath2)


def files_compare_in_folders():
    """Compare all the files in both folders"""
    value = range(len(list1))
    value1 = range(len(list2))
    for x in list2:
        path_val = os.path.split(x)[1]
        list_dummy.append(path_val)

    for x in list1:
        path_val = os.path.split(x)[1]
        list_dummy2.append(path_val)
        
    
    for x in value:
        test1 = os.path.split(list1[x])[1]
        if test1 in list_dummy:
            y=list_dummy.index(test1)
            cmpt1=list1[x]
            cmpt2=list2[y]
            if filecmp.cmp(cmpt1, cmpt2) is True:
                pass
                list6.append(cmpt1)
            else:
                list3.append(cmpt1)
                list7.append(cmpt2)
        else:
            list5.append(list1[x])

    for y in value1:
        test2 = os.path.split(list2[y])[1]
        if test2 in list_dummy2:
            pass
        else:
            list4.append(list2[y])

def get_entair_data():
    ##For Getting unmatched files from path1
    for x in list3:
        dirpath = x.split('\\')[-2:-1][0]
        if not os.path.exists(Retrived_path + '\\FirstFolder\\'+ dirpath):
                os.makedirs(Retrived_path + '\\FirstFolder\\'+dirpath)
        shutil.copy2(x, Retrived_path + '\\FirstFolder\\' + dirpath)
    ##For Getting unmatched files from path2
    for y in list7:
        dirpath = y.split('\\')[-2:-1][0]
        if not os.path.exists(Retrived_path + '\\SecondFolder\\'+dirpath):
                os.makedirs(Retrived_path + '\\SecondFolder\\'+dirpath)
        shutil.copy2(y, Retrived_path + '\\SecondFolder\\'+dirpath)

    ##For Getting ExtraFiles files from path1
    if len(list5) > 0 :
##        if not os.path.exists(Retrived_path + '\\Extrafiles\\FirstPtah'):
##            os.makedirs(Retrived_path + '\\Extrafiles\\FirstPtah')
        for x in list5:
            dirpath = x.split('\\')[-2:-1][0]
            if not os.path.exists(Retrived_path + '\\Extrafiles\\FirstPtah\\' +dirpath):
                    os.makedirs(Retrived_path + '\\Extrafiles\\FirstPtah\\'+dirpath)    
            shutil.copy2(x, Retrived_path + '\\Extrafiles\\FirstPtah\\'+dirpath)
    else:
        if not os.path.exists(Retrived_path + '\\Extrafiles\\FirstPath'):
            os.makedirs(Retrived_path + '\\Extrafiles\\FirstPath')
        Retrived_path1 = Retrived_path+'\\Extrafiles\\FirstPath'
        output_file = open(Retrived_path1 + '\\ReadMe.txt', 'w+')
        output_file.write("No Extra files are found in : %s"%(sPath1))
        output_file.close()
    ##For Getting ExtraFiles files from path2
    if len(list4) > 0:
##        if not os.path.exists(Retrived_path + '\\Extrafiles\\SecondPath'):
##            os.makedirs(Retrived_path + '\\Extrafiles\\SecondPath')
        for x in list4:
            dirpath = x.split('\\')[-2:-1][0]
            if not os.path.exists(Retrived_path + '\\Extrafiles\\SecondPath\\' +dirpath):
                    os.makedirs(Retrived_path + '\\Extrafiles\\SecondPath\\'+dirpath)
            shutil.copy2(x, Retrived_path + '\\Extrafiles\\SecondPath\\'+dirpath)
    else:
        if not os.path.exists(Retrived_path + '\\Extrafiles\\SecondPath'):
            os.makedirs(Retrived_path + '\\Extrafiles\\SecondPath')
        Retrived_path1 = Retrived_path+'\\Extrafiles\\SecondPath'
        output_file = open(Retrived_path1 + '\\ReadMe.txt', 'w+')
        output_file.write("No Extra files are found in : %s"%(sPath2))
        output_file.close()

    output_file = open(Retrived_path + '\\UnmatchedFiles.txt', 'w+')
    list3_len = range(len(list3))
    for x in list3_len:
            output_file.write(str(list3[x]) + '\n')
    output_file.close()
        
    print('''effected Files are coped in
            "%s"
            "%s" successfully'''%(Retrived_path + '\\FirstFolder', Retrived_path + '\\SecondFolder'))

#====================================================================================
def get_allRetrive_data():
        for fpath1,fpath2 in zip(list3, list7):
                base_name = os.path.basename(fpath1)
                dirpath = fpath1.split('\\')[-2:-1][0]
                list_val1=[]
                list_val2=[]
                list_dummy3=[]
                list_dummy4=[]
                file1_lines=[]
                file2_lines=[]
                file1=open(fpath1)
                file2=open(fpath2)
                file1_lines_temp=file1.readlines()
                file2_lines_temp=file2.readlines()
                for x in range(len(file1_lines_temp)):
                        string_value = file1_lines_temp[x].rstrip()
                        file1_lines.append(string_value)
                for x in range(len(file2_lines_temp)):
                        string_value = file2_lines_temp[x].rstrip()
                        file2_lines.append(string_value)        
                ##make both file index value will be same
                if len(file1_lines) > len(file2_lines):
                    x = len(file1_lines) - len(file2_lines)
                    for a  in range(x):
                        f1=file2_lines.append('')
                                    
                elif len(file1_lines) < len(file2_lines):
                    y = len(file2_lines) - len(file1_lines)
                    for b  in range(y):
                        file1_lines.append('')
                else:
                    pass
                ##Create Dummy values
                file1_data1 = file1_lines[:]
                file2_data1 = file2_lines[:]
                #get differents in first file
                def get_firstfile_data(file1_data1, file2_data1):
                    val1 = range(len(file1_data1))
                    for x in val1:
                            if file1_data1[x] == file2_data1[x]:
                                    file1_data1[x] = ''
                                    file2_data1[x] = ''
                            elif file1_data1[x] != file2_data1[x]:
                                    string= file1_data1[x]
                                    regex_value = re.findall(regex, string)
                                    if len(regex_value) > 0:
                                            pass
                                    elif file1_data1[x] not in file2_data1:
                                            list_dummy3.append( file1_data1[x])
                                            list_val1.append(x)
                     
                            else:
                                    pass
                    file1.close()
                    file2.close()
                get_firstfile_data(file1_data1, file2_data1)
                #get differents in Second file
                def get_secondfile_data(file1_lines, file2_lines):
                    val2 = range(len(file2_lines))
                    for x in val2:
                            if file2_lines[x] == file1_lines[x]:
                                    file1_lines[x] = ''
                                    file2_lines[x] = ''
                            elif file2_lines[x] != file1_lines[x]:
                                    string= file2_lines[x]
                                    regex_value = re.findall(regex, string)
                                    if len(regex_value) > 0:
                                            pass
                                    elif file2_lines[x] not in file1_lines:
                                            list_dummy4.append( file2_lines[x])
                                            list_val2.append(x)
                            else:
                                    pass
                get_secondfile_data(file1_lines, file2_lines)
                ##Create a File for Data difference
                if not os.path.exists(Retrived_path + '\\FileDifferences\\'+dirpath):
                        os.makedirs(Retrived_path + '\\FileDifferences\\'+dirpath)                        
                
                output_file=open(Retrived_path+ '\\FileDifferences\\'+ dirpath +'\\'+ base_name[:-3]+ '.txt', 'a+')
                output_file.write('############################################################################################################################################################\n')
                output_file.write('\tFirst file data -->' + fpath1 + '\n') 
                output_file.write('############################################################################################################################################################\n')
                for x in range(len(list_dummy3)):
                        output_file.write("Line-->%d"%(list_val1[x]+1) +'\t'+ list_dummy3[x]+'\n')
                output_file.write('\n\n')
                list_dummy3=[]
                output_file.write('############################################################################################################################################################\n')
                output_file.write('\tSecond file data -->' + fpath2 + '\n')
                output_file.write('############################################################################################################################################################\n')
                for y in range(len(list_dummy4)):
                        output_file.write("Line-->%d"%(list_val2[y]+1) +'\t'+ list_dummy4[y]+'\n')
                output_file.write('\n\n')
                list_dummy3=[]
                output_file.close()
        
        
        print("Good..Bye....:)")
#====================================================================================
if __name__ == "__main__":
    
    First_directory_contents(sPath1)
    Second_directory_contents(sPath2)
    files_compare_in_folders()
    get_entair_data()
    get_allRetrive_data()
    
    
