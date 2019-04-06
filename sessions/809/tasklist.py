tasks = [
    # Generated on 2019-04-06 12:26:06.860000, contains telemetry from sessions 808 to 809.
    # The session starts on 2019-04-06 13:02:41+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # 10th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_10'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [173, 223, 273, 323, 373, 198, 248, 298, 348, 186, 236, 286, 336, 386, 210, 260, 310, 360, 180, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [280, 330, 380, 192, 242, 292, 342, 392, 204, 254, 304, 354, 216, 266, 316, 366]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]