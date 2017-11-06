# Remove Column from Data File

  
def remove_column(read_file,write_file,column_index):
    
    f = open(read_file, 'r')
    g = open(write_file, "w")

    for line in f:
        if line.strip():
            left_index=column_index - 1
            right_index=column_index + 1
            string1=line.split("|")[:left_index]
            string2=line.split("|")[right_index:]
            str1="|".join(string1)
            str2="|".join(string2)
            str3=str1 + "|" +str2
            g.write(str3)
            
    print("Column is removed from File. Result is stored in u.item_clean file.")
    f.close()
    g.close()


read_file="C:\\Users\\KETKI\\Desktop\\India Resume\\LoudCloud Test\\dataset\\u.item"
write_file="C:\\Users\\KETKI\\Desktop\\India Resume\\LoudCloud Test\\dataset\\u.item_clean"
column_index=4      
remove_column(read_file,write_file,column_index)
