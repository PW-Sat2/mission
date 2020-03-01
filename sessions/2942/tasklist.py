tasks = [
    # Generated on 2020-03-01 11:08:36.555000, contains telemetry from sessions 2941 to 2942.
    # The session starts on 2020-03-01 12:18:51+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1620, 1670, 1720, 1770, 1820, 1645, 1695, 1745, 1795, 1633, 1683, 1733, 1783, 1833, 1657, 1707, 1757, 1807, 1627, 1677]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1727, 1777, 1827, 1639, 1689, 1739, 1789, 1839, 1651, 1701, 1751, 1801, 1663, 1713, 1763, 1813]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

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