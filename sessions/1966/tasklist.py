tasks = [
    # Generated on 2019-10-05 11:40:55.317000, contains telemetry from sessions 1965 to 1966.
    # The session starts on 2019-10-05 12:59:51+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 28, 78, 128, 178, 16, 66, 116, 166, 216, 40, 90, 140, 190, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [110, 160, 210, 22, 72, 122, 172, 222, 34, 84, 134, 184, 46, 96, 146, 196]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Download radfet data
    [tc.DownloadFile(100, '/radfet_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    # Download low-res photos    
    [tc.DownloadFile(200, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]