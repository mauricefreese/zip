import argparse
from src.remove import delete_directory, clear_directory, delete_file_pattern, delete_files
from src.zipped import zip_directory, extract_directory
from src.move import move_directory

def main(args):
    """
    different cases for to do actions
    """
    
    if args.action == 'rm_dir':
        delete_directory()

    elif args.action == 'clear_dir':
        clear_directory()

    elif args.action == 'rm_file':
        delete_files()

    elif args.action == 'rm_ftype':
        pattern = args.pattern
        delete_file_pattern(pattern)

    elif args.action == 'zip_dir':
        zipname = args.zipname
        zip_directory(zipname)

    elif args.action == 'extr_dir':
        zipname = args.zipname
        extract_directory(zipname)

    elif args.action == 'mv_dir':
        move_directory()

    else:
        ValueError ("Parameter arg {} is not valid.".format(args.action))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Files - Directories Management')
    parser.add_argument('--action', type=str, dest='action', choices = ['rm_dir', 'clear_dir', 'rm_file', 'rm_ftype', 'zip_dir', 'extr_dir', 'mv_dir'], help='Action to do', required=True)
    parser.add_argument('--pattern', type=str, dest='pattern', help='File pattern type. Example: to delete all text files from a directory, add ".*txt"')
    parser.add_argument('--zipname', type=str, dest='zipname', help='Zip or Unzip name', default='test.zip')
    args = parser.parse_args()
    main(args)