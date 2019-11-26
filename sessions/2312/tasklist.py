tasks = [
    # Generated on 2019-11-26 11:00:45.373000, contains telemetry from sessions 2311 to 2312.
    # The session starts on 2019-11-26 11:45:26+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [203, 253, 303, 353, 403, 228, 278, 328, 378, 216, 266, 316, 366, 416, 240, 290, 340, 390, 210, 260]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [310, 360, 410, 222, 272, 322, 372, 422, 234, 284, 334, 384, 246, 296, 346, 396]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]