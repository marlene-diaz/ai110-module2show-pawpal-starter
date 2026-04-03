# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
Initial Design: 
 - add a pet profile (name, age , type)
 - add/Schedule action to respective pet (walking , grooming, bathing, feeding ... etc)
 - Display Daily schedule (perhaps weekly schedule as well)

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, I couldn't make it as complex as I wanted to and had to only add in the basic features of the application.
for example, I could format horizontally instead of just vertically up and down the information.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

some contraints that the scheduler should consider is overlapping and priority. (we should feed the animals as priority)
I considered the overlapping/overscheduling would matter the most because we can't lie to owners or animals on who would get a certain task down. This is inefficient because if overbooked then almost nothing would get done.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

I couldn't implement thee overlapping feature due to time however I made sure the timing sorting feature had to be placed for display. (at least bookers would notice the times already taken)

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI for organization. I didn't where to start and the right syntax, I told it to give me a step by step to keep me on track and to be productive. The best prompts were "explain this to me.." and "how do I do xyz on VS code.." as I got to learn new content and would be able to be more efficient next time.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I would describe the moment when I ignored a certain git syntax and instead went on my own to figure out the problem. I tried to run a certain test and it wouldn't let me and AI would tell me to install things and delete certain things however I felt like this was doing too much for a simple runnning problem. I started brainstorming and I realized I never pushed certain code into the project and therefore couldn't run the testing code on the terminal. It was such an easy fix and AI couldn't do that.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

 I tested a test completed and assigning tasks to certain pets. This is important because we want clearly assign things to their respective pet and make sure they are not priortized if the task was already completed.  We don't want that in our system.


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I would say for the bare minimum it works however I would want it to be more complex than simple. If i had more time I would test same name assignment or canceling a task to a certain pet but with the same owner. perhaps even alter owner name , in case ownership changes.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The most satificying part of the project was making it into simple steps to be organized to the fullest. I got to do things step by step with my own pace while learning the concepts as well.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

i would improve the overlapping booking of events. I would like it to not book things on certain times. Maybe add working hours!

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

AI doesn't know your computer fully, it doesn't understand what you have downloaded. Take the troubleshooting into your own hands because sometimes the answer is more simplier than AI makes it.