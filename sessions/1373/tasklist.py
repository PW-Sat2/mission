tasks = [
    # Generated on 2019-06-28 23:21:15.499000, contains telemetry from sessions 1372 to 1373.
    # The session starts on 2019-06-29 12:53:16+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [12, 62, 112, 162, 212, 37, 87, 137, 187, 25, 75, 125, 175, 225, 49, 99, 149, 199, 19, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [119, 169, 219, 31, 81, 131, 181, 231, 43, 93, 143, 193, 55, 105, 155, 205]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # 16th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_16'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # file download start
    [tc.DownloadFile(100, '/p2_128_0', [i for i in range(30, 38, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p3_128_0', [i for i in range(0, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(122, '/p2_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/p2_240_0', [i for i in range(105, 113, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(130, '/p3_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/p3_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/p3_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/p3_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(140, '/p4_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/p4_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/p4_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/p4_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(150, '/p5_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/p5_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/p5_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/p5_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(160, '/p6_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/p6_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/p6_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(163, '/p6_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(170, '/p7_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/p7_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(172, '/p7_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(173, '/p7_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(180, '/p8_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/p8_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/p8_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(183, '/p8_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(190, '/p9_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(191, '/p9_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(192, '/p9_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(193, '/p9_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(200, '/p10_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/p10_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/p10_240_0', [i for i in range(70, 105, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/p10_240_0', [i for i in range(105, 140, 1)]), Send, WaitMode.Wait],
    # file download end

    # auto-generated file remove start
    # auto-generated file remove end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]