import os

def find_pdf_size(top):
    total_size = 0
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.endswith('.pdf'):
                total_size += os.path.getsize(os.path.join(root, file))
    return total_size

print(find_pdf_size("."))
