tasks = [
    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.DelayRebootToNormal(10, 48), Send, WaitMode.Wait], 

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ReadMemory(100, 2282733568, 231 * 3), Send, WaitMode.Wait],  
    [tc.ReadMemory(103, 2282734261, 231 * 3), Send, WaitMode.Wait],  
    [tc.ReadMemory(106, 2282734954, 231 * 3), Send, WaitMode.Wait],     
    [tc.ReadMemory(109, 2282735647, 231 * 3), Send, WaitMode.Wait],    
    [tc.ReadMemory(112, 2282736340, 231 * 3), Send, WaitMode.Wait],   
    [tc.ReadMemory(115, 2282737033, 231 * 3), Send, WaitMode.Wait],   
    [tc.ReadMemory(118, 2282737726, 231 * 3), Send, WaitMode.Wait],   
    [tc.ReadMemory(121, 2282738419, 231 * 3), Send, WaitMode.Wait],    
    [tc.ReadMemory(124, 2282739112, 231 * 3), Send, WaitMode.Wait],    
    [tc.ReadMemory(127, 2282739805, 231 * 3), Send, WaitMode.Wait],     
    [tc.ReadMemory(130, 2282740498, 231 * 2 + 77), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],     

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
