import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\rbsim_000\Documents\Python Scripts\tempDir")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)
    os.chdir(r"C:\Users\rbsim_000\Documents\Python Scripts\tempDir")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        print ("Old Name - " +file_name)
        new_name = file_name.translate(None, "0123456789")
        print ("New NAme - " +new_name)
        os.rename(file_name, new_name)
    os.chdir(saved_path)
        
rename_files()
