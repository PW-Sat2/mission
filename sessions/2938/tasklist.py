tasks = [
    # Generated on 2020-02-29 20:31:11.682000, contains telemetry from sessions 2937 to 2938.
    # The session starts on 2020-02-29 21:38:46+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [3, 53, 103, 153, 203, 28, 78, 128, 178, 16, 66, 116, 166, 216, 40, 90, 140, 190, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [110, 160, 210, 22, 72, 122, 172, 34, 84, 134, 184, 46, 96, 146, 196]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(7, '/radfet_33', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
 
    [tc.DownloadFile(40, '/t0w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t0n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t1w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t1n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t2w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t2n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t3w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t3n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t4w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t4n_480_0', range(0, 20)), Send, WaitMode.Wait],


    [tc.DownloadFile(50, '/t0w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t0n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t1w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t1n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t2w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t2n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t3w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t3n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t4w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t4n_480_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/t0w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t0n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t1w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t1n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t2w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t2n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t3w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t3n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t4w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t4n_480_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t0w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t0n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t1w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t1n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t2w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t2n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t3w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t3n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t4w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t4n_480_0', range(60, 80)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/t0w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t0n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t1w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t1n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t2w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t2n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t3w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t3n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t4w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t4n_480_0', range(80, 100)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]