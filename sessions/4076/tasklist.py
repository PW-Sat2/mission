tasks = [
    # Generated on 2020-08-23 22:13:34.631000, contains telemetry from sessions 4075 to 4076.
    # The session starts on 2020-08-23 23:29:38+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(40, '/telemetry.current', [1517, 1567, 1617, 1667, 1717, 1542, 1592, 1642, 1692, 1530, 1580, 1630, 1680, 1730, 1554, 1604, 1654, 1704, 1524, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1624, 1674, 1724, 1536, 1586, 1636, 1686, 1548, 1598, 1648, 1698, 1560, 1610, 1660, 1710]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/a_w_12_59_0', [144, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a_w_12_59_0', [157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_w_13_00_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_w_13_00_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_13_00_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_13_00_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_13_00_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_13_00_0', [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_13_00_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_13_00_0', [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157]), Send, WaitMode.Wait],
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