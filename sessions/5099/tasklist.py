tasks = [
    # Generated on 2021-02-04 11:24:45.434000, contains telemetry from sessions 5098 to 5099.
    # The session starts on 2021-02-04 11:39:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [157, 207, 257, 307, 357, 182, 232, 282, 332, 170, 220, 270, 320, 194, 244, 294, 344, 164, 214, 264]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [314, 364, 176, 226, 276, 326, 188, 238, 288, 338, 200, 250, 300, 350]), Send, WaitMode.Wait],
    # auto-generated telemetry end



    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]