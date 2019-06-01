tasks = [
    # Generated on 2019-06-01 10:58:15.499000, contains telemetry from sessions 1178 to 1179.
    # The session starts on 2019-06-01 12:14:26+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [12, 62, 112, 162, 212, 37, 87, 137, 187, 25, 75, 125, 175, 225, 49, 99, 149, 199, 19, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [119, 169, 219, 31, 81, 131, 181, 231, 43, 93, 143, 193, 55, 105, 155, 205]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # 14th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_14'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # file download start
    [tc.DownloadFile(100, '/p2_128_0', [i for i in range(0, 33, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    # file download end



    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]