from datetime import datetime
import os


class FileInfo(object):
    def __init__(self, file_path: str, is_stripped: bool = False) -> None:
        """Stores the file information"""

        # Store given information
        self.file_path = file_path
        self.is_stripped = is_stripped

        self.os_stat = None
        self.file_size = None
        self.created_time = None
        self.file_permissions = None

        self.refresh()

    def refresh(self) -> None:
        """Refresh the file info"""
        self.os_stat = os.lstat(self.file_path)
        self._reset()

    def _reset(self) -> None:
        """Reset file information"""
        # Creating the file info
        self.file_size = self.os_stat.st_size
        self.created_time = datetime.fromtimestamp(self.os_stat.st_ctime)
        self.file_permissions = oct(self.os_stat.st_mode)[2:]

    def __repr__(self) -> str:
        """String representation of FileInfo"""
        return f"Path: {self.file_path}\nFile Size: {self.file_size} bytes\nPermissions: {self.file_permissions}\nStripped: {self.is_stripped}\nCreated Time: {self.created_time}"


def get_file_info(file_path: str) -> FileInfo:
    """Find information about the file"""
    return FileInfo(file_path)


if __name__ == '__main__':
    result = get_file_info('../../vulnerable_binary/command_inj/cmd_inj.exe')
    print(result)
