
# 🕵️‍♂️ SUBDOMINATOR v2

SUBDOMINATOR v2 is a high-performance subdomain enumeration tool built with Python's asynchronous capabilities. It mimics the behavior of tools like `subfinder` but offers blazing fast performance, passive subdomain discovery via APIs, and brute-force enumeration using a wordlist. 

Created by: MJ DHURGESH  
Version: 2.0  
License: MIT

---

## 🚀 Getting Started

To install SUBDOMINATOR, clone the repository and install dependencies:

```bash
https://github.com/Dhurgesh-mj/Subdomainator-V2
cd Subdomainator-V2/
pip install -r requirements.txt
```

---

## 🛠️ Usage

Launch the tool using Python:

```bash
python main.py -h
```

This will show the help menu:

```
usage: main.py [-h] [-d DOMAIN] [-ld LIST] [-o OUTPUT] [-oJ JSON] [-oD OUTPUT_DIR]
               [-t THREADS] [--silent] [--timeout TIMEOUT]
               [--bruteforce] [--wordlist WORDLIST]

```

### 🔹 Examples

#### 1. Passive Scan on a Single Domain
```bash
python main.py -d example.com
```

#### 2. Brute-force Subdomains
```bash
python main.py -d example.com --bruteforce --wordlist wordlist.txt
```

#### 3. Scan Multiple Domains from a File
```bash
python main.py -ld domains.txt
```

#### 4. Export Results to Text or JSON
```bash
python main.py -d example.com -o output.txt
python main.py -d example.com -oJ output.json
```

#### 5. Save Results in Separate Files by Domain
```bash
python main.py -ld domains.txt -oD output_dir/
```

#### 6. Silent Mode (Only Subdomains Output)
```bash
python main.py -d example.com --silent
```

#### 7. Custom Thread Count and Timeout
```bash
python main.py -d example.com -t 25 --timeout 20
```

---

## 🔐 API Key Configuration

SUBDOMINATOR uses AlienVault OTX for passive subdomain discovery.  
To use this feature, edit the `config.json` file:

```json
{
  "otx": "your_otx_api_key",
  "alienvault": "your_otx_api_key"
}
```

You can get your free OTX API key from: https://otx.alienvault.com/api/

---

## 📂 Output Sample

```bash
$ python main.py -d hackerone.com --silent
api.hackerone.com
support.hackerone.com
assets.hackerone.com
```

Or save to file with:

```bash
$ python main.py -d hackerone.com -o result.txt
```

---

## 📁 Project Structure

```
SUBDOMINATOR/
├── main.py              # Main CLI script
├── config.json          # API keys for OTX
├── requirements.txt     # Required dependencies
├── core/
│   ├── runner.py        # Passive recon engine
│   └── brute.py         # Brute-force engine
```

## ⚠️ Disclaimer

This tool is intended **only for educational or authorized penetration testing** purposes.  
Do **not** use it on systems you don’t have explicit permission to test.  
The creator is **not responsible** for any misuse or damage caused.

---

## 👨‍💻 Author

**MJ DHURGESH**  
Cybersecurity Enthusiast 

---
