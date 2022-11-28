def fileExists(filename):
    try:
        f = open(filename, "x")
        f.close()
        return True
    except:
        return False