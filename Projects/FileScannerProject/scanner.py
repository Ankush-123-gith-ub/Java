import os
import hashlib
import datetime
import psutil

######################################  check file type  ##########################################################
def file_type_identifier(path):
    magic_numbers = {
        "jpg":  b"\xff\xd8\xff",
        "png":  b"\x89PNG",
        "pdf":  b"%PDF"
    }
    with open(path,"rb") as f:
        data = f.read(16)
        # print(data.hex())

        for filetype,magic_number in magic_numbers.items():
            if data.startswith(magic_number):
                return filetype
    return "unknown"

################################ extension check #########################################
def check_extension_mismatch(path):
    ext = os.path.splitext(path)[1].lower().replace('.', '')  # get extension without dot
    detected_type = file_type_identifier(path)
    if ext != detected_type:
        return True, ext, detected_type
    return False, ext, detected_type

#######################################  check malicious file  #######################################################


def malware_hashes_check(path):
    known_hash = {
    "44d88612fea8a8f36de82e1278abb02f",
    "db349b97c37d22f5ea1d1841e3c89eb4",
    "5d41402abc4b2a76b9719d911017c592",
    "7c4a8d09ca3762af61e59520943dc264"
    }

    file_hash = md5_hash_file(path)
    if file_hash in known_hash:
            return file_hash
    return "Safe"

def md5_hash_file(path,chunk_size=4096):
    md5 = hashlib.md5()
    with open(path,"rb") as f:
            while chunk := f.read(chunk_size):
                 md5.update(chunk)
    return md5.hexdigest()

###############################################  monitoring suspicious proces ######################################



##################################################### main ######################################################### 
magic_numbers = {
        "jpg":  b"\xff\xd8\xff",
        "png":  b"\x89PNG",
        "pdf":  b"%PDF"
    }
total_files = 0
safe_count = 0
infected_count = 0
file_type_count = {}  # {"jpg": 2, "pdf": 3}
infected_files = []  # [("file.pdf", hash)]

folder = r"C:\Users\Asus\OneDrive\Documents\cyber-sb\oops\Projects\FileScannerProject\test_files"
files = os.listdir(folder)
for file in files:
    total_files += 1
    file_path = os.path.join(folder,file)
    if os.path.isfile(file_path):
        mismatch, ext, detected = check_extension_mismatch(file_path)


        ##### count safe and infected files and stroing with name ####
        if malware_hashes_check(file_path) == "Safe":
              safe_count += 1
        else:
              
            #   infected_files[infected_count] = (file,malware_hashes_check(file_path)) wrong 
            infected_count+=1
            infected_files.append((file,malware_hashes_check(file_path)))
        
        ###### file type count#######
        for type_f in magic_numbers.keys():
             if type_f == file_type_identifier(file_path):
                if type_f  not in file_type_count.keys():
                       file_type_count[type_f] = 1
                else:
                        file_type_count[type_f] += 1

############################################# witing file ##################################################################
time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
scanner_file_path = fr"C:\Users\Asus\OneDrive\Documents\cyber-sb\oops\Projects\FileScannerProject\Reports\Scanner_report_{time_stamp}.txt"
with open(scanner_file_path,"w") as report:
    report.write(f"Total files scanned: {total_files}\n")
    report.write(f"Safe files: {safe_count}\n")
    report.write(f"Infected files: {infected_count}\n")
    report.write("\n")
    report.write("File types detected:\n")
    for file,count in file_type_count.items():
        report.write(f"    {file}: {count}\n")
    report.write("\n")
    report.write("Infected files:\n")
    if infected_count:
        for file,hash_v in infected_files:
            report.write(f"    {file} --> Infected({hash_v})\n")

    if mismatch:
        report.write(f"[WARNING] {file}: extension .{ext} does not match detected type {detected}\n")
    
# Console summary
print("===== Scan Summary =====")
print(f"Total files scanned: {total_files}")
print(f"Safe files: {safe_count}")
print(f"Infected files: {infected_count}")
print(f"Report saved at: {scanner_file_path}")
###################################################################################################################
