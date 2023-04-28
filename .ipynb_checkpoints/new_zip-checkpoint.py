# libraries being used
import zipfile
import os
import shutil
import os.path
import stat
from os.path import basename
from shutil import make_archive
from shutil import copytree

# Text Style classes
class Color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
        
a = '2020'
# b = 'For all directory paths required, insert the ' + Color.BOLD + Color.MAGENTA + 'ABSOLUTE PATH' + Color.END + ' and ' + Color.BOLD + Color.UNDERLINE + Color.RED + 'NOT' + Color.END + ' the relative path.' 
c = 'Example:' 
# d = Color.UNDERLINE + 'Absolute Directory Path:' + Color.END + Color.UNDERLINE + Color.BOLD + ' S:\\' +'Clients'+ '\\' + Color.END +'Institution_Name'+ '\\' +'ALM'+ '\\' +'Historical'+ '\\' 
# e = Color.UNDERLINE + 'Relative Directory Path:' + Color.END + ' Instistution_Name' + '\\' +'ALM\Historical'+ '\\'

b = 'For all directory paths required, insert the ' + 'ABSOLUTE PATH' + ' and ' + 'NOT' + ' the relative path.' 
d = 'Absolute Directory Path:' + ' S:\\' +'Clients'+ '\\' + 'Institution_Name'+ '\\' +'ALM'+ '\\' +'Historical'
e = 'Relative Directory Path:' + ' Instistution_Name' + '\\' +'ALM\Historical'
print(b)
# print(Color.UNDERLINE + Color.MAGENTA + c + Color.END)
# print(Color.GREEN + d + a+  Color.END)
#print(Color.RED + e + a + Color.END)
print(c)
print(d + '\n' + e)

global folder
    # Abs path for Directory to zip
folder = os.path.join(str(input('Enter the directory that needs to be zipped: ')))
folder = os.path.normpath(folder)
# folder = os.path.abspath(os.path.normpath(os.path.expanduser(folder)))
'''
extension = ".zip"

#os.chdir(folder)  # Change directory from working dir to dir with files

# Look for and extract any zipped files before zipping
def unpack_all_in_dir(folder):
    for item in os.listdir(folder):  # Loop through items in dir
        abs_path = os.path.join(folder, item)  # Absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # Get full path of file
            print('Unzipping %s...' % (item))
            shutil.unpack_archive(file_name)
            os.remove(file_name)  # Delete zipped file
        #elif os.path.isdir(abs_path):
         #   unpack_all_in_dir(abs_path)  # Loop this function with inner folder

unpack_all_in_dir(folder)
'''

def backupToZip(folder):    
    # Figure out the filename this code should used based on what files already exist.
    # This is for if you input the whole "Historical" folder
# The first section zips the months
    for dirpath, dirnames, filenames in os.walk(folder):
        make_archive(dirpath,'zip',dirpath)
        for filename in filenames:
            print('Adding files %s...' % (filename))
            make_archive(filename,'zip',filename)
    print('Finished Zipping.')

# This deletes the archive 'year' folders in the main path
    for f in os.listdir(folder):
        folder_delete = folder + '\\' + f
        if folder_delete.endswith('.zip'):
            os.remove(folder_delete)

            # This deletes the non-zip months
    for f in os.listdir(folder):
        files = folder + '\\' + f
        for folders, subfolders, filenames in os.walk(files):    
            for sub in subfolders:
                f_delete = files + '\\' + sub
                if f_delete.endswith('.zip'):
                    continue
                else:
                        shutil.rmtree(f_delete)

# Cleans out CWD of copied zip files
    current = os.getcwd()
    for f in os.listdir(current):
        current_delete = current + '\\' + f
        if current_delete.endswith('.zip'):
            os.remove(current_delete)

# Removes archive of historical folder
    base = os.path.dirname(folder)
    for f in os.listdir(base):
        base_delete = base + '\\' + f
        if f == os.path.basename(folder) + '.zip':
            os.remove(base_delete)    

backupToZip(folder)


def singleZip():
    for f in os.listdir(folder):
        loose = os.path.join(folder,f)
        for f in os.listdir(loose):
            f = os.path.join(loose,f)
            if f.endswith('.xls') or f.endswith('.pdf') or f.endswith('.xlsx'):
                print('Loose files zipped: %s' % (f))
                zipf = zipfile.ZipFile(f+'.zip','w',zipfile.ZIP_DEFLATED)
                zipf.write(f,arcname=os.path.basename(f))
                zipf.close()
    print('Finished.')

            # This deletes the non-zip months
    for f in os.listdir(folder):
        files = folder + '\\' + f
        for folders, subfolders, filenames in os.walk(files):    
            for sub in filenames:
                f_delete = files + '\\' + sub
                if f_delete.endswith('.zip'):
                    continue
                else:
                        os.remove(f_delete)

    # Cleans out CWD of copied zip files
    current = os.getcwd()
    for f in os.listdir(current):
        current_delete = current + '\\' + f
        if current_delete.endswith('.zip'):
            os.remove(current_delete)

singleZip()
