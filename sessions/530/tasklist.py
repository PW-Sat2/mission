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

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]