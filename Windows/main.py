import ctypes
import logging
import sys

from WritingToolApp import WritingToolApp

# Set up logging to console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load user32.dll for Windows API calls
user32 = ctypes.windll.user32


def main():
    """
    The main entry point of the application.
    """
    app = WritingToolApp(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()