
def extension(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower()
