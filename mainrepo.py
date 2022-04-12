import subrepo as sr
from subrepo.subrepo import print_subrepo

def print_mainrepo():
    print("Thank's to use mainrepo!")
    return

if __name__ == "__main__":
    print_mainrepo()
    print("sub version: " + sr.__version__)
    print_subrepo()