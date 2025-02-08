# learning_how_to_learn
Implementation of some concepts from Learning How To Learn with LLM help.

## What is it about?

When watching educational video, I wanted to focus on video itself and follow along rather than taking notes. However, notes are useful later too e.g. when you recall information and check yourself. So, I decided to use an LLM to handle this note-taking for me with some ideas from Learning How Lo Learn - pose questions for recall, use metaphors / analogies so that key points stay in memory longer.

## How to launch?

1. **Clone the Repository**
   
   ```sh
   git clone <repo_url>
   cd <repo_name>

2. ```sh
   pip install -r requirements.txt
3. ```sh
   ollama pull model_name
4. Create `.env` and fill with your data (example in `.env.example`). For now, the audio will be in `root_name/data/audio`, transcripts - `root_name/data/transcripts`, summary - `root_name/data/summary.md`. Specify `YOUTUBE_URL` (like playlist / single video) and other vars (like `WHISPER_MODEL`)
5. `python3 main.py`

#### What I've encountered so far:
- running relatively small models locally (around 7B parameters) gives satisfactory results for small transcripts. As trasncripts get longer, the model does not follow indicated instructions
- the result from **deepseek-r1** is quite fun to read, especially it's reasoning part (\<think>reasoning\<think>). With this model it requires more time to generate the summary and the model often gets confused following parts with calculations

### To Do
- [ ] add error handling
- [ ] try out proprietary models (e.g. recently new Gemini was released)
- [ ] play around with local LLMs more to improve result with long transcripts


## Check out 🧐
Inspired by this [Learning How To Learn lecture](https://youtu.be/QcoCYnzGwBo?si=hV_yS6-t3XOxeZKZ) given at Kyiv School of Economics (KSE) by Barbara Oakley.

Kudos to [StatQuest with Josh Starmer](https://youtube.com/@statquest?si=DFI09E5011omE3OO) for an exceptional explanations. The data example is created based on some videos from Deep Learning playlist.
