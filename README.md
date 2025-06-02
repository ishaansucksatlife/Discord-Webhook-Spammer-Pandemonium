# Pandemonium Webhook Spammer 🔗💻

A powerful, multi-threaded Discord webhook spammer featuring a vibrant multi-color console theme, flexible configuration options, and robust retry handling for smooth operation.

> 💻 Built by **Plasma**
[![GitHub Stars](https://img.shields.io/github/stars/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium?style=for-the-badge)](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium?style=for-the-badge)](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/fork)

## 📚 Table of Contents

- [About](#pandemonium-webhook-spammer-)
- [Safety & Assurance](#safety-and-assurance)
- [Note](#️-note)
- [Features](#-features)
- [Requirements](#-requirements)
- [How It Works](#-how-it-works)
- [How To Use](#-how-to-use)
- [Configuration Options](#configuration-options)
- [Supported Modes](#-supported-modes)
- [Included Files](#-included-files)
- [License](#-license)
- [FAQ](#-faq)
- [Need Help?](#-need-help)

---

## 🛡️ Safety & Assurance <a id="safety-and-assurance"></a>

We understand that downloading `.exe` files can be a concern for many users. That's why we prioritize transparency and user trust.

✅ Both the executable file `PandemoniumWebhookSpammer.exe` **and the full source code** are provided for every release.

- **Executable (`.exe`):** For convenience, you can use the pre-built `.exe` even if you don’t have Python or any dependencies installed.
- **Source Code:** For those who prefer to inspect, verify, or run the tool directly from Python, the complete source code is included.

To ensure your safety, we have scanned the `PandemoniumWebhookSpammer.exe` file using [VirusTotal](https://www.virustotal.com/), a trusted online service that checks files against dozens of antivirus engines to detect malware or suspicious behavior.

🔗 **VirusTotal Scan Report:** [Click here to view the results](https://www.virustotal.com/gui/file/91f56a730589bb041e4de9328d8eb7f09bca54a96601fd008cdbc205c7daeacc)

> This scan confirms that the file contains no malware, spyware, or malicious behavior.

Some antivirus engines may flag this tool due to its automation and network request capabilities, as well as how it’s packaged as a `.exe`. Please note:  
> These are generic heuristic tags:

| **Engine**                                 | **Detection Name**                    | **What it Means**                                                                     |
| ------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------- |
| ALYac, BitDefender, GData, Emsisoft, eScan | Gen:Variant.Tedy.770190               | Generic heuristic detection — flags tools made using application packers.             |
| Antiy-AVL                                  | RiskWare/Win32.Kryptik.a              | Flags automation tools or executables that connect to the network frequently.         |
| Arcabit                                    | Trojan.Tedy.DBC08E                    | Heuristic flag due to behavior, **not** confirmed malicious payload.                  |
| Arctic Wolf                                | Unsafe                                | General warning — based on behavior, not confirmed malicious code.                    |
| CTX                                        | Exe.unknown.tedy                      | Marks unknown executables; often applied to custom-compiled or packed `.exe` files.   |
| SecureAge                                  | Malicious                             | Generic label for packed `.exe`; common for automation tools.                         |
| SentinelOne                                | Static AI - Suspicious PE             | AI/ML-based guess — no actual virus found, flagged for “possible risk.”               |
| Skyhigh (SWG)                              | BehavesLike.Win64.Suspicioustrojan.rc | Flags programs that send repetitive requests or rapid actions, like webhook spamming. |
| Zillya                                     | Tool.DDoS.Script.1                    | Flags tools that send repeated web requests (even if just for local testing).         |

> **🏷 Final Assurance:**

- No malicious payloads are present in this tool.
- You are free to use either the source code or the `.exe`, depending on your preference.
- We recommend downloading only from official links.
- If you have concerns, you may seek support in the Discord Support server.
> ✅ **No malicious behavior exists in this project.**

For additional peace of mind:
- The official source code is included for transparency and user verification.
- Only use the executable and source code from our [GitHub releases](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/releases) to ensure safety.

> **Disclaimer:** The `.exe` is provided for convenience. Always use software responsibly and in accordance with Discord’s Terms of Service.

If you have any doubts or questions, feel free to ask in our [Discord Support Server](https://discord.com/invite/HazvsVHxyE).


## ⚠️ Note

⚠️ This tool is Windows-optimized.
While it may work on Linux/macOS, full functionality (like terminal colors and smooth clearing) is designed with Windows consoles in mind.

Use responsibly — misuse can lead to webhook bans or account penalties.

## 🔥 Features

🎨 Multi-Color Console UI  
Vibrant terminal colors for a glowing, aesthetic interface.

⚙️ Rich User Configuration  
• Webhook URL  
• Custom username + avatar  
• Spam mode: fixed count or infinite  
• Thread count  
• Delay between requests

💥 Multi-Threaded Spamming  
Uses Python’s ThreadPoolExecutor for fast, parallel spamming.

🛡️ Auto-Retry & Rate-Limit Handling  
Handles Discord 429 rate limits smoothly using backoff + retries.

🛑 Keyboard Stop Listener  
Press Enter anytime to instantly stop the spamming process.

💡 Detailed Console Feedback  
Clear color-coded logs for successes, errors, and rate limits.

🚀 Infinite or Fixed Modes  
Choose between endless spam or a precise message count.

👾 Customizable Avatar + Username  
Override the default webhook name and icon for every message.



## 📦 Requirements

### To run **PandemoniumWebhookSpammer.exe** (Windows Executable):

- Windows operating system
- Internet connection

> **No Python installation or additional setup is required for the `.exe` file. Just download and run.**

---

### To run **PandemoniumWebhookSpammer.py** (Python Source Code):

- Python 3.8+ installed  
- Internet connection  
- The following Python package:
`requests`

### To install the dependency, run this command:
```bash
pip install requests
```



## 🚀 How It Works

- Runs directly in your terminal (Windows, macOS, or Linux)
- Sends messages to the provided Discord webhook URL
- Supports two modes:
  • **Fixed** — send a specific number of messages
  • **Infinite** — spam until manually stopped
- Allows multiple threads to increase speed
- Uses a retry system to handle Discord rate limits
- Press **Enter** anytime to gracefully stop the spammer
- Displays clear success, warning, and error messages in color
- **Choose your method:**  
  • Use the included `PandemoniumWebhookSpammer.exe` for instant access (no Python or dependencies required)  
  • Or run the provided Python source code if you prefer to inspect or run the tool yourself

---

## 🧪 How To Use

#### ✅ Using the Executable (`PandemoniumWebhookSpammer.exe`)

1. Double-click or run `PandemoniumWebhookSpammer.exe` in your terminal.
2. Enter the required inputs when prompted (webhook URL, message, mode, threads, delay).
3. The spammer will start sending messages based on your selected mode.
4. To stop spamming, press **Enter** anytime in the terminal.
5. After completion, choose whether to restart or exit.

#### 🐍 Using the Python Source Code

1. Make sure you have Python installed on your system.
2. Install any required dependencies listed in the project (see `requirements.txt` if provided).
3. Run the script in your terminal:
```
python PandemoniumWebhookSpammer.py
```
4. Follow the same prompts as above to use the tool.

## ⚙️ Configuration Options <a id="configuration-options"></a>

| Setting           | Description                                           |
| ----------------- | ----------------------------------------------------- |
| Webhook URL       | Full Discord webhook URL to target                    |
| Message           | The message content to send                           |
| Custom Username   | Override the webhook’s default username               |
| Custom Avatar URL | Optional custom avatar icon                           |
| Mode              | `1` = Fixed count; `2` = Infinite spam                |
| Iterations        | Number of messages (for fixed mode)                   |
| Threads           | Number of parallel threads to use (recommended: 1–10) |
| Delay (seconds)   | Time between each message to reduce rate limits       |



## 🧩 Supported Modes

• 📦 Fixed Mode → Sends a set number of messages and stops  

• ♾️ Infinite Mode → Sends messages continuously until you manually stop  





## 📂 Included Files

- `README.md` → This help file with setup instructions  
- `PandemoniumWebhookSpammer.exe` → The main executable spammer tool (no Python required)  
- `PandemoniumWebhookSpammer.py` → The full Python source code for running or inspecting the tool

## 📄 License

This project is proprietary software and is provided under the following terms:

- For personal use and non-commercial testing only
- Redistribution is allowed **only** with proper credit to the original author

You may **not**:

- Reverse-engineer, decompile, or modify the executable or source code
- Redistribute without giving credit
- Use this tool for illegal, malicious, or unauthorized purposes

By using this software, you agree to these terms.

## ❓ FAQ

#### ⚙️ Why does my antivirus flag the `.exe`?
Some antivirus engines use heuristic detection, meaning they flag **any** program that automates actions or sends repeated requests—even if it’s harmless. PandemoniumWebhookSpammer uses automated scripts and network requests, which can trigger these flags. You can always review the VirusTotal report linked above for full transparency.

#### 🖥️ Do I need Python installed to run the `.exe`?
No. The `PandemoniumWebhookSpammer.exe` file is a standalone executable that includes all dependencies. Just download and run—no Python or extra setup required.

#### 🌐 Does this tool work on Mac or Linux?
Currently, only Windows `.exe` builds are provided.  
If you want to use the tool on Mac or Linux, you can run the included Python source code with Python installed on your system.

#### 📦 Is the source code available?
Yes! The full source code is included in every release, alongside the `.exe`. This allows you to inspect and run the tool yourself on any platform with Python installed.

#### 🚨 Is using a webhook spammer safe and allowed?
This tool is provided for educational and testing purposes only.  
**Abuse of Discord webhooks (including spamming) is against Discord's Terms of Service and can result in account or server sanctions.** Always use responsibly and only with webhooks you own or have permission to test[2][4].

#### 🔗 Where can I get official releases?
Official builds and the latest source code are always posted on our [GitHub releases](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/releases). 

Never download from unofficial sources to avoid tampered or unsafe files.

## 💬 Need Help?

Join our **Discord Support Server**:  
👉 [![Pandemonium](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/HazvsVHxyE)

We’re happy to help with:

- 🐛 Bug reports  
- 💡 Feature suggestions  
- 🙋 General support

## 💻 Made by Plasma

Because sometimes, spamming is just about having control.

**Follow me online:**  
🔗 GitHub – [![Ishaansucksatlife](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ishaansucksatlife)

📱 Discord - [![Pandemonium](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/HazvsVHxyE)

## 🏷 Tags

`discord` `webhook` `automation` `python` `multi-threading` `spammer` `bot` `open-source`
