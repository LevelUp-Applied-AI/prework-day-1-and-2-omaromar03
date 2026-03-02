## Compute Log — PR 4

==================================================
SYSTEM INFORMATION
==================================================
OS:         Linux 6.6.87.2-microsoft-standard-WSL2
Version:    #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
Machine:    x86_64
Processor:  x86_64
Python:     3.11.14 (main, Oct 10 2025, 08:54:04) [GCC 13.3.0]

Benchmark 1 — sum(range(5,000,000))
  Result:  12,499,997,500,000
  Time:    0.0918 seconds

Benchmark 2 — list comprehension (n=1,000,000)
  First 5: [0, 1, 4, 9, 16]
  Time:    0.1728 seconds

Benchmark 3 — string join (n=100,000)
  Length:  588,889 characters
  Time:    0.0216 seconds

==================================================
SUMMARY
==================================================
  sum benchmark:    0.0918s
  list benchmark:   0.1728s
  string benchmark: 0.0216s

## RAM

Total RAM:  3.7 GiB
