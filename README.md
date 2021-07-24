# XenForo-ProfilePhotos

# English:
Gets first profile photos within a user-specified range at forums based on XenForo.

Usage:
  Arguments:
        --url=<XenForo forum url to fetch profile photos>
        --dirname=<directory name to save images>
        --start=<number to start at>
        --stop=<number to stop at>
        --help  Display help text
  Example:
        python3 __main__.py --url=https://www.silicone-forum.com/ --dirname=test_silicone-forum --start=1 --stop=50
    This will create a directory named "test_silicone-forum" if it doesn't exist already. And it will store downloaded files in this folder. It will download first 50       profile photos if available. 
