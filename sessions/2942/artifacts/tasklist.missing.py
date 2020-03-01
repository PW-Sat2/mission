tasks = [
[tc.DownloadFile(30, '/telemetry.current', [1620, 1627, 1633, 1639, 1645, 1651, 1657, 1663, 1670, 1677, 1683, 1689, 1695, 1701, 1707, 1713, 1720, 1727]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [1733, 1739, 1745, 1751, 1757, 1763, 1770, 1777, 1783, 1789, 1795, 1801, 1807, 1813, 1820, 1827, 1833, 1839]), Send, WaitMode.Wait]
]