# import os.path
import easyocr
import time


if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim'])
    # patterns, ignore_patterns, ignore_directories, case_sensitive
    result = reader.readtext('five.png', detail=0)
    print(result)
