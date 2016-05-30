import os
from six.moves.urllib.request import urlretrieve

def get_text8(expected_bytes):
    filename = "text8.zip"
    url = "http://mattmahoney.net/dc/"
    if not os.path.exists(filename):
        filename, _ = urlretrieve(url + filename, filename)
    if os.stat(filename).st_size == expected_bytes:
        print('Found and verified')
    else:
        raise Exception('Failed to verify. Try accessing through browser.')
    return filename

def read_text():
    filename = "text8.zip"
    f = zipfile.ZipFile(filename)
    for name in f.namelist():
        return tf.compat.as_str(f.read(name))
    f.close()

def download_and_read():
    expected_bytes = 31344016
    filename = get_text(expected_bytes)
    return read_text8(filename)

    

