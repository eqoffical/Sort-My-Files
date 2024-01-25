import os
import shutil
import subprocess

# Extensions
extensions = { 
    "Text": [".txt", ".csv", ".log", ".md", ".tex", ".cfg", ".ini"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".eps", ".raw", ".ico", ".psd", ".webp"],
    "Audio": [".mp3", ".wav", ".aac", ".wma", ".ogg", ".flac", ".alac", ".aiff", ".dsd", ".m4a", ".mid"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".mpeg", ".3gp", ".rmvb", ".m4v", ".vob"],
    "Archives": [".zip", ".rar", ".tar", ".7z", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".img", ".pkg", ".wad", ".pk3"],
    "Executable": [".exe", ".msi", ".apk", ".aab", ".app", ".com", ".run"],
    "Scripts": [".bat", ".sh", ".cgi", ".gadget", ".vbs", ".ps1", ".ahk", ".cmd", ".tcl"],
    "Databases": [".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".sql", ".json", ".csv", ".xml", ".dbf", ".dat", ".mysql", ".ora"],
    "Dev": [".c", ".cpp", ".h", ".hpp", ".java", ".class", ".jar", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss", ".less", ".php", ".py", ".rb", ".swift", ".go", ".dart", ".kotlin", ".scala", ".groovy", ".lua", ".perl"],
    "Links and Shortcuts": [".html", ".htm", ".xhtml", ".shtml", ".asp", ".aspx", ".jsp", ".do", ".action", ".rhtml", ".mhtml", ".hta", ".url", ".webloc", ".lnk"],
    "Office": [".doc", ".docx", ".docm", ".dotx", ".dotm", ".odt", ".rtf", ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".ods", ".csv", ".ppt", ".pptx", ".pps", ".ppsx", ".pptm", ".potx", ".potm", ".odp"],
    "Books": [".epub", ".mobi", ".pdf", "djvu", ".azw", ".azw3", ".ibooks", ".fb2", ".lit", ".pdb", ".cbz", ".cbr"]} 

# Change directory
path = input("\nEnter path to files you want to sort: ")
if not os.path.exists(path):
    print(f"Error: The directory path does not exist.")
    exit()
os.chdir(path)

# File list
print("Here is all files in your directory (folders exculded): ")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print("> " + entry)
        
confirmation = input("You want to sort it? (Y/N): ")

if confirmation.lower() == "y":
    print(f"Notification: You said yes.")
        
    # Move files into their corresponding category folder or the "Others" folder
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            for category, exts in extensions.items():
                if file_extension in exts:
                    folder_path = os.path.join(path, category)
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                    new_file_path = os.path.join(folder_path, filename)
                    try:
                        os.rename(file_path, new_file_path)
                        print(f"Success: moved {filename} to {category} folder.")
                    except Exception as exception_message:
                        print(f"Error: moving {filename} to {category} folder: {exception_message}.")
                    break  # Move on to the next file
            else:
                # File extension didn't match any categories, move to the "Others" folder
                other_path = os.path.join(path, 'Others')
                if not os.path.exists(other_path):
                    os.mkdir(other_path)
                new_file_path = os.path.join(other_path, filename)
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Success: moved {filename} to Others folder.")
                except Exception as exception_message:
                    print(f"Error: moving {filename} to Others folder: {exception_message}.")

elif confirmation.lower() == "n":
    print (f"Notification: You said no.")

else:
    print(f"Error: Invalid character."
          f"Notification: Enter Y for approval or N for rejection.\n")

input("Press any key to exit...")
