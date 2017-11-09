# coding:utf-8
# this is a simple example
import logging
import json
import os


# define the log file, file mode and logging level
logging.basicConfig(filename='example.log', filemode="w", level=logging.INFO)
SUCCESS = 'success'
projpath = 'project'
path = os.getcwd()
pro_path = os.path.join(path,projpath)

def new_project(project) -> str:
    pid = project['id']
    f_name = 'pid'+pid+'.json'
    f_path= os.path.join(pro_path,f_name)
    isExists = os.path.exists(pro_path)
    if isExists: 
        logging.info('already exit')
    else: 
        os.makedirs(pro_path)
    with open(f_path, 'w') as f:  
        f.write(json.dumps(project))
    return SUCCESS 

def projects_get() -> str:
    jj_aa= list()
    files = os.listdir(pro_path)
    for f in files:
        if f.startswith('pid'):
            j_file = os.path.join(pro_path,f)
            with open(j_file,'r') as load_f:
                load_dict = json.load(load_f)        
                jj_aa.append(load_dict)
    return jj_aa

def projects_id_delete(id) -> str:
    del_file = os.path.join(pro_path ,'pid' + id +'.json')
    move_file = os.path.join(pro_path ,'del_pid'+ id +'.json')
    os.rename(del_file ,move_file)
    return SUCCESS 

def projects_id_get(id) -> str:
    get_project = os.path.join(pro_path ,'pid' + id +'.json')
    with open(get_project ,'r') as load_f:
                load_dict = json.load(load_f)
    return load_dict 

