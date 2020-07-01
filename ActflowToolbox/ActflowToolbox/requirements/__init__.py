import os
import requests
from zipfile import ZipFile
import pkg_resources

actflowdir = pkg_resources.resource_filename('ActflowToolbox', '/')
requirementsdir = pkg_resources.resource_filename('ActflowToolbox.requirements', '/')
requirementsFile= requirementsdir + 'requirements.cfg'
#dependenciesdir = pkg_resources.resource_filename('ActflowToolbox.dependencies', '/')

def download_requirements():
    print("Downloading requirements. This may take some time depending on your internet speed")
    
    # # download dependencies folder
    # print("Downloading dependencies folder...");
    # dependencies_url = "https://colelab.s3.us-east-2.amazonaws.com/dependencies.zip"
    # r = requests.get(dependencies_url, allow_redirects=True)
    # zip_path = actflowdir + "dependencies.zip"
    # open(zip_path, "wb").write(r.content)
    # with ZipFile(zip_path, 'r') as zipObj:
        # zipObj.extractall(actflowdir)
    # os.remove(zip_path)
    
    # # download docs folder
    # print("Downloading docs folder...");
    # docs_url = "https://colelab.s3.us-east-2.amazonaws.com/docs.zip"
    # r = requests.get(docs_url, allow_redirects=True)
    # zip_path = actflowdir + "docs.zip"
    # open(zip_path, "wb").write(r.content)
    # with ZipFile(zip_path, 'r') as zipObj:
        # zipObj.extractall(actflowdir)
    # os.remove(zip_path)

    # download examples folder
    print("Downloading examples folder...");
    examples_url = "https://colelab.s3.us-east-2.amazonaws.com/examples.zip"
    r = requests.get(examples_url, allow_redirects=True)
    zip_path = actflowdir + "examples.zip"
    open(zip_path, "wb").write(r.content)
    with ZipFile(zip_path, 'r') as zipObj:
        zipObj.extractall(actflowdir)
    os.remove(zip_path)

    # # download network_definitions folder
    # print("Downloading network_definitions folder...");
    # network_definitions_url = "https://colelab.s3.us-east-2.amazonaws.com/network_definitions.zip"
    # r = requests.get(network_definitions_url, allow_redirects=True)
    # zip_path = actflowdir + "network_definitions.zip"
    # open(zip_path, "wb").write(r.content)
    # with ZipFile(zip_path, 'r') as zipObj:
        # zipObj.extractall(actflowdir)
    # os.remove(zip_path)
    
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
