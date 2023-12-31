import struct

def read_certificate(filename):
    with open(filename, 'rb') as file:
        # Read fixed-size fields
        magic = struct.unpack('<H', file.read(2))[0]
        size = struct.unpack('<H', file.read(2))[0]
        protocol_version = struct.unpack('<H', file.read(2))[0]
        issuer_key_id = struct.unpack('<H', file.read(2))[0]
        issue_date = struct.unpack('<Q', file.read(8))[0]
        soc_id = file.read(16).hex()
        generation_id = struct.unpack('<H', file.read(2))[0]
        allowed_states = struct.unpack('B', file.read(1))[0]
        last_capability = struct.unpack('B', file.read(1))[0]
        flags = struct.unpack('<I', file.read(4))[0]
        expire_date = struct.unpack('BBBBBB', file.read(6))
        minimum_sp_version = struct.unpack('B', file.read(1))[0]
        minimum_2bl_version = struct.unpack('<Q', file.read(8))[0]
        nonce = file.read(16).hex()
        reserved = file.read(56).hex()

        # Capability Offset
        file.seek(0x80)

        ## Capability Mapping Borrowed from https://xboxoneresearch.github.io/wiki/certificates/
        capabilities = {
            0x2001: "SRA_DEVKIT",
            0x2002: "SRA_DEVKIT_DEBUG",
            0x2003: "SRA_FILE_IO",
            0x2004: "SRA_STREAM",
            0x2005: "SRA_PUSH_DEPLOY",
            0x2006: "SRA_PULL_DEPLOY",
            0x2007: "SRA_PROFILING",
            0x2008: "SRA_JS_PROFILING",
            0x3001: "RECOVERY",
            0x3002: "VS_CRASH_DUMP",
            0x3003: "CRASH_DUMP",
            0x3004: "REMOTE_MGMT",
            0x3005: "VIEW_TRACING",
            0x3006: "TCR_TOOL",
            0x3007: "ALLOW_RETAIL_GAME_DUMP",
            0x3008: "GESTURE_BUILDER",
            0x3009: "SPEECH_LAB",
            0x300A: "SMARTGLASS_STUDIO",
            0x300B: "NETWORK_FIDDLER",
            0x4001: "ERA_DEVKIT",
            0x4002: "HW_BERINGSEA_DEBUG",
            0x4003: "ERA_DEVKIT_DEBUG",
            0x4004: "ERA_FILE_IO",
            0x4005: "ERA_STREAM",
            0x4006: "ERA_PUSH_DEPLOY",
            0x4007: "ERA_PULL_DEPLOY",
            0x4008: "ERA_EXTRA_MEM",
            0x4009: "ERA_PROFILING",
            0x6001: "MS_DEVKIT",
            0x6002: "HW_CPU_DEBUG",
            0x6003: "HW_FW_DEBUG",
            0x6004: "HW_POWER_DEBUG",
            0x6005: "MEMENC_DISABLED",
            0x6006: "MEMENC_FIXED_KEY",
            0x6007: "MEMENC_KEY_0",
            0x6008: "CERT_MTE_BOOST",
            0x6009: "CERT_RIO_BOOST",
            0x600A: "CERT_TEST_BOOST",
            0x600B: "UPDATE_TESTER",
            0x600C: "RED_CPU_CODE",
            0x600D: "OS_PREVIEW",
            0x600E: "RETAIL_DEBUGGER",
            0x600F: "OFFLINE",
            0x6010: "IGNORE_UPDATESEQUENCE",
            0x6011: "CERT_QASLT",
            0x6013: "GPU_FENCE_DEBUG",
            0x6014: "HW_EN_MEM_SPEED_RETEST",
            0x6015: "HW_EN_MEM_1GB_RETEST",
            0x6016: "HW_EN_FUSE_READ",
            0x6017: "HW_EN_POST_CODE_SECURE",
            0x6018: "HW_EN_FUSE_OVR_RETEST",
            0x6019: "HW_EN_MEM_UNLIM_RETEST",
            0x601A: "ICT_TESTER",
            0x601B: "LOADXVD_TESTER",
            0x601C: "WIDE_THERMAL_THRESHOLDS",
            0x601D: "MS_TESTLAB",
            0x601E: "ALLOW_DISK_LICENSE",
            0x601F: "ALLOW_SYSTEM_DOWNGRADE",
            0x6020: "WIFI_TESTER",
            0x6021: "GREEN_FIDDLER",
            0x6022: "KIOSK_MODE",
            0x6023: "FULL_MEDIA_AUTH",
            0x6024: "HW_DEVTEST",
            0x6025: "ALLOW_FUSE_FA",
            0x6026: "ALLOW_SERIAL_CERT_UPLOAD",
            0x6027: "ALLOW_INSTRUMENTATION",
            0x6028: "WIFI_TESTER_DFS",
            0x6029: "HOSTOS_HW_TEST",
            0x602A: "HOSTOS_ODD_TEST",
            0x7001: "PR_SL2000",
            0x7002: "REDUCE_MODE_TESTER",
            0x8001: "SP_DEVKIT",
            0x8002: "HW_SP_DEBUG",
            0x8003: "SCP_DEBUG",
            0x8004: "HW_SDF",
            0x8005: "HW_ALL_DEBUG",
            0x8006: "HW_AEB_DEBUG",
            0x8007: "HW_BTG",
            0x8008: "SP_TESTER",
            0x8009: "SP_DEBUG_BUILD",
            0x800A: "NO_FUSE_BLOW",
            0x800B: "HW_DIS_N_CALIB_RETEST",
            0x800C: "HW_DIS_CRIT_FUSE_CHK_RETEST",
            0x800D: "GREEN_SRA_DEBUG",
            0x800E: "GREEN_ERA_DEBUG",
            0x800F: "HW_DIS_RNG_CHK_SECURE",
            0x8010: "HW_EN_FUSE_OVRD_SECURE",
            0x8011: "GREEN_HOST_DEBUG",
            0x8012: "GREEN_ALLOW_DISK_LICENSES",
            0xF001: "VIRT_CAP_DEVKIT_ANY_EQUIV",
            0xF002: "VIRT_CAP_DEVKIT_INTERNAL_EQUIV",
            0xF003: "VIRT_CAP_SP_DEVKIT_EQUIV",
            0xF004: "VIRT_CAP_MS_DEVKIT_EQUIV",
            0xF005: "VIRT_CAP_RED_SIGNED_CPU_CODE",
        }

        found_capabilities = []
        while file.tell() < 0x280:
            capability = int.from_bytes(file.read(2), byteorder='little')
            if capability in capabilities:
                found_capabilities.append(capabilities[capability])

        print(f"Magic: {magic}")
        print(f"Size: {size}")
        print(f"Protocol Version: {protocol_version}")
        print(f"Issuer Key ID: {issuer_key_id}")
        print(f"Issue Date: {issue_date}")
        print(f"SoC ID: {soc_id}")
        print(f"Generation ID: {generation_id}")
        print(f"Allowed States: {allowed_states}")
        print(f"Last Capability: {last_capability}")
        print(f"Flags: {flags}")
        print(f"Expire Date: {expire_date[0]}-{expire_date[1]}-{expire_date[2]} {expire_date[3]}:{expire_date[4]}:{expire_date[5]}")
        print(f"Minimum SP Version: {minimum_sp_version}")
        print(f"Minimum 2BL Version: {minimum_2bl_version}")
        print(f"Nonce: {nonce}")
        print(f"Reserved: {reserved}")
        print(f"Capabilities: {', '.join(found_capabilities)}")

filename = "certkeys.bin"
read_certificate(filename)