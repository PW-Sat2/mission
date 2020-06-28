tasks = [
    # Generated on 2020-06-28 21:09:43.633000, contains telemetry from sessions 3714 to 3715.
    # The session starts on 2020-06-28 22:28:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(44, '/telemetry.current', [1191, 1241, 1291, 1341, 1391, 1216, 1266, 1316, 1366, 1204, 1254, 1304, 1354, 1404, 1228, 1278, 1328, 1378, 1198, 1248]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1298, 1348, 1398, 1210, 1260, 1310, 1360, 1222, 1272, 1322, 1372, 1234, 1284, 1334, 1384, 1093, 1143, 1193]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/dummy_15_33_0', [80, 100, 102, 104, 107, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/dummy_15_33_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/dummy_16_33_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/dummy_16_33_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/dummy_16_33_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/dummy_16_33_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/dummy_16_33_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/dummy_16_33_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/dummy_18_04_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/dummy_18_04_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/dummy_18_04_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/dummy_18_04_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/dummy_18_04_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # DEEP SLEEP
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]