tasks = [
    # Generated on 2019-09-01 22:13:25.200000, contains telemetry from sessions 1762 to 1763.
    # The session starts on 2019-09-01 22:37:40+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1536, 1586, 1636, 1686, 1736, 1561, 1611, 1661, 1711, 1549, 1599, 1649, 1699, 1749, 1573, 1623, 1673, 1723, 1543, 1593]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1643, 1693, 1743, 1555, 1605, 1655, 1705, 1755, 1567, 1617, 1667, 1717, 1579, 1629, 1679, 1729]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]