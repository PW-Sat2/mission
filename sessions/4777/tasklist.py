tasks = [
    # Generated on 2020-12-12 21:56:02.667000, contains telemetry from sessions 4776 to 4777.
    # The session starts on 2020-12-12 22:39:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [1178, 1228, 1278, 1328, 1378, 1203, 1253, 1303, 1353, 1191, 1241, 1291, 1341, 1391, 1215, 1265, 1315, 1365, 1185, 1235]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1285, 1335, 1385, 1197, 1247, 1297, 1347, 1209, 1259, 1309, 1359, 1221, 1271, 1321, 1371]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/b_w_p480_1_0', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/b_w_p480_1_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/b_w_p480_1_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/b_w_p480_2_0', [80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    # missing from previous session end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]