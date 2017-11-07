# Task 2, 3 and 5 - Sorting Data and Finding Movies with at least 2 vowels in their names

from datetime import datetime
import operator  
import csv   

  
def create_temp_file_intermediate_op(read_file,write_file):
    
    f = open(read_file, 'r')
    g = open(write_file, "w")
    
    for line in f:
        if line.strip():
        
            fields = line.split('|')
        
            Movie_Name= fields[1]

        
            if fields[2].strip():
                dt = datetime.strptime(fields[2], '%d-%b-%Y')
                Month_Name = dt.strftime("%B")
                Month_Number = dt.month
                Year_Number= dt.year
                str1= str(Year_Number) + "|" + str(Month_Number) + "|" + Month_Name + "|" + Movie_Name + "\n"
                g.write(str1)
            
    print("Intermediate Result is stored in temp_item_file.")
    f.close()
    g.close()

def sort_file_date(read_file,write_file_task2,write_file_task3,write_file_task4):
    
    read_ptr = csv.reader(open(read_file),delimiter='|')
    sort_list = sorted(read_ptr,key=operator.itemgetter(0,1),reverse=False)
    
    write_task2_ptr = open(write_file_task2, "w")
    write_task3_ptr = open(write_file_task3, "w")
    write_task4_ptr = open(write_file_task4, "w")
    
    
    vowels = ['a','i','o','u','A','I','O','U']
    
    for row in sort_list:
        str1= row[0] + "|" + row[2] + "|" + row[3] +  "\n"
        str2=row[0]  + "|" + row[3] +  "\n"
        write_task2_ptr.write(str1)
        write_task3_ptr.write(str2)
        i=0
        for c in row[3]:
            if c in vowels:
                i = i + 1
            
        if (i>=2):
            str3=row[0] + "|" + row[2] + "|" + row[3] + "|" + str(i) + "\n"
            write_task4_ptr.write(str3)
        
        
    print("Task 2 output is stored in Task_2_output file")  
    print("Task 3 output is stored in Task_3_output file")    
    print("Task 4 output is stored in Task_4_output file")  
    write_task2_ptr.close()
    write_task3_ptr.close()
    write_task4_ptr.close()


read_file=input('Enter u.ietm file path location (with File Name): ')
Temp_OP_File= read_file + "_intermediate_op"
  
create_temp_file_intermediate_op(read_file,Temp_OP_File)

Task2_OP_File=input('Enter output file Location for Task 2 (with File Name): ')
Task3_OP_File=input('Enter output file Location for Task 3 (with File Name): ')
Task4_OP_File=input('Enter output file Location for Task 4 (with File Name): ')

sort_file_date(Temp_OP_File,Task2_OP_File,Task3_OP_File,Task4_OP_File)
