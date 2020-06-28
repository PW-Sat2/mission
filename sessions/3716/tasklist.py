tasks = [
    # Generated on 2020-06-28 22:44:26.945000, contains telemetry from sessions 3715 to 3716.
    # The session starts on 2020-06-29 00:03:24+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1357, 1407, 1457, 1507, 1557, 1382, 1432, 1482, 1532, 1370, 1420, 1470, 1520, 1570, 1394, 1444, 1494, 1544, 1364, 1414]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1464, 1514, 1564, 1376, 1426, 1476, 1526, 1576, 1388, 1438, 1488, 1538, 1400, 1450, 1500, 1550]), Send, WaitMode.Wait],
    # auto-generated telemetry end

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