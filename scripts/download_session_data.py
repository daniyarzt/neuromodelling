"""
Usage: python download_session_data.py session_id1 [session_id2 session_id3 ...]

Description:
    This script downloads session data from the Allen Brain Observatory for one or more session IDs using the AllenSDK library.

Arguments:
    session_id1, session_id2, session_id3, ...   : ID(s) of the session(s) for which data will be downloaded.

Optional Argument:
    None

Example:
    python download_session_data.py 715093703

    This command will download session data for the session with ID 715093703 and save it in the "./allendata" directory.

    python download_session_data.py 715093703 715093704 715093705

    This command will download session data for sessions with IDs 715093703, 715093704, and 715093705, respectively, and save them in the "./allendata" directory.

Note:
    - Make sure to have the AllenSDK library installed (`pip install allensdk`) before running the script.
    - The session ID(s) can be obtained from the Allen Brain Observatory website.
    - If no session IDs are provided, the script will not download any data.
    - The script saves the downloaded data in the "./allendata" directory by default. You can change this directory by modifying the "data_dir" variable in the script.
"""
import sys 
import os
from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache

arguments = sys.argv

# Change data_dir to download to a different directory
data_dir = "./allendata"

for i in range(1, len(arguments)):
    session_id = int(arguments[i])
    
    print(f'Downloading [{i} / {(len(arguments) - 1)}] session data with session_id = {session_id} in folder "{data_dir}"')

    print('Initializing EcephysProjectCache...')
    manifest_path = os.path.join(data_dir, "manifest.json")
    cache = EcephysProjectCache.from_warehouse(manifest=manifest_path)

    print('Requesting session data...')
    cache.get_session_data(session_id, timeout = 3000)


