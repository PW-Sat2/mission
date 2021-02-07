tasks = [
    # Generated on 2021-02-07 10:58:57.843000, contains telemetry from sessions 5116 to 5117.
    # The session starts on 2021-02-07 12:14:58+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1265, 1315, 1365, 1415, 1465, 1290, 1340, 1390, 1440, 1278, 1328, 1378, 1428, 1478, 1302, 1352, 1402, 1452, 1272, 1322]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1372, 1422, 1472, 1284, 1334, 1384, 1434, 1296, 1346, 1396, 1446, 1308, 1358, 1408, 1458]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
