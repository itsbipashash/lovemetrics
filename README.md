# 💕 LoveMetrics — Relationship Analytics for Long-Distance Couples

> "What if you could understand your relationship the same way startups understand their users?"

## 📌 What is this?

LoveMetrics is a data analytics project that extracts insights from WhatsApp chat history between long-distance couples — revealing communication patterns, emotional trends, and connection scores.

Built as both a **personal data project** and an **early-stage startup idea**.

---

## 📊 What insights does it generate?

| Metric | Insight |
|---|---|
| Message volume | Who texts more and by how much |
| Peak hours | What time you both talk most |
| Message length | Who writes longer, more thoughtful texts |
| Monthly activity | Which months had the strongest connection |
| Sentiment (coming soon) | Emotional tone over time |
| Connection score (coming soon) | A single health score for the relationship |

---

## 🔍 Key Findings (Sample Dataset)

- 📱 **39,653 total messages** analyzed
- 🌙 **11PM is peak hour** — late night conversations dominate
- 💬 One partner sends **56% of all messages**
- 📅 **February was the most active month** — 9,947 messages
- ✍️ One partner writes **27% longer messages** on average

---

## 🛠️ Tech Stack

- **Python** — core analysis
- **Pandas** — data manipulation
- **Matplotlib & Seaborn** — visualizations
- **Streamlit** — dashboard (coming soon)

---

## 🚀 How to run it yourself

1. Export your WhatsApp chat (Settings → Chat → Export Chat → Without Media)
2. Rename the file to `chat.txt` and place it in the project folder
3. Install dependencies:
```bash
pip install pandas matplotlib seaborn
```
4. Run the analysis:
```bash
python parse_chat.py
```

---

## 🗺️ Roadmap

- [x] WhatsApp chat parser
- [x] Basic analytics (volume, peak hours, message length)
- [x] Visualizations
- [ ] Sentiment analysis
- [ ] Connection health score
- [ ] Daily mood check-in feature
- [ ] Streamlit dashboard
- [ ] Multi-couple support (startup version)

---

## 💡 The Startup Angle

**Problem:** 14M+ long-distance couples struggle to stay emotionally connected  
**Solution:** Data-driven insights that make couples more intentional about communication  
**Market:** LDR couples, relationship counselors, couples therapy apps  
**Monetization:** Premium insights, date night suggestions, gift integrations  

---

## ⚠️ Privacy Note

No real chat data is stored or uploaded in this repository.
All analysis is done locally on your own device.
Your conversations stay private. 🔒

---

*Built with love and Python 💕*
