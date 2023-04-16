import os   #The os module allows us to access functionality of the underlying operating system. So we can perform tasks such as: navigate the file system, obtain file information, rename files, search directory trees, fetch environment variables, and many other operations. 
'''Its a built-in module so don't need to install any third party libraries.'''
#print(dir(os)) #all the attribtes and methods which are present in this module.
'''
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAPS D:\python_practice\hands_on> python .\os_module.py
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 
'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
'''

print(os.getcwd()) # to know about the current working directory.
print(os.listdir()) # to know about the files present in the current directory.

'''If we want to create a folder in the current directory'''
#os.mkdir('new_folder') #to create only top level directory only if this directory is not already created
#os.makedirs('new_folder2/child_dir') # to create top level direcory as well as sub-directory.
print(os.listdir())

'''To delete the directory'''
#os.rmdir('new_folder') #to delete the directory
#os.removedirs('new_folder2/child_dir') #to delete the directory as well as sub-directory.

'''Rename a file or folder'''
#os.rename('abc.py', 'sum.py') #os.rename(old_file_name, new_file_name)
print(os.listdir())

print(os.stat('sum.py')) #to know the info about file o/p: os.stat_result(st_mode=33206, st_ino=281474976722716, st_dev=1719336346, st_nlink=1, st_uid=0, st_gid=0, st_size=80, st_atime=1681582628, st_mtime=1681466899, st_ctime=1681466899)
print(os.stat('sum.py').st_mtime) # o/p: last modified time = 1681466899.7245493 
'''since last modified time is not readable to import dateime '''
from datetime import datetime
last_modified_time = os.stat('sum.py').st_mtime
print(datetime.fromtimestamp(last_modified_time)) #o/p: 2023-04-14 15:38:19.724549

'''To walk to the directory and its sub-directory and the files in the direcory tree then use os.walk'''

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Directory_path: ",dirpath)
    print("Directory_names: ",dirnames)
    print("file_names: ",filenames)

'''get environment variables'''
print("home environmet variables: ",os.environ.get('HOME'))
#if we want to add a file 'new.py' on the home directory then
#file_new_path = os.environ.get('HOME') + 'new.py'
#print(file_new_path) # bt this could create problem while concatinating like forward slashes will not be at right position. so will use os.path
file_new_path = os.path.join(r'D:\python_practice\hands_on\new_folder', 'new.py') #sing r the \n will also be printed
print(file_new_path)

with open(file_new_path,'w') as f:
    f.write("I am writing data into a file.")

print(os.path.basename('/tmp/text.py'))    
print(os.path.dirname('/tmp/text.py'))    
print(os.path.split('/tmp/text.py'))    #o/p: returns ('/tmp', 'text.py') directory name first then basename.

print(os.path.exists('/tmp/text.py'))  #o/p: False, returns boolean values if the path is a fake path or it really exists.


