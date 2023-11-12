# Xbox certkeys.bin Analyser

### Requirements
* certkeys.bin from an xbox one/series devkit
* Python 3.7>

### Usage
1. Download this repo
2. Drop your certkeys.bin file along with the analyser.py file
3. run ```python analyser.py```

### Output
Output will be a list of capabilities i.e. 

SRA_DEVKIT
SRA_DEVKIT_DEBUG
SRA_FILE_IO
SRA_STREAM
SRA_PUSH_DEPLOY
SRA_PULL_DEPLOY
SRA_PROFILING
SRA_JS_PROFILING
RECOVERY
VS_CRASH_DUMP
CRASH_DUMP
REMOTE_MGMT
VIEW_TRACING
TCR_TOOL
ALLOW_RETAIL_GAME_DUMP
GESTURE_BUILDER
SPEECH_LAB
SMARTGLASS_STUDIO
NETWORK_FIDDLER
ERA_DEVKIT
HW_BERINGSEA_DEBUG
ERA_DEVKIT_DEBUG
ERA_FILE_IO
ERA_STREAM
ERA_PUSH_DEPLOY
ERA_PULL_DEPLOY
ERA_EXTRA_MEM
ERA_PROFILING
VIRT_CAP_MS_DEVKIT_EQUIV

Refer to https://xboxoneresearch.github.io/wiki/certificates/ for more details

