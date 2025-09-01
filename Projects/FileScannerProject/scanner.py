import os
import hashlib

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



def malware_hashes_check(path):
    known_hash = {
    "44d88612fea8a8f36de82e1278abb02f",
    "db349b97c37d22f5ea1d1841e3c89eb4",
    "5d41402abc4b2a76b9719d911017c592",
    "7c4a8d09ca3762af61e59520943dc264"
    }

    with open(path,"rb") as f:
        ########################### use chunk for big files ################################# baad m krna h
        data = f.read()
        hash_form = hashlib.md5(data).hexdigest()
        if hash_form in known_hash:
                return hash_form
        return "Safe"
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

folder = r"FileScannerProject\test_files"
files = os.listdir(folder)
for file in files:
    total_files += 1
    file_path = os.path.join(folder,file)
    if os.path.isfile(file_path):

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


####### printing output ########
# Total files scanned: 10
# Safe files: 8
# Infected files: 2

# File types detected:
#   jpg: 4
#   pdf: 3
#   png: 3

# Infected files:
#   badfile.pdf → Infected <hash>
#   virus.png → Infected <hash>

print(f"Total files scanned: {total_files}")
print(f"Safe files: {safe_count}")
print(f"Infected files: {infected_count}")
print("\n")
print("File types detected:")
for file,count in file_type_count.items():
     print(f"    {file}: {count}")
print("\n")
print("Infected files:")
for file,hash_v in infected_files:
     print(f"    {file} --> Infected({hash_v})")

###################################################################################################################
