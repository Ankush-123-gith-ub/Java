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
                return f"Infected {hash_form}"
        return "Safe"
    
folder = r"C:\Users\Asus\OneDrive\Documents\cyber-sb\Projects\FileScannerProject\test_files"
files = os.listdir(folder)
for file in files:
    file_path = os.path.join(folder,file)
    if os.path.isfile(file_path):
        print(f"{file} : {file_type_identifier(file_path)} : {malware_hashes_check(file_path)} ")

# for print files
# files = os.listdir(r"C:\Users\Asus\OneDrive\Documents\cyber-sb\Projects\FileScannerProject\test_files")
# print(files)