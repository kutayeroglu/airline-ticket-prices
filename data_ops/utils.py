import os
from google.colab import drive

# def construct_full_path(drive_pathz, filename):

def ensure_drive_mounted(mount_path='/content/drive'):
    """
    Ensures that Google Drive is mounted at the specified path.

    Args:
    mount_path: The path where Google Drive should be mounted.

    Raises:
    OSError: If the drive is not mounted or is inaccessible.
    """

    # Check if the mount path exists and is a directory.
    if not os.path.exists(mount_path) or not os.path.isdir(mount_path):
        # Mount the drive using google.colab.drive.
        drive.mount(mount_path)
    else:
        print(f"Drive already mounted at {mount_path}.")

    # Check if the mount was successful.
    if not os.path.exists(mount_path) or not os.path.isdir(mount_path):
        raise OSError(f"Could not mount Google Drive at {mount_path}. "
                        "Please check your connection and try again.")


def ensure_datadir_exists(drive_images_dir, drive_annotations_path=None):
    ensure_drive_mounted()

    print(f"\nImage file directory: {drive_images_dir}")
    print("Does image directory exist?", os.path.exists(drive_images_dir))

    if drive_annotations_path is not None:  
        print(f"\nAnnotation file path: {drive_annotations_path}")
        print("Does annotation file exist?", os.path.exists(drive_annotations_path))