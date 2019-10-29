
# Create a latex template <path> <name>

import sys, os
from shutil import copyfile

if __name__ == "__main__":

    path = 'report'
    filename = 'report.tex'
    refs = 'references.bib'

    if len(sys.argv) > 1:
        path = sys.argv[1]
    if len(sys.argv) > 2:
        filename = sys.argv[2]
        if not filename.endswith('.tex'):
            filename += '.tex'
    
    if os.path.isdir(path):
        if os.path.exists(os.path.join(path, filename)):
            print('File {} already exists. Aborted.'.format(filename))
            exit(-1)
        if os.path.exists(os.path.join(path, refs)):
            print('File {} already exists. Aborted.'.format(refs))
            exit(-1)

    else:
        print('Creating directory {}'.format(path))
        os.mkdir(path)
    
    mypy_path = os.path.abspath(os.path.dirname(__file__))
    latex_path = os.path.join(mypy_path, 'latex/')
    
    print('Copying templates from {}'.format(latex_path))

    template_src = os.path.join(latex_path, 'template.tex')
    template_dst = os.path.join(path, filename)

    references_src = os.path.join(latex_path, refs)
    references_dst = os.path.join(path, refs)

    copyfile(template_src, template_dst)
    copyfile(references_src, references_dst)

    print('Done')