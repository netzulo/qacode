from sys import version_info
from os import path

class Utils(object):
    """All methods what i don't know where to include"""

    def get_file(version_py=version_info.major,file_path=None, file_name=None, encoding=None):
        """Returns file, py version and enconding parametrization"""        
        if not path.exists(file_path):
            raise IOError("Path '{0!s}' doesn't exists")
        if not path.exists(file_name):
            raise IOError("File '{0!s}' doesn't exists")        
        file_path_join = path.join(Utils.get_file_abspath(file_path), file_name)
        if encoding is None:
            with open(file_path_join) as f:
                return f.read()
        if version_py == 3:
            with open(file_path_join, encoding=encoding) as f:
                return f.read()
        if version_py == 2:
            with open(file_path_join) as f:
                return f.read().decode(encoding)

    def get_file_abspath(file=None):
        """Return absolute path for __file__ instance"""
        if file is None:
            raise IOError("File '{0!s}' doesn't exists")
        return path.abspath(path.dirname(file))
