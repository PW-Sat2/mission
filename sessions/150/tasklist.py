tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # wait for better SNR
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(3, 0x88017fe8, 8), Send, WaitMode.Wait], # _bootTime value

    # Telemetry between sessions 148 and 150
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1200, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(0, 350, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1225, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(12, 350, 24)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]