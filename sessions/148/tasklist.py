tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # wait for better SNR
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(3, 0x88017fe8, 8), Send, WaitMode.Wait], # _bootTime value

    # Telemetry between sessions 147 and 148
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1060, 1250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1066, 1250, 12)]), Send, WaitMode.Wait],

    # Telemetry between session 145 and 147
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(36, 1060, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(48, 1060, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(61, 1060, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(73, 1060, 50)]), Send, WaitMode.Wait],

    # Telemetry between session 14:00 and 18:00 (SAA nad temperature peak)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(433, 1060, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(439, 1060, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(445, 1060, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(451, 1060, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]