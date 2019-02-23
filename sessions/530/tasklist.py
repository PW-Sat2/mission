tasks = [
    # Generated on 2019-02-23 21:24:35.259462, contains telemetry from sessions 529 to 530.
    # The session starts on 2019-02-23 21:43:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [812, 862, 912, 962, 1012, 837, 887, 937, 987, 825, 875, 925, 975, 1025, 849, 899, 949, 999, 819, 869]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [919, 969, 1019, 831, 881, 931, 981, 1031, 843, 893, 943, 993, 855, 905, 955, 1005]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Wait for good comms
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove files
    [tc.RemoveFile(100, 'p1_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, 'p2_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, 'p3_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, 'p4_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, 'p5_128_0' ), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(110, 'p6_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(112, 'p7_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(114, 'p8_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(116, 'p9_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(118, 'p10_128_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # High res photos download
    # 'Chunks': 139, 'File': 'p2_480_0'
    [tc.DownloadFile(60, '/p2_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p2_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p2_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p2_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p2_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p2_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p2_480_0', [i for i in range(129, 139, 1)]), Send, WaitMode.Wait],

    # 'Chunks': 150, 'File': 'p3_480_0'
    [tc.DownloadFile(70, '/p3_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p3_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p3_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p3_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p3_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p3_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p3_480_0', [i for i in range(129, 150, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]