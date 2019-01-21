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

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # manualy-generated telemetry start
	[tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1990, 2280, 12)]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1996, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(0, 860, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(12, 860, 24)]), Send, WaitMode.Wait],
	
	[tc.DownloadFile(34, '/telemetry.current', [i for i in range(6, 860, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(18, 860, 24)]), Send, WaitMode.Wait],
    # manualy-generated telemetry end
	
	[tc.RemoveFile(50, '/p10_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(51, '/p3_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(52, '/p4_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(53, '/p5_480_0'), Send, WaitMode.Wait],
	
	[tc.RemoveFile(54, '/p6_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(55, '/p7_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(56, '/p8_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(57, '/p9_480_0'), Send, WaitMode.Wait],

	[tc.ListFiles(58, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]