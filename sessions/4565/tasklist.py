tasks = [
    # Generated on 2020-11-08 21:00:23.675931, contains telemetry from sessions 4564 to 4565.
    # The session starts on 2020-11-08 21:57:07+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [1341, 1391, 1441, 1491, 1541, 1366, 1416, 1466, 1516, 1354, 1404, 1454, 1504, 1554, 1378, 1428, 1478, 1528, 1348, 1398]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1448, 1498, 1548, 1360, 1410, 1460, 1510, 1372, 1422, 1472, 1522, 1384, 1434, 1484, 1534]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [523, 553, 573, 623, 629, 667, 673, 679, 703, 729, 753, 760, 779]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [829, 879, 1103, 1135, 1153, 1185, 1203, 1253, 1285, 1335, 1341, 1385]), Send, WaitMode.Wait],
    # missing from previous session end

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
