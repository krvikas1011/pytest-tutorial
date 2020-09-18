import os


class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    """https://pypi.org/project/pytest-mock/"""
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
