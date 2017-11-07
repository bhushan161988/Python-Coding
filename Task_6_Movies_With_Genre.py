import sys
import csv
import operator  

answer = {}
 
def genre_file_swap_fields(read_file,write_file):
    
    fileHandle = open(read_file, 'r')
    fileHandle1 = open(write_file, 'w')

    for line in fileHandle:
        fields = line.rstrip("\n").split('|')
        if (fields[0].strip()):
            if (fields[1].strip()):
                str1=fields[1] + "|" + fields[0] + "\n"
                fileHandle1.write(str1)


    fileHandle.close()
    fileHandle1.close()


def create_genre_dictionary(read_file):

    fileHandle = open(read_file, 'r')

    #answer = {}
    for line in fileHandle:
        line = line.rstrip("\n").split("|")
        if not line:  # empty line?
            continue
        answer[line[0]] = line[1:]

    fileHandle.close()


def get_movie_with_genre(item_file,item_temp_file):
    
    fileHandle = open(item_file, 'r')
    fileHandle1 = open(item_temp_file, 'w')
    for line in fileHandle:
        fields = line.split('|')
        for i in range(5,24):
            if (int(fields[i]) is 1):
          
                b = i -5
                val=answer.get(str(b))
                val=str(val)
                val=val.replace("[", "")
                val=val.replace("]", "")
                val=val.replace("'", "")
                
                str1= str(val) + "|" + fields[1] + "\n"
                fileHandle1.write(str1)
        
 

    fileHandle.close()
    fileHandle1.close()
    
def sort_file(item_temp_file): 
    read_ptr = csv.reader(open(item_temp_file),delimiter='|')
    sort_list = sorted(read_ptr,key=operator.itemgetter(0),reverse=False)   
    
    write_task2_ptr = open(item_temp_file, "w")
    
    for row in sort_list:
        str2=row[0]  + "|" + row[1] +  "\n"
        write_task2_ptr.write(str2)
    
    
    print("Output is stored in Task_6_Output File")
    write_task2_ptr.close()
     


#Main Code Starts here
genre_file_path=input('Enter u.genre file path location (with File Name): ')
Temp_OP_File= genre_file_path + "_intermediate_op"

#Call function to first swap the fields required to create dictionary
genre_file_swap_fields(genre_file_path,Temp_OP_File)


#Call function to create dictionary from genre file
create_genre_dictionary(Temp_OP_File)

#Get the item file name and location from user
item_file=input('Enter u.item file path location (with File Name): ')
ITEM_Temp_OP_File= item_file + "_Task_6_Output"


#Get the movies and corresponding genre into  a separate file
get_movie_with_genre(item_file,ITEM_Temp_OP_File)


# Sort the same file
sort_file(ITEM_Temp_OP_File)



