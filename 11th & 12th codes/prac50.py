# os.rename() function is used to rename the name of exisiting file
import os

# Specify the old file name
current_name  = "file(for name change).txt"

# Specify the new name                      # abhi it is not changed run karne ke baad
new_name = "file(with changed name).txt"    # it will change.
# Rename the file
os.rename(current_name, new_name)