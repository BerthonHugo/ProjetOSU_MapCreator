import os
import shutil

import Utils as util

file = ".osz file"
osz_file = ".zip beatmap pack"



def testRead():
    # util.readZip(file)
    # print("\n")
    util.checkOSZFile(file)
    print("\n")

def test_extract_osz():
    # name of the copy
    dest = "dest.osz"

    # to create a copy of the file
    shutil.copy2(file, dest)
    # extract file
    util.extractAll(dest,os.getcwd())
    # delete file after extraction
    util.deleteFileAfterExtraction(dest)

def test_write_archive():
    util.write_osz_archive("./dest","text_write_archive")

if __name__ == "__main__":
    testRead()
    # test_extract_osz()
    # test_write_archive()