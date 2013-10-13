#!/usr/bin/env python

import os, stat, sys
from jinja2 import Environment, PackageLoader

def init_env():
    print 'Initializing gve'
    env = Environment(loader=PackageLoader('gve', 'resources'))
    t = env.get_template('template.sh')

    current_dir = os.getcwd()
    print 'Setting up project in dir `' + current_dir + '`'

    env_dir = current_dir + '/env'
    env_bin_dir = env_dir + '/bin'

    os.mkdir(env_dir)
    os.mkdir(env_bin_dir)
    os.mkdir(env_dir + '/deps')

    exe_path = env_bin_dir + '/activate'
    exe = open(exe_path, 'w+')
    
    exe.write(t.render(currentdir=current_dir))
    exe.close()
    st = os.stat(exe_path)
    os.chmod(exe_path, st.st_mode | stat.S_IEXEC)
    print 'Successfully configured environment'
    print 'To activate run `source env/bin/activate`'

def main():
    init_env()
    

if __name__ == '__main__':
    main()
