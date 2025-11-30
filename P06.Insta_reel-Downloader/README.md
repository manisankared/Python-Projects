📥 Instagram Reel Downloader (Python)

A lightweight Python script that lets you download Instagram Reels just by providing the reel link. It uses the instaloader library to pull the reel and save it locally.

⚙️ Key Features

Downloads reels from public Instagram accounts

Saves each reel into a folder named after the creator’s username

Simple command-line usage

Detects invalid, private, or broken links and handles errors cleanly

🔐 Requirements

Python 3.x

Install the required package:

pip install instaloader


Working internet connection

A valid public Instagram Reel URL

💻 How to Use

Open your terminal

Run the script:

python 5_insta_reel.py


Paste the reel link when asked

The reel will be saved inside a folder like:

<username>_reel/

🧪 Example
📥 Instagram Reel Downloader
Enter Reel URL: https://www.instagram.com/reel/XYZ123abc/
✅ Reel successfully downloaded from @creatorname

🚫 Error Handling

Wrong or malformed URL → “Invalid reel link.”

Private, deleted, or inaccessible reel → shows the exact error received from Instagram

📦 Technologies Used

Python 3.x

instaloader

Regex for link validation

Try-except for safe execution

📌 Why I Created This

I wanted a simple way to practice:

Using external Python libraries

Handling URL patterns

Building small but useful automation tools

📄 License

MIT License — open to use, modify, and share.

🙋‍♂️ About Me

I'm Manisankar, an AI and Data Science engineer who likes building practical automation tools and clean command-line utilities.

“If it can be automated, I’ll make it simpler.”