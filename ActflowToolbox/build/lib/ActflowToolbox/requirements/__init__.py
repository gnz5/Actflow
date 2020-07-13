import os
import requests
from zipfile import ZipFile
import pkg_resources

actflowdir = pkg_resources.resource_filename('ActflowToolbox', '/')
requirementsFile = actflowdir + '/requirements/requirements.cfg'
start_path = os.getcwd()

def download_requirements():
    print("Downloading requirements. This may take some time depending on your internet speed")
    
    # download dependencies folder
    print("Downloading dependencies folder...");
    dependencies_url = "https://colelab.s3.us-east-2.amazonaws.com/dependencies.zip"
    r = requests.get(dependencies_url, allow_redirects=True)
    zip_path = actflowdir + "dependencies.zip"
    open(zip_path, "wb").write(r.content)
    with ZipFile(zip_path, 'r') as zipObj:
        os.chdir(actflowdir)
        zipObj.extractall()
    os.chdir(start_path)
    os.remove(zip_path)
    
    # download docs folder
    print("Downloading docs folder...");
    docs_url = "https://colelab.s3.us-east-2.amazonaws.com/docs.zip"
    r = requests.get(docs_url, allow_redirects=True)
    zip_path = actflowdir + "docs.zip"
    open(zip_path, "wb").write(r.content)
    with ZipFile(zip_path, 'r') as zipObj:
        os.chdir(actflowdir)
        zipObj.extractall()
    os.chdir(start_path)
    os.remove(zip_path)

    # download examples folder
    print("Downloading examples folder...");
    examples_url = "https://colelab.s3.us-east-2.amazonaws.com/examples.zip"
    r = requests.get(examples_url, allow_redirects=True)
    zip_path = actflowdir + "examples.zip"
    open(zip_path, "wb").write(r.content)
    with ZipFile(zip_path, 'r') as zipObj:
        os.chdir(actflowdir)
        zipObj.extractall()
    os.chdir(start_path)
    os.remove(zip_path)

    # download network_definitions folder
    print("Downloading network_definitions folder...");
    network_definitions_url = "https://colelab.s3.us-east-2.amazonaws.com/network_definitions.zip"
    r = requests.get(network_definitions_url, allow_redirects=True)
    zip_path = actflowdir + "network_definitions.zip"
    open(zip_path, "wb").write(r.content)
    with ZipFile(zip_path, 'r') as zipObj:
        os.chdir(actflowdir)
        zipObj.extractall()
    os.chdir(start_path)
    os.remove(zip_path)
    
    with open(requirementsFile, "w") as f:
        f.write("files_downloaded=True")
        
    print("Success")

def verify_requirements():
    with open(requirementsFile, "r") as f:
        content = f.readline()
        if content.split('=')[1] == "False":
            download_requirements()
        else:
            print("Requirements satisfied")
            
# given a directory, returns a tuple containing the number of files 
# and the sum of the sizes of all files in the directory free
def get_size(start_path = '.'):
    total_size = 0
    num_files = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                num_files += 1
                
    return (num_files, total_size)            
            
# checks the number of files and total size of the dependencies,
# docs, examples, and network_definitions folders        
def verify_folder_sizes():
    actflow_dir = pkg_resources.resource_filename('ActflowToolbox', '/')
    dirs_to_check = ['dependencies', 'docs', 'examples', 'network_definitions']

    print(os.listdir(actflow_dir))

    if not os.getcwd().endswith('ActflowToolbox'):
        os.chdir(actflow_dir)

    for directory in dirs_to_check:
        num_files, folder_size = get_size(directory)
        print(num_files, 'files,', folder_size, 'bytes')










    