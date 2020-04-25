tasks = [
    # Generated on 2020-04-25 11:37:12.451000, contains telemetry from sessions 3299 to 3300.
    # The session starts on 2020-04-25 12:53:05+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [5, 55, 105, 155, 205, 30, 80, 130, 180, 18, 68, 118, 168, 218, 42, 92, 142, 192, 12, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [112, 162, 212, 24, 74, 124, 174, 224, 36, 86, 136, 186, 48, 98, 148, 198]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # =========================================
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_37'), Send, WaitMode.Wait],
    # =========================================


    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.DownloadFile(42, '/t1w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t1n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t2w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t2n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t3w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t3n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t4w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t4n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t5w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t5n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/t6w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t6n_480_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/t1w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t1n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t2w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t2n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t3w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t3n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t4w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t4n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t5w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t5n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/t6w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/t6n_480_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/t1w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t1n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t2w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t2n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t3w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t3n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t4w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t4n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t5w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t5n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/t6w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/t6n_480_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(72, '/t1w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t1n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t2w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t2n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t3w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t3n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t4w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t4n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t5w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t5n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/t6w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/t6n_480_0', range(60, 80)), Send, WaitMode.Wait],

    [tc.DownloadFile(82, '/t1w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t1n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t2w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t2n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t3w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t3n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t4w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t4n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t5w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t5n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/t6w_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/t6n_480_0', range(80, 100)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]