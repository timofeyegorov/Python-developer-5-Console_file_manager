from directories import show_dirs, show_files
import yaml, os

def save_dir_content():
    dirs_list = show_dirs()
    files_list = show_files()
    to_yaml = {'dirs': dirs_list, 'files': files_list}
    with open('content_yaml.yaml', 'w') as f:
        yaml.dump(to_yaml, f)

if __name__ == '__main__':
    save_dir_content()
    with open('content_yaml.yaml', 'r') as f:
        y = f.read()
    print(y)
    print(type(y))
    # for el in y:
    #     print(el)
    print(os.listdir())