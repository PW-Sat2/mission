tasks = [
    # Generated on 2020-01-20 09:59:01.420000, contains telemetry from sessions 2673 to 2674.
    # The session starts on 2020-01-20 11:17:34+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [525, 575, 625, 675, 725, 550, 600, 650, 700, 538, 588, 638, 688, 738, 562, 612, 662, 712, 532, 582]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [632, 682, 732, 544, 594, 644, 694, 744, 556, 606, 656, 706, 568, 618, 668, 718]), Send, WaitMode.Wait],
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