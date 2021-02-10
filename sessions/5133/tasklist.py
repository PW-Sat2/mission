tasks = [
    # Generated on 2021-02-10 11:34:52.069815, contains telemetry from sessions 5132 to 5133.
    # The session starts on 2021-02-10 12:41:20+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [90, 140, 190, 240, 290, 115, 165, 215, 265, 103, 153, 203, 253, 303, 127, 177, 227, 277, 97, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [197, 247, 297, 109, 159, 209, 259, 121, 171, 221, 271, 133, 183, 233, 283]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(40, '/telemetry.previous', range(1240, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', range(1250, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', range(1245, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', range(1255, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', range(1241, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', range(1246, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', range(1251, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', range(1256, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', range(1242, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', range(1247, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', range(1252, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', range(1257, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', range(1243, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', range(1248, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', range(1253, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', range(1258, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', range(1244, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', range(1249, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', range(1254, 1600, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', range(1259, 1600, 20)), Send, WaitMode.Wait],

    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
