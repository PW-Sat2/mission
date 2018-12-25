tasks = [
    # ============================================================================
    # Sail experiment training on 1200
    # ============================================================================
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(500, 505, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(505, 510, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(510, 515, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(515, 520, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(520, 525, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Go/no-go for uplink/downlink?", Print, WaitMode.Wait],

    # ============================================================================
    # Ordinary and boring session on 9600
    # ============================================================================
    # Set 9600
    [tc.SetBitrate(8, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [[tc.SendBeacon(), 5], SendLoop, WaitMode.NoWait],

    # Telemetry between session 136 and 138
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(500, 1880, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(525, 1880, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(512, 1880, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(537, 1880, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 5], SendLoop, WaitMode.NoWait],
]