import os

def rename_files():
    # (1) get the file from the folder 
    file_list = os.listdir("/Users/bhetey/Downloads/prank")
    #print(file_list)
    saved_path = os.getcwd()

    print("Current working directory is " + saved_path)
    #os.chdir("/Users/bhetey/Downloads/prank")

    #(2) for each file, on the rename filename 
    #for file_name in file_list:
    #    os.rename(file_name, file_name.translate(None, "0123456789"))
    #os.chdir(saved_path)

rename_files()

