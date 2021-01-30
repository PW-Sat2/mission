tasks = [
    # Generated on 2021-01-30 22:13:04.454613, contains telemetry from sessions 5071 to 5072.
    # The session starts on 2021-01-30 22:58:31+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [448, 498, 548, 598, 648, 473, 523, 573, 623, 461, 511, 561, 611, 661, 485, 535, 585, 635, 455, 505]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [555, 605, 655, 467, 517, 567, 617, 479, 529, 579, 629, 491, 541, 591, 641]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [14, 314]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [294, 644, 2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait],
    # missing from previous session end

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
