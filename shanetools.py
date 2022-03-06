# This tool is meant for windows only.
import os
import sys
import glob
import logging
# from datetime import datetime
# now = datetime.now()

path = ".\\Dump\\root\\doshin\\audio\\bgm\\samples"

musicDumpFolder = ".\\shanetools\\out\\bgm\\"

# logging.basicConfig(filename='shanetools-' + now + '.log', encoding='utf-8', level=logging.DEBUG)
def dump_bgm():
    
    print("\nDumping BGM...")
    print("Calling MusyXExtract...")
    os.system("python MusyXExtract.py .\\Dump\\root\\doshin\\audio\\bgm\\")
    # Get a list of the folders in the samples folder
    foldersToConvert = glob.glob(path + "\\**\\", recursive = True)
    # Remove the folder "." from the list since it's not a folder to convert

    foldersToConvert.pop(0)

    # Get a list of all the dsp files in the samples folder
    dspList = glob.glob(path + "\\**\\*.dsp", recursive = True)

    print("Calling VGAudioCli through shanetoolshelper...")

    print(dspList)

    for i in range(len(foldersToConvert)):
        fn=foldersToConvert[i].replace("\\Dump\\root\\doshin\\audio\\bgm\\samples\\", "" , 1).replace("\\", "").replace(".", "").replace("\\", "")
        print(".\\shanetoolshelper.bat " + musicDumpFolder + fn + ".wav \"" + dspList[i-2] + "\"")
        os.system(".\\shanetoolshelper.bat " + musicDumpFolder + fn + ".wav \"" + dspList[i-2] + "\"")

    print("Dumped BGM to /toolsOut/bgm.")



def repack_bgm():
    print("Repacking BGM...")
    foldersToRepack = glob.glob(path + "\\**\\", recursive = True)
    foldersToRepack.pop(0)
    foldersToRepack.pop(1)
    foldersToRepack.pop(-1)
    print(foldersToRepack)
    dspList = glob.glob(path + "\\**\\*.wav", recursive = True)
    # print(dspList)
    for i in range(len(dspList)):
        # fn=foldersToRepack[i].replace("\\Dump\\root\\doshin\\audio\\bgm\\samples\\", "" , 1).replace("\\", "").replace(".", "").replace("\\", "")
        # os.system(".\\sp2.bat \"" + dspList[i] + "\"")
        h = dspList[i].replace(".\\Dump\\root\\doshin\\audio\\bgm\\samples\\", " ")
        print(".\\sp2.bat \"" + dspList[i] + "\" "  "\"" + foldersToRepack[i] + h + "\"")
        # print(".\\sp2.bat \"" + dspList[i-2] + "\"")
        # print(foldersToRepack)


def dump_textures():
    print("Dumping Textures...")
    

def main():
    while True:
        print("<<<   Shane's Doshin Tools   >>>\n")
        print("    > What would you like to do?")
        print("        Dump")
        print("            > 1. Dump the BGM")
        print("        Repack")
        print("            > 2. Repack the BGM")
        print("        Other")
        print("            > 3. Exit\n")
        choice = input ("> ")
        if choice == "1":
            dump_bgm()
        elif choice == "2":
            repack_bgm()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            os.system("cls")
if __name__ == "__main__":
    main()