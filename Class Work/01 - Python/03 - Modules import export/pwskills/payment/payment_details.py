import os,sys
from os.path import join,dirname,abspath
sys.path.insert(1,abspath(join(dirname(__file__),'..')))
from course import course_details
def payment():
    print('This is my payment details')
course_details.course()