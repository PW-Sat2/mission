tasks = [
    # Generated on 2020-02-01 22:06:19.057000, contains telemetry from sessions 2755 to 2756.
    # The session starts on 2020-02-01 22:42:43+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [358, 408, 458, 508, 558, 383, 433, 483, 533, 371, 421, 471, 521, 571, 395, 445, 495, 545, 365, 415]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [465, 515, 565, 377, 427, 477, 527, 577, 389, 439, 489, 539, 401, 451, 501, 551]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]