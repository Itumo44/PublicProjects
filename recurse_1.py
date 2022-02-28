from PIL import Image
import aspose.words as aw
import os
from dotenv import load_dotenv
load_dotenv()
STORAGE_PATH = os.getenv('STORAGE_PATH')


class PDFconverter():
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_type(self):
        filename = os.path.basename(self.file_path)
        filetypes = ['png', 'jpg', 'jpeg', 'doc', 'docx']
        for x in filetypes[:3]:
            if os.path.splitext(filename)[1].split('.')[1] == x:
                return 'image'

        for x in filetypes[3:]:
            if os.path.splitext(filename)[1].split('.')[1] == x:
                return 'word doc'

    def convert_doc(self):
        doc = aw.Document(self.file_path)
        result = doc.save(os.path.join(STORAGE_PATH, 'converted.pdf'))
        return result

    def convert_image(self):
        image1 = Image.open(self.file_path)
        im1 = image1.convert('RGB')
        result = im1.save(os.path.join(STORAGE_PATH, 'converted.pdf'))
        return result

    def convert_file(self):
        if self.get_file_type() == 'image':
            return self.convert_image()
        elif self.get_file_type() == 'word doc':
            return self.convert_doc()



