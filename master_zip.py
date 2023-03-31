import zipfile, os
import shutil
import os.path
import stat
from os.path import basename

    # Text Style class
class Color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
        
a = '2020'
b = 'For all directory paths required, insert the ' + Color.BOLD + Color.MAGENTA + 'ABSOLUTE PATH' + Color.END + ' and ' + Color.BOLD + Color.UNDERLINE + Color.RED + 'NOT' + Color.END + ' the relative path.' 
c = 'Example:' 
d = Color.UNDERLINE + 'Absolute Directory Path:' + Color.END + Color.UNDERLINE + Color.BOLD + ' S:\\' +'Clients'+ '\\' + Color.END +'Institution_Name'+ '\\' +'ALM'+ '\\' +'Historical'+ '\\' 
e = Color.UNDERLINE + 'Relative Directory Path:' + Color.END + ' Instistution_Name' + '\\' +'ALM\Historical'+ '\\'
print(b)
print(Color.UNDERLINE + Color.MAGENTA + c + Color.END)
print(Color.GREEN + d + a+  Color.END)
print(Color.RED + e + a + Color.END)

global folder
    # Abs path for Directory to zip
folder = os.path.join(str(input('Enter the directory that needs to be zipped: ')))
folder = os.path.abspath(os.path.normpath(os.path.expanduser(folder)))

extension = ".zip"

#os.chdir(folder)  # Change directory from working dir to dir with files

# Look for and extract any zipped files before zipping
def unpack_all_in_dir(folder):
    for item in os.listdir(folder):  # Loop through items in dir
        abs_path = os.path.join(folder, item)  # Absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # Get full path of file
            os.chmod(file_name, stat.S_IWRITE) # Changes from file permissions
            zip_ref = zipfile.ZipFile(file_name)  # Create zipfile object
            zip_ref.extractall(folder)  # Extract file to dir
            zip_ref.close()  # Close file
            os.remove(file_name)  # Delete zipped file
        elif os.path.isdir(abs_path):
            unpack_all_in_dir(abs_path)  # Loop this function with inner folder

unpack_all_in_dir(folder)

def backupToZip(folder):    
    # Figure out the filename this code should used based on 
    # what files already exist.
    zipFilename = os.path.basename(folder) + '.zip'


    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
    
    # Prints pathway of Directory to send to
    final_path = os.getcwd() + '\\' + backupZip.filename
    original = final_path
    target = os.path.join((input('What path do you want this zipped file to be transferred to?: ')))
    shutil.move(original,target)
    shutil.rmtree(folder)
    print('Deleting: ', folder)

#    for f in os.listdir(folder):
  # Folder = os.path.join(path + f)
 #       folder_delete = folder + '\\' + f
 #       if folder_delete.endswith('.zip'):
 #           continue
 #       shutil.rmtree(folder_delete)
 #       shutil.rmtree(folder)
 #       print('Deleteing Folder(s): \n', folder_delete,'\n', folder)

    
backupToZip(folder)
# backupToZip('C:\\Users\\mfreese\\Downloads\\Side work notes')