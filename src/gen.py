if __name__ == '__main__':
    for i in range(1, 26):
        filename = str(i) + ".py"
        f = open(filename, 'w')
        l1 = "import os"
        l2 = "\n"
        l3 = "\nif __name__ == \'__main__\':"
        l4 = "\n\tdirname=os.path.dirname"
        l5 = f"\n\tpath = os.path.join(dirname(dirname(__file__)), os.path.join(\"inputs\", \"{i}.txt\"))"
        l6 = "\n\tf = open(path)"
        f.writelines([l1,l2,l3,l4,l5,l6])
        f.close()