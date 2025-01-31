tasks = [
    # Generated on 2021-01-29 22:32:09.146000, contains telemetry from sessions 5066 to 5067.
    # The session starts on 2021-01-29 23:44:35+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [162, 212, 262, 312, 362, 187, 237, 287, 337, 175, 225, 275, 325, 375, 199, 249, 299, 349, 169, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [269, 319, 369, 181, 231, 281, 331, 193, 243, 293, 343, 205, 255, 305, 355]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(40, '/t01w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t01w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t01w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t01w_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/t01w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t01w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t01w_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t01w_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t01w_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/t01n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t01n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t01n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t01n_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(55, '/t01n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t01n_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t01n_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01n_0', range(180, 200)), Send, WaitMode.Wait],
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]