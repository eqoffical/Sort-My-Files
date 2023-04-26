import os
import shutil
import colorama
import subprocess

# terminal's customization
subprocess.run(['prompt 🧽 '], shell=True)
subprocess.run(['title Sort-My-Files'], shell=True)
subprocess.run(['cls'], shell=True)

# init colorama
colorama.init()

# messages
error = f"{colorama.Fore.RED}Error: "           # Error
notif = f"{colorama.Fore.BLUE}Notification: "  # Notification
end = f"{colorama.Style.RESET_ALL}"             # Reset all styles

# Extensions
"""
extensions = {
    "Text": [".txt", ".csv", ".log", ".md", ".tex", ".cfg"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".eps", ".raw", ".ico", ".psd", ".webp"],
    "Audio": [".mp3", ".wav", ".aac", ".wma", ".ogg", ".flac", ".alac", ".aiff", ".dsd", ".m4a", ".mid"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".mpeg", ".3gp", ".rmvb", ".m4v", ".vob"],
    "Archives": [".zip", ".rar", ".tar", ".7z", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".img", ".pkg", ".wad", ".pk3"],
    "Executable": [".exe", ".msi", ".apk", ".aab", ".app", ".com", ".run"],
    "Scripts": [".bat", ".sh", ".cgi", ".gadget", ".vbs", ".ps1", ".ahk", ".cmd", ".tcl"],
    "Databases": [".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".sql", ".json", ".csv", ".xml", ".dbf", ".dat", ".mysql", ".ora"],
    "Programming": [".c", ".cpp", ".h", ".hpp", ".java", ".class", ".jar", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss", ".less", ".php", ".py", ".rb", ".swift", ".go", ".dart", ".kotlin", ".scala", ".groovy", ".lua", ".perl"],
    "Links": [".html", ".htm", ".xhtml", ".shtml", ".asp", ".aspx", ".jsp", ".do", ".action", ".rhtml", ".mhtml", ".hta", ".url", ".webloc", ".lnk"],
    "Office": [".doc", ".docx", ".docm", ".dotx", ".dotm", ".odt", ".rtf", ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".ods", ".csv", ".ppt", ".pptx", ".pps", ".ppsx", ".pptm", ".potx", ".potm", ".odp"],
    "Books": [".epub", ".mobi", ".pdf", "djvu", ".azw", ".azw3", ".ibooks", ".fb2", ".lit", ".pdb", ".cbz", ".cbr"]
}
"""

# Change directory
path = input("\nEnter path to files you want to sort: ")
if not os.path.exists(path):
    print(f"{error}The directory path does not exist.{end}")
    exit()
os.chdir(path)

# Open file
"""
with open('data.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
    file.close()
"""

# File list
print("Here is all files in your directory (folders exculded): ")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print("> " + entry)
confirmation = input("You want to sort it? (Y/N): ")
if confirmation == "y":
    print("You said yea")

elif confirmation == "n":
    print (f"{notif} You said no.{end}")

else:
    print("bruh")