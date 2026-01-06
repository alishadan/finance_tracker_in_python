from pathlib import Path
import os
def get_id():
    id_trans=1
    file_path = Path("info.txt")
    if os.path.isfile("info.txt") and os.path.getsize("info.txt")>0:
        with open("info.txt", "r") as f:
         id_trans = int(f.read().strip())
         id_trans+=1
         with open("info.txt","w") as f:
             f.write(str(id_trans))
    else:
         with open("info.txt","w") as f:
             f.write(str(id_trans))
    return id_trans

