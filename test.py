import os

def add_pending(file_path):
    print("Added "+file_path)

if __name__ == '__main__':
    matryoshka = 8;
    scan_extracted_files = True
    directory = os.getcwd()
    extraction_directory = "test"
    output = {}
    dd_file_path = "unknown..."
    # Loop through a list of newly created files (i.e., files that
    # weren't listed in the last directory listing)
    #if not has_key(last_directory_listing, extraction_directory):
    last_directory_listing = dict()
    last_directory_listing['test'] = {1, 2}
    last_directory_listing[extraction_directory] = set()

    directory_listing = set(os.listdir(extraction_directory))
    #for f in ["new1","new2","new3"]:
    for f in directory_listing.difference(last_directory_listing[extraction_directory]):
        # Build the full file path and add it to the extractor
        # results
        file_path = os.path.join(extraction_directory, f)
        real_file_path = os.path.realpath(file_path)
        #result(description=file_path, display=False)

        # Also keep a list of files created by the extraction utility.
        # Report the file_path, not the real_file_path, otherwise symlinks will be resolved and
        # the same file can end up being listed multiple times if there are symlinks to it.
        if real_file_path != dd_file_path:
            #output[r.file.path].extracted[r.offset].files.append(file_path)
            print("Append to output "+file_path)
        # If recursion was specified, and the file is not the same
        # one we just dd'd
        if (matryoshka and
            file_path != dd_file_path and
            scan_extracted_files and
                directory in real_file_path):
            # If the recursion level of this file is less than or
            # equal to our desired recursion level
            if len(real_file_path.split(directory)[1].split(os.path.sep)) <= matryoshka:
                # If this is a directory and we are supposed to process directories for this extractor,
                # then add all files under that directory to the
                # list of pending files.
                if os.path.isdir(file_path):
                    for root, dirs, files in os.walk(file_path):
                        for f in files:
                            full_path = os.path.join(root, f)
                            add_pending(full_path)
                # If it's just a add file, it to the list of pending
                # files
                else:
                    add_pending(file_path)
