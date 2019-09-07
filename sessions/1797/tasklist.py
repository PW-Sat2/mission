tasks = [
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 220, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing, part 1
    [tc.DownloadFile(200, '/radfet_21', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]