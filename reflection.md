# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

It asked to guess a number from 1 to 100, and when I guessed my first number, it gave me a hint. However, I noticed when it said "Go Lower" it wasn't helping. I even submitted 1 as a guess and it still said go lower. That makes me think that the hints were backwards. Another bug I found was that the New Game button did not start a new game after winning. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code for this project.

The AI suggested I hardcode the range displayed at the top of the game to keep it dynamic based on the level being played. I verified the result by running the updated game and switching between difficulties to see if the ranges updated. 

When I was trying to figure out why I couldn't run pytest, it tried to add some sort of path code to an unknown file. I declined the edit and found that I had to use a different terminal command to get the tests to run successfully. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For each bug I fixed with Claude, I verified it worked by testing it extensively through my own use of the app, and then testing it through pytest. 

For example, I asked it to fix a bug where the new game would break the Guess button. I confirmed it was fixed by looking through the lines of code it edited and the difference between them, then testing out the Guess button myself in the context where it was breaking before.

Claude Code helped me design tests and understand what exactly they were testing by giving an explanation for each one. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are whenever a user interacts with the interface (clicking a button, typing input), Streamlit reruns the entire script from the top. Like refreshing a page anytime you change something.

Session state is a dictionary that persists across reruns. It will still be there even if the app restarts. It keeps the important values needed across reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to be able to use AI to create more and better tests than I would usually create myself. 
Next time, I would have a boilerplate code ready before prompting like we did in this exercise, I think it's useful for the AI to have some sort of context before going in and editing things instead of relying on pure generation.
I learned a lot from this project, but one thing that stood out to me was how efficient coding agents have become over the years. This is my first time using one to do something like this and it's been really cool figuring it out.