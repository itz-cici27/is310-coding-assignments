# Social Media Use Diary

A data-curation tool for logging social media use, built in two forms: a command-line app (`cli_data_entry.py`) and an HTML page (`social_media_diary.html`). Both collect the same fields and save them in the same CSV format.

This connects to our group project on how social media, gaming, mental health, and sleep relate to academic performance among US university students. It works as a pilot for a one-week diary study with UIUC undergraduates, where each participant logs every time they use a social media app.

## What it collects

Each entry is one session of social media use:

| Field | Description |
|---|---|
| `date` | Date of use (YYYY-MM-DD) |
| `platform` | Instagram, TikTok, YouTube, Snapchat, X, Reddit, Discord, or Other |
| `minutes` | Minutes spent (whole number above 0) |
| `time_of_day` | Morning, Afternoon, Evening, or Late night |
| `purpose` | School, Social, Entertainment, News, or Other |
| `interrupted_studying` | Yes or No |
| `notes` | Optional free text |

## Setup

From the repository root, create and activate a virtual environment.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Then install the requirements:

```bash
python -m pip install -r python-libraries/requirements.txt
```

## How to run

**CLI:** from the repository root, run

```bash
python python-libraries/cli_data_entry.py
```

The script shows example entries, asks for each field, displays your entry for review, and saves it only after you confirm. Answer `n` at the review step to re-enter it. Confirmed entries are appended to `social_media_diary.csv` in the `python-libraries` folder, and the full path is printed at the end.

**HTML:** open `social_media_diary.html` in any web browser. Fill in the form, choose **Review entry**, then **Save entry** (or **Edit entry** to fix it). After saving your entries, choose **Download CSV**. No installation is needed.

## Sample data

`social_media_diary.csv` is a sample file produced by the CLI.

## Comparing the two interfaces

**What each interface makes easier or harder.** The CLI is super quick once you're comfy in the terminal, and I love that it keeps adding to the same CSV every time you run it, so your diary just keeps growing! The downside is that you need Python and a virtual environment set up first, and you have to type your choices exactly. The HTML page is way more beginner friendly since there's zero setup and you can see every field at once, which is perfect for a study participant who's never coded before. The catch is that your entries disappear when you close the page, so you have to remember to hit download before you leave!

**Different choices about fields, instructions, or validation.** Both versions collect the exact same fields, but they handle mistakes pretty differently. The CLI checks your answers one at a time and asks again right away (like if you type a date in the wrong format or put 0 minutes). The HTML form waits until you click Review entry, then highlights every field that needs fixing all at once. Dropdowns and radio buttons in the HTML also make typos basically impossible, while the CLI has to work around them by listing the choices and accepting any capitalization. Plus, the HTML gets a cute little date picker instead of making you type the date out!

**What the AI contributed, and what I changed, rejected, or troubleshot.** Claude wrote the first versions of both the CLI and the HTML page, tested them, and fixed a few small bugs along the way (like making the choices case-insensitive and fixing "1 entries" to "1 entry"). It also walked me through setting up my virtual environment and explained parts of the code I didn't understand, like how `Path(__file__).parent` decides where the CSV gets saved. My main job was testing both versions myself, making my own sample data, regenerating my `requirements.txt`, and shaping the documentation so it actually sounded like me.

**What the AI contributed, and what I changed, rejected, or troubleshot.** Claude wrote the first versions of both the CLI and the HTML page. I tested them and fixed a few small bugs along the way (like making the choices case-insensitive so typing "tiktok" works). I also picked the social media diary topic because it connects to my group project and I chose CSV over JSON since it's easier to open in Excel and analyze later. I also had Claude walk me through setting up my virtual environment and explain parts of the code I didn't get at first, like how `Path(__file__).parent` decides where the CSV gets saved. Honestly, I didn't change much of the code itself since I was on a tight deadline, so my focus was on testing both versions and making my own sample data.

**Which interface better fits this material and intended user.** I think the HTML version is the better fit for a social media diary! The people logging entries would be regular UIUC undergrads, probably filling it out on their phones throughout the day right after scrolling, so it needs to be quick and easy with no setup. The CLI would be more useful for a researcher like me who's entering or cleaning up the data afterward.