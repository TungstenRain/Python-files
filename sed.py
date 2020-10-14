"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 14: Files in Think Python 2
    
    Note: Using Python 3.9.0
"""
def sed(pattern, replace, source, dest):
    """
        Reads a source file and writes the destination file.
        In each line, replaces pattern with replace.
    
        pattern: string
        replace: string
        source: string filename
        dest: string filename
    """
    # Open files
    fin = open(source, 'r')
    fout = open(dest, 'w') # destination file to be written to

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    # Close the files
    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_test.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()