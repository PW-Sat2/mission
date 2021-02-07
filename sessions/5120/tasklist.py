tasks = [
    # Generated on 2021-02-07 21:25:22.666000, contains telemetry from sessions 5119 to 5120.
    # The session starts on 2021-02-07 22:43:51+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [136, 186, 236, 286, 336, 161, 211, 261, 311, 149, 199, 249, 299, 173, 223, 273, 323, 143, 193, 243]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [293, 343, 155, 205, 255, 305, 167, 217, 267, 317, 179, 229, 279, 329]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
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
    [tc.DownloadFile(60, '/t02w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t02w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t02w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t02w_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/t02w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t02w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t02w_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t02w_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t02w_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t02n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t02n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t02n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t02n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t02n_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(75, '/t02n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t02n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t02n_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t02n_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t02n_0', range(180, 200)), Send, WaitMode.Wait],

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]