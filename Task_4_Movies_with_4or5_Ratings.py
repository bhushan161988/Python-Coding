
import csv
import operator  
from collections import defaultdict
from datetime import datetime

answer = {}
movie_ratings_dict = defaultdict(int)
movie_ratings_dict_sum = defaultdict(int)
movie_year = defaultdict(int)
 
def data_file_sorted(read_file,write_file):
    
    read_ptr = csv.reader(open(read_file),delimiter='\t')
    sort_list = sorted(read_ptr,key=operator.itemgetter(1,2),reverse=False)   
    write_task2_ptr = open(write_file, "w")
     
    for row in sort_list:
        if (row[2] is '4' or row[2] is '5' ):
            str2=row[1]  + "|" + row[2] +  "\n"
            write_task2_ptr.write(str2)
    write_task2_ptr.close()



def create_temp_file_intermediate_op(read_file,write_file):
    
    f = open(read_file, 'r')
    g = open(write_file, "w")
    
    for line in f:
        if line.strip():
        
            fields = line.split('|')
        
            Movie_id= fields[0]
            Movie_Name= fields[1]

        
            if fields[2].strip():
                dt = datetime.strptime(fields[2], '%d-%b-%Y')
              
                Year_Number= dt.year
                str1= Movie_id + "|" + str(Year_Number) + "|" + Movie_Name  + "\n"
                g.write(str1)
            
    print("Intermediate Result is stored in temp_item_file.")
    f.close()
    g.close()
    
    
    

def get_movie_year(read_file):

    fileHandle = open(read_file, 'r')

    #answer = {}
    for line in fileHandle:
        line = line.rstrip("\n").split("|")
        if not line:  # empty line?
            continue
        movie_year[line[0]] = line[1:]
    
    
    
    fileHandle.close()
    
    


def get_file_sum(read_file, write_file):

    reader = csv.reader(open(read_file),delimiter='|')
    write_task1_ptr = open(write_file, "w")
    for row in reader:
        movie_ratings_dict_sum[row[0]] += int(row[1])

    for row in movie_ratings_dict_sum:
      
        val1=str(row)
        val1=val1.replace("('","")
        val1=val1.replace("')","")
        val1=val1.replace("','","|")
        val2=str(movie_ratings_dict_sum[row])
        val2=val2.replace("[","")
        val2=val2.replace("]","")
        val4=val1 + "|" + val2 + "\n"    
        
        write_task1_ptr.write(val4)
    
    write_task1_ptr.close()
    
    
    
    
    

def get_file_count(read_file, write_file):

    reader = csv.reader(open(read_file),delimiter='|')
   
    for row in reader:
        
        str1="('"+row[0]+"','"+row[1]+"')"
        
        if str1 in movie_ratings_dict:
            val=movie_ratings_dict.get(str1)
            val1=str(val)
            val1=val1.replace("[","")
            val1=val1.replace("]","")
            val1 = int(val1) +1
            movie_ratings_dict[str1]= [int(val1)]
        else:
            movie_ratings_dict[str1]= [int(1)]

    
    
    write_task2_ptr = open(write_file, "w")
    
    for row in movie_ratings_dict:
        
        val2=str(row)
        val2=val2.replace("('","")
        val2=val2.replace("')","")
        val2=val2.replace("','","|")
        val3=str(movie_ratings_dict[row])
        val3=val3.replace("[","")
        val3=val3.replace("]","")
        val4=val2 + "|" + val3 + "\n"    

        write_task2_ptr.write(val4)
    
    write_task2_ptr.close()


def final_output(read_file, write_file):
    fileHandle = open(read_file, 'r')
    write_task2_ptr = open(write_file, "w")
    #answer = {}
    for line in fileHandle:
        line = line.rstrip("\n").split("|")
        if not line:  # empty line?
            continue
        
        rating_sum= int(movie_ratings_dict_sum[line[0]])
        if (int(rating_sum) >= 20):
            val2=str(movie_year[line[0]])
            val2=val2.replace("['","")
            val2=val2.replace("']","")
            val2=val2.replace("', '","|")
            val4=val2 + "|" + line[1] + "|" + line[2] + "\n"
            write_task2_ptr.write(val4)
        
    print("Final Result is stored in Task_4_Final_output.") 
    
    write_task2_ptr.close()   

    fileHandle.close()
    
    
            
data_file_path=input('Enter u.DATA file location (with File Name): ')
Temp_OP_File= data_file_path + "_intermediate_op"

Task_4_OP_SUM_File=data_file_path + "_Task_4_Sum_output"
Task_4_OP_Count_File=data_file_path + "_Task_4_Count_output"

item_file_path=input('Enter u.item file location (with File Name): ')

Item_Temp_OP_File= item_file_path + "_intermediate_op_task4"

data_file_sorted(data_file_path,Temp_OP_File)


create_temp_file_intermediate_op(item_file_path,Item_Temp_OP_File)


get_movie_year(Item_Temp_OP_File)


get_file_sum(Temp_OP_File, Task_4_OP_SUM_File)

get_file_count(Temp_OP_File, Task_4_OP_Count_File)
    
Task_4_Final_Output=input('Enter Final Output File location (with File Name): ')
   
final_output(Task_4_OP_Count_File, Task_4_Final_Output)
