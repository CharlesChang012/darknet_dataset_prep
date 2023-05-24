import os, glob
import shutil
import pathlib

#train_jpg_path = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\train_jpg"
#train_txt_path = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\train_txt"
#train_destination_folder = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\obj\train"

#valid_jpg_path = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\valid_jpg"
#valid_txt_path = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\valid_txt"
#valid_destination_folder = r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\obj\valid"


x64_data_path = pathlib.Path().resolve() # r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data
obj_folder = os.path.join(x64_data_path, "obj") # r"C:\Users\spacelab\Desktop\Charles\Autonomous Driving\AD_final\darknet-master\darknet-master\build\darknet\x64\data\obj

def write_empty_txt(dataset_type):
    jpg_list = []
    txt_list = []
    
    global x64_data_path
    jpg_path = os.path.join(x64_data_path, dataset_type + "_jpg")
    
    os.chdir(jpg_path)
    for jpg_filename in os.listdir(os.getcwd()):
        jpg_list.append(jpg_filename)

    txt_path = os.path.join(x64_data_path, dataset_type + "_txt")
    os.chdir(txt_path)
    for txt_filename in os.listdir(os.getcwd()):
        new_name = str(txt_filename).replace('.txt', '')
        txt_list.append(new_name)

    for i in range(len(jpg_list)):
        if any(txt_name in jpg_list[i] for txt_name in txt_list):
            pass
        else:
            txt_file_name = str(jpg_list[i]).replace('jpg', 'txt')
            f = open(txt_file_name, "x")
            f.close()


def copy_to_dest(dataset_type):    
    global x64_data_path
    jpg_path = os.path.join(x64_data_path, dataset_type + "_jpg")
    txt_path = os.path.join(x64_data_path, dataset_type + "_txt")
    copy(jpg_path, dataset_type)
    copy(txt_path, dataset_type)

def copy(path, dataset_type):
    global obj_folder
    for file_name in os.listdir(path):
        # construct full file path
        source = os.path.join(path, file_name)
        destination = os.path.join(obj_folder, dataset_type, file_name)
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)


# dataset_typr: "train", "valid", "test"
def write_jpg_name_to_txt(dataset_type):
    global obj_folder
    des = "data/obj/" + dataset_type + "/"
    jpg_list = []
    global x64_data_folder
    jpg_path = os.path.join(x64_data_path, dataset_type + "_jpg")
    os.chdir(jpg_path)
    for jpg_filename in os.listdir(os.getcwd()):
        if "jpg" in str(jpg_filename):
            jpg_list.append(des + str(jpg_filename))

    output_path = os.path.join(x64_data_path, dataset_type + ".txt")
    f = open(output_path, 'w')
    for i in range(len(jpg_list)):
        f.write(jpg_list[i] + '\n')
    f.close()

write_empty_txt("train")
write_empty_txt("valid")

copy_to_dest("train")
copy_to_dest("valid")


write_jpg_name_to_txt("train")
write_jpg_name_to_txt("valid")