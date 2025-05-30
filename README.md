# Pandemonium Webhook Spammer 🔗💻
 
An advanced multi-threaded Discord webhook spammer with a glowing multi-color console theme, rich configuration options, and detailed retry handling.

> 💻 Built by **Plasma**

---

## 🛡️ Safety & Assurance

We understand that downloading `.exe` files can be a concern for many users. That's why we prioritize transparency and user trust.

✅ The executable file `PandemoniumWebhookSpammer.exe` has been scanned and verified to be safe.

🔗 **VirusTotal Scan Report:** [Click here to view the results]([https://www.virustotal.com/gui/file/your-scan-report-link-here](https://www.virustotal.com/gui/file/91f56a730589bb041e4de9328d8eb7f09bca54a96601fd008cdbc205c7daeacc))

> This scan confirms that the file contains no malware, spyware, or malicious behavior.

Some antivirus engines may flag this tool due to its automation and network request capabilities, as well as how it’s packaged as a `.exe`. Rest assured:  
> These are generic heuristic tags:

| **Engine**                                 | **Detection Name**                    | **What it Means**                                                                     |
| ------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------- |
| ALYac, BitDefender, GData, Emsisoft, eScan | Gen\:Variant.Tedy.770190              | Generic heuristic detection — flags tools made using application packers.   |
| Antiy-AVL                                  | RiskWare/Win32.Kryptik.a              | Flags automation tools or executables that connect to the network frequently.         |
| Arcabit                                    | Trojan.Tedy.DBC08E                    | Heuristic flag due to behavior, **not** confirmed malicious payload.                  |
| Arctic Wolf                                | Unsafe                                | General warning — based on behavior, not confirmed malicious code.                    |
| CTX                                        | Exe.unknown.tedy                      | Marks unknown executables; often applied to custom-compiled or packed `.exe` files.   |
| SecureAge                                  | Malicious                             | Generic label for packed `.exe`; common for automation tools.                         |
| SentinelOne                                | Static AI - Suspicious PE             | AI/ML-based guess — no actual virus found, flagged for “possible risk.”               |
| Skyhigh (SWG)                              | BehavesLike.Win64.Suspicioustrojan.rc | Flags programs that send repetitive requests or rapid actions, like webhook spamming. |
| Zillya                                     | Tool.DDoS.Script.1                    | Flags tools that send repeated web requests (even if just for local testing).         |

> **🏷 Final Assurance:**

- No malicious payloads are hidden in this tool.

- We recommend downloading only from official links.

- If you’re worried, you may seek support in the Discord Support server.
> ✅ **No malicious behavior exists in this project.**

For additional peace of mind:
- The source code remains private to prevent tampering and unauthorized edits.
- Only use the official executable from our [GitHub releases](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/releases) to ensure safety.

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

To run **PandemoniumWebhook Spammer.exe**, you need:

- Python 3.8+ installed  
- Internet connection  
- The following Python packages:

```txt
requests
```

### To install the dependency, run this command:
```bash
pip install requests
```



## 🚀 How It Works

- Runs directly in your terminal (Windows, macOS, or Linux)  
- Sends messages to the provided Discord webhook URL  
- Supports two modes:  
  • Fixed — send a specific number of messages  
  • Infinite — spam until manually stopped  
- Allows multiple threads to increase speed  
- Uses a retry system to handle Discord rate limits  
- Press **Enter** anytime to gracefully stop the spammer  
- Displays clear success, warning, and error messages in color  



## 🧪 How To Use

 #### ✅ (`PandemoniumWebhookSpammer.exe`)

1. Double-click or run `PandemoniumWebhookSpammer.exe` in your terminal.
2. Enter the required inputs when prompted (webhook URL, message, mode, threads, delay).
3. The spammer will start sending messages based on your selected mode.
4. To stop spamming, press **Enter** anytime in the terminal.
5. After completion, choose whether to restart or exit.

## ⚙️ Configuration Options

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
- `PandemoniumWebhookSpammer.exe` → The main executable spammer tool  




## 📄 License

This project is proprietary software provided for:

- Personal use  
- Non-commercial testing

You may **not**:

- Reverse-engineer, decompile, or modify the executable  
- Redistribute it without credit  
- Use it for illegal or malicious purposes




## ❓ FAQ

#### ⚙️ Why does my antivirus flag the `.exe`?
Some antivirus engines use heuristic detection, meaning they flag **any** program that automates actions or sends repeated requests — even if it’s harmless. PandemoniumWebhookSpammer uses automated scripts, which can trigger these flags. You can review the VirusTotal report linked above for full transparency.



#### 🖥️ Do I need Python installed to run the `.exe`?
No. The `PandemoniumWebhookSpammer.exe` file is a standalone executable that includes all dependencies. Just download and run.



#### 🌐 Does this tool work on Mac or Linux?
Currently, only Windows `.exe` builds are provided. If you want to run it on other systems, you’ll need to run the Python source (Not Public).



#### 📦 Will you release the source code?
The project is currently closed-source to prevent abuse, tampering, and unauthorized redistribution. Official builds are always posted on our [GitHub releases](https://github.com/ishaansucksatlife/Discord-Webhook-Spammer-Pandemonium/releases).





## 💬 Need Help?

Join our **Discord Support Server**:  
👉 [Pandemonium](https://discord.com/invite/HazvsVHxyE)

We’re happy to help with:

- 🐛 Bug reports  
- 💡 Feature suggestions  
- 🙋 General support



## 💻 Made by Plasma

Because sometimes, spamming is just about having control.

**Follow me online:**  
🔗 GitHub – [@ishaansucksatlife](https://github.com/ishaansucksatlife)

📱 Discord - [Pandemonium](https://discord.com/invite/HazvsVHxyE)
