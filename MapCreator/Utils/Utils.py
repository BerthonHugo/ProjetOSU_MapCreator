import os
import zipfile


def readZip(file: str):
    with zipfile.ZipFile(file, mode="r") as archive:
        archive.printdir()


def checkOSZFile(file: str):
    name = file.split(".")
    if len(name) != 2 or name[1] != "osz":
        print("File is not an .osz file")
    else:
        try:
            with zipfile.ZipFile(file) as archive:
                archive.printdir()
        except zipfile.BadZipFile as error:
            print(error)

    # if zipfile.is_zipfile(fileName):
    #     with zipfile.ZipFile(fileName, "r") as archive:
    #         archive.printdir()
    # else:
    #     print("File is not an .osz file")


def extractAll(file: str, dirPath: str):
    """
    :param file: file path of the zip to extract
    :param dirPath: directory in which the zip will be extracted
    """
    with zipfile.ZipFile(file, 'r') as zip:
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(path=dirPath+"/"+file.split("/")[-1].split(".")[0])
        print('Done!')
def deleteFileAfterExtraction(file):
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def write_archive(file_paths,name:str):
    """
    :param file_paths: list of files to zip
    :param name: name of the zip file
    """
    # writing files to a zipfile
    with zipfile.ZipFile(f'{name}.osz', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')

def write_osz_archive(directory,name):
    """
    :param directory: directory in which the zip will be created
    :param name: name of the zip file
    """
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
    write_archive(file_paths, name)