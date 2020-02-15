tasks = [
    # Generated on 2020-02-15 21:44:41.413000, contains telemetry from sessions 2845 to 2846.
    # The session starts on 2020-02-15 23:01:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1197, 1247, 1297, 1347, 1397, 1222, 1272, 1322, 1372, 1210, 1260, 1310, 1360, 1410, 1234, 1284, 1334, 1384, 1204, 1254]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1304, 1354, 1404, 1216, 1266, 1316, 1366, 1416, 1228, 1278, 1328, 1378, 1240, 1290, 1340, 1390]), Send, WaitMode.Wait],
    # auto-generated telemetry end


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