#!/usr/bin/env python

import os
import stat
from os.path import realpath, dirname


def init_env():
    print 'Initializing ggg'
    template_path = os.path.join(dirname(realpath(__file__)), 'resources', 'template.sh')
    with open(template_path, 'r') as t:
        contents = t.read()

    current_dir = os.getcwd()
    print 'Setting up project in dir `' + current_dir + '`'

    source_dir = current_dir + '/src'
    os.mkdir(source_dir)

    env_dir = current_dir + '/env'
    env_bin_dir = env_dir + '/bin'

    os.mkdir(env_dir)
    os.mkdir(env_bin_dir)
    os.mkdir(env_dir + '/deps')

    exe_path = env_bin_dir + '/activate'

    with open(exe_path, 'w') as exe:
        exe.write(contents.replace("{{currentdir}}", current_dir))
    st = os.stat(exe_path)
    os.chmod(exe_path, st.st_mode | stat.S_IEXEC)
    print 'Successfully configured environment'
    print 'Run `source env/bin/activate` to activate'


def main():
    init_env()


if __name__ == '__main__':
    main()
