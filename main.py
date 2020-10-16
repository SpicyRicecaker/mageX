import os.path
import easyocr
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

reader = easyocr.Reader(['ch_sim'])

if __name__ == "__main__":
    # patterns, ignore_patterns, ignore_directories, case_sensitive
    my_event_handler = PatternMatchingEventHandler(
        "*", "", True, False)

    def on_created(event):
        result = reader.readtext(os.path.basename(event.src_path), detail=0)
        print(result)
    def on_modified(event):
        result = reader.readtext(os.path.basename(event.src_path), detail=0)
        print(result)

    # my_event_handler.on_created = on_created
    my_event_handler.on_modified = on_modified

    print('setting up observer')
    my_observer = Observer()
    # event_handler, path, recursive=(t/f)
    my_observer.schedule(my_event_handler, ".", recursive=True)
    my_observer.start()
    print('ready')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
