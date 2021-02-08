tasks = [
    # Generated on 2021-02-08 22:26:03.584650, contains telemetry from sessions 5124 to 5125.
    # The session starts on 2021-02-08 23:24:33+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [640, 690, 740, 614, 664, 714, 764, 634, 684, 734, 646, 696, 746, 608, 658, 708, 758, 620, 670, 720]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(42, '/l01w', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/l01w', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/l01w', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/l01w', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/l01w', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/l01w', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/l01w', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/l01w', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/l01n', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/l01n', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/l01n', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/l01n', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/l01n', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/l01n', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/l01n', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/l01n', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/l02w', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/l02w', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/l02w', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/l02w', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/l02w', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/l02w', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/l02w', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/l02w', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/l02n', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/l02n', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/l02n', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/l02n', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/l02n', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/l02n', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/l02n', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/l02n', range(140, 160)), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.DownloadFile(81, '/l01w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/l01w_0', range(21, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/l01w_0', range(41, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/l01w_0', range(41, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/l01w_0', range(61, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/l01w_0', range(81, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/l01w_0', range(101, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/l01n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/l01n_0', range(20, 50)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/l01n_0', range(51, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/l02w_0', range(0, 30)), Send, WaitMode.Wait],

    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
