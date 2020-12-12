tasks = [
    # Generated on 2020-12-12 11:02:33.283000, contains telemetry from sessions 4773 to 4774.
    # The session starts on 2020-12-12 12:00:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 27, 77, 127, 177, 15, 65, 115, 165, 215, 39, 89, 139, 189, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [109, 159, 209, 21, 71, 121, 171, 33, 83, 133, 183, 45, 95, 145, 195]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # download experiment & photos

    [tc.DownloadFile(33, '/radfet_53', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/b_w_p480_0_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/b_n_p480_0_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/b_w_p480_1_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/b_n_p480_1_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/b_w_p480_2_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/b_n_p480_2_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/b_w_p480_0_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/b_n_p480_0_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/b_w_p480_1_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/b_n_p480_1_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/b_w_p480_2_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/b_n_p480_2_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/b_w_p480_0_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/b_n_p480_0_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/b_w_p480_1_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/b_n_p480_1_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/b_w_p480_2_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/b_n_p480_2_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/b_w_p480_0_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/b_n_p480_0_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/b_w_p480_1_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/b_n_p480_1_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/b_w_p480_2_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/b_n_p480_2_0', range(60, 80)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]