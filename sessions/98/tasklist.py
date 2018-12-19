tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ReadMemory(2, 0x8809ec74, 4), Send, WaitMode.Wait], # Read memory to check RAM utilization before power cycle
    [tc.ReadMemory(3, 0x88018760, 3720), Send, WaitMode.Wait], # YAFFS_dev structure

    [tc.SendBeacon(), Send, WaitMode.Wait], # Wait until good communication
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ReadMemory(5, 0x8809ec74, 4), Send, WaitMode.Wait], # Read memory to check RAM utilization before power cycle
    [tc.ReadMemory(6, 0x88018760, 3720), Send, WaitMode.Wait], # YAFFS_dev structure

    # Set 9600
    [tc.SetBitrate(7, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    # Telemetry between session 96 and 98
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1890, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1902, 2280, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(25, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(12, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(37, 600, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1896, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.previous', [i for i in range(1908, 2280, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(6, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(18, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(31, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(43, 600, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
