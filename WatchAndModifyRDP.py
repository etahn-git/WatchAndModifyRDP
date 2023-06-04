import os
import time
import shutil
import glob
from pathlib import Path
import subprocess
import pygetwindow as gw
import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem as item
import threading


def quit_action(icon, item):
    icon.stop()
    # Additional cleanup or exit actions can be added here


def watch_downloads_folder():
    # Path to the Downloads folder
    downloads_folder = os.path.expanduser("~") + "\\Downloads"
    rdp_files = glob.glob(downloads_folder + "\\*.rdp")
    processed_files = []
    is_processing = False

    while True:
        # Get the list of RDP files in the Downloads folder
        new_rdp_files = glob.glob(downloads_folder + "\\*.rdp")

        # Check for new RDP files
        for rdp_file in new_rdp_files:
            if rdp_file not in rdp_files:
                # New RDP file found
                rdp_files.append(rdp_file)
                if rdp_file not in processed_files and not is_processing:
                    is_processing = True
                    modify_and_launch_rdp_file(rdp_file)
                    processed_files.append(rdp_file)
                    is_processing = False

        time.sleep(5)


def modify_and_launch_rdp_file(rdp_file_path):
    renamed_rdp_file_path = rdp_file_path.replace('_', '')  # Remove underscore from the file name

    try:
        print(f"Renaming file: {rdp_file_path} -> {renamed_rdp_file_path}")
        os.rename(rdp_file_path, renamed_rdp_file_path)  # Rename the file
        print(f"Modifying file: {renamed_rdp_file_path}")
        modify_rdp_file(renamed_rdp_file_path)
        launch_rdp_file(renamed_rdp_file_path)
    except Exception as e:
        print(f"Error: {e}")


def modify_rdp_file(rdp_file_path):
    try:
        # Read the contents of the RDP file
        with open(rdp_file_path, 'r') as file:
            lines = file.readlines()

        # Modify the "use multimon" setting to 1
        modified_lines = []
        for line in lines:
            if line.lower().startswith('use multimon'):
                modified_lines.append('use multimon:i:1\n')
            else:
                modified_lines.append(line)

        # Write the modified contents back to the RDP file
        with open(rdp_file_path, 'w') as file:
            file.writelines(modified_lines)

    except Exception as e:
        print(f"Error: {e}")


def launch_rdp_file(rdp_file_path):
    try:
        # Open the modified RDP file
        print(f"Launching RDP file: {rdp_file_path}")
        subprocess.Popen([rdp_file_path], shell=True)

        # Wait for the connection to establish (adjust the sleep duration if needed)
        time.sleep(5)

        # Check if the file still exists before deleting
        if os.path.exists(rdp_file_path):
            delete_rdp_file(rdp_file_path)
        else:
            print("error")

    except Exception as e:
        print(f"Error: {e}")


def delete_rdp_file(rdp_file_path):
    try:
        # Delete the RDP file
        print(f"Deleting RDP file: {rdp_file_path}")
        os.remove(rdp_file_path)
    except Exception as e:
        print(f"Error: {e}")
        
def create_monitor_icon():
    # Create a blank image with transparent background
    icon = Image.new('RGBA', (64, 64), (0, 0, 0, 0))

    # Create a draw object
    draw = ImageDraw.Draw(icon)

    # Draw the monitor outline
    outline_width = 6
    outline_rect = [(outline_width, outline_width), (64 - outline_width - 1, 64 - outline_width - 1 - 10)]
    draw.rectangle(outline_rect, outline=(255, 255, 255))

    # Draw the monitor stand outline
    stand_height = 10
    stand_width = 14
    stand_x = 64 // 2 - stand_width // 2
    stand_outline_rect = [(stand_x, 64 - outline_width - stand_height), (stand_x + stand_width, 64 - outline_width)]
    draw.rectangle(stand_outline_rect, outline=(255, 255, 255))

    # Draw the monitor base outline
    base_width = 30
    base_height = 4
    base_x = 64 // 2 - base_width // 2
    base_y = 64 - outline_width - stand_height - base_height
    base_outline_rect = [(base_x, base_y), (base_x + base_width, base_y + base_height)]
    draw.rectangle(base_outline_rect, outline=(255, 255, 255))

    return icon


def create_system_tray_icon():
    # Create a system tray icon

    menu = (item('Quit', quit_action),)
    image = create_monitor_icon()
    icon = pystray.Icon("name", image, "WatchAndModifyRDP", menu)
    icon.run()


if __name__ == "__main__":
    threading.Thread(target=watch_downloads_folder, daemon=True).start()
    create_system_tray_icon()
