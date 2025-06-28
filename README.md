# 🧠 Python Voice Assistant

This is a Python-based voice assistant that responds to your spoken commands and performs various tasks like opening websites, searching Wikipedia, telling the time, launching applications, and more.

You can choose between a **Male Assistant (Jarvis)** or a **Female Assistant (Friday)** — giving it a more personalized and fun interaction experience! The names for Male and Female assistant are inspired from Tony Stark's AI assistants in Marvel Comics/ Cinematic Universe.

![IronManTonyStarkGIF](https://github.com/user-attachments/assets/3338ba74-b7c7-4d6d-ab26-7cf2e461bfa0)



---

## 🧰 Features

- 🎙️ **Voice Input**: Uses your microphone to take voice commands.
- 🧠 **Voice Output**: Responds to you with voice using `pyttsx3`.
- 📖 **Wikipedia Search**: Asks and reads out summaries.
- 🌦️ **Weather Updates**: Ask your assistant "What's the weather in Mumbai?" and get real-time weather info (uses OpenWeatherMap API + `.env` for key management).
- 🌐 **Open Websites**:
  - YouTube
  - Google
  - Spotify
  - Codedex
- ⏰ **Tells Current Time**
- ⚙️ **Opens Applications** (like VS Code)
- 🃏 **Tells Jokes & Motivational Quotes**
- 📰 **Tells News headlines**: Ask assistant "Tell me today's news" and get upto 5 news headlines along with their short description (uses News API + `.env` for key management).
- 🧑‍🚀 **Voice Selection**: Choose between Male (Jarvis) and Female (Friday)

📌 *Note:* For Weather updates feature get your API key from https://openweathermap.org/api and for News updates feature get your API key from https://newsapi.org/

Place those inside `.env` like:
```
Weather_API_KEY=your_weatherapi_key_here
News_API_KEY=your_newsapi_key_here
```


---

## 📦 Requirements

Install the dependencies using pip:

```
pip install -r requirements.txt
```
## 🚀 How to Use

1. Run the script:
```
python jarvis.py
```

2. Choose your assistant:
```
1. Male 👨  (Jarvis)
2. Female 👩 (Friday)
```

3. Speak a command like:
- "Tell me about Python"
- "Open YouTube"
- "What’s the time?"
- "Open VS Code"

---

## 🧠 Voice Assistant Logic

- **Jarvis** = Male voice  
- **Friday** = Female voice  

The assistant will greet you based on your voice choice and respond accordingly.

---

## 💡 Future Ideas

- Email automation  
- Remember notes (simple to-do feature)  

---

## 🙌 Author

**Sarthak Satish Deshmukh**  
- [LinkedIn](https://www.linkedin.com/in/sarthak-deshmukh-398316235)  
- [GitHub](https://github.com/sarthakkkk7)

---

> 🔊 “I am always listening, boss.” – Jarvis/Friday

![JarvisTellHerIMissHerGIF](https://github.com/user-attachments/assets/eb76a41d-4949-4438-b179-94c94fccf6cc)
