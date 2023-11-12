# Xbox certkeys.bin Analyser

### Requirements
* certkeys.bin from an xbox one/series devkit
* Python 3.7>

### Usage
1. Download this repo
2. Drop your certkeys.bin file along with the analyser.py file
3. run ```python analyser.py```

### Output Sample

Magic: ?????  
Size: 1024  
Protocol Version: 1  
Issuer Key ID: 2  
Issue Date: ?????
SoC ID: ???????????????
Generation ID: 1  
Allowed States: 16  
Last Capability: 27  
Flags: 0  
Expire Date: 20-23-1 11:1:00  
Minimum SP Version: 18  
Minimum 2BL Version: 0  
Nonce: 00000000000000000000000000000000  
Reserved: 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  
Capabilities: SRA_DEVKIT, SRA_DEVKIT_DEBUG, SRA_FILE_IO, SRA_STREAM, SRA_PUSH_DEPLOY, SRA_PULL_DEPLOY, SRA_PROFILING, SRA_JS_PROFILING, RECOVERY, VS_CRASH_DUMP, CRASH_DUMP, REMOTE_MGMT, VIEW_TRACING, TCR_TOOL, ALLOW_RETAIL_GAME_DUMP, GESTURE_BUILDER, SPEECH_LAB, SMARTGLASS_STUDIO, NETWORK_FIDDLER, ERA_DEVKIT, HW_BERINGSEA_DEBUG, ERA_DEVKIT_DEBUG, ERA_FILE_IO, ERA_STREAM, ERA_PUSH_DEPLOY, ERA_PULL_DEPLOY, ERA_EXTRA_MEM, ERA_PROFILING  


Refer to https://xboxoneresearch.github.io/wiki/certificates/ for more details

