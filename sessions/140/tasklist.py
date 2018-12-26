tasks = [
    # ============================================================================
    # Energy-saving session on 9600
    # ============================================================================

    ["Session 140", Print, WaitMode.NoWait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry between session 139 and 140 and becons
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(1952, 2140, 9)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(1955, 2140, 9)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(1958, 2140, 9)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]