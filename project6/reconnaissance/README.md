# Reconnaissance Evidence

Raw local-only outputs belong here:

```bash
nmap -sV -sC -oN reconnaissance/nmap.txt 127.0.0.1
dirb http://127.0.0.1/ -o reconnaissance/dirb.txt
nikto -h http://127.0.0.1/ -output reconnaissance/nikto.txt
```

Run these only after the local services are intentionally started. Do not overwrite existing evidence without review.