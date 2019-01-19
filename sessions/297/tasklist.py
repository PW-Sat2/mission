tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],
    
    # ======= In case if telemetry.current was not overloaded
    # Skip to step 18 in case of error frames
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1100, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1124, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1112, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1136, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1106, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1118, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1130, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1142, 2280, 48)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # manualy-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1100, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1124, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(32, '/telemetry.previous', [i for i in range(1112, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [i for i in range(1136, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(34, '/telemetry.previous', [i for i in range(1106, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [i for i in range(1118, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [i for i in range(1130, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [i for i in range(1142, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(0, 30, 6)]), Send, WaitMode.Wait],

    # manualy-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]