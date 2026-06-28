# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

     Finding the best rated study spots can be difficult when the information is spread all over and no one knows if it is reliable or not. Official channels often are promoting a certain brand or company and these can be overcrowded and just no enjoyable for some students. Having one place where students can find study spots leaves more time for the actual studying. This project should combine popular study areas like coffee shops, cafes, libraries, classroom buildings, etc. and introduce users to more niche and under the ground spots.This project should also be honest and give appropriate feedback on each place according to the sources. As a student, I get sick of the same, busy places that I would love to find more intimate spots that are different than my dorm or the nearby Starbucks.
---
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

https://sweetwatergainesville.com/resources/best-study-spots-uf/ 
https://www.swamprentals.com/help-finding-apartments/gainesville-study-spots-near-campus
https://gatorrentals.com/blog/best-study-spots-on-campus/
https://www.staygainesville.com/uf-campus-insider-tips-best-study-spots-hidden-gems
https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/
https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/
https://www.hercampus.com/school/ufl/gainesville-bucket-list/
https://www.reddit.com/r/ufl/comments/oqbhhq/best_unknown_study_spots_on_campus/
https://www.reddit.com/r/ufl/comments/16tqs1w/whats_your_favorite_place_to_study/
https://www.reddit.com/r/ufl/comments/j0yaz0/pretty_outdoor_study_spots_around_gainesville/
https://www.reddit.com/r/ufl/comments/xnrfer/what_are_some_good_coffee_shopsplaces_to_study_
https://ufl.pb.unizin.org/ulaguide/chapter/library-west/
https://spoonuniversity.com/school/ufl/a-peek-inside-coterie-market/
https://www.theodysseyonline.com/review-uf-campus-libraries
https://carlymccullough.com/2018/03/13/stress-free-study-spots-on-uf-campus/

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 350 tokens - fits because I am able to grab enough information to answer each of the questions, while still providing a summarized response.

**Overlap:** k = 4 - this overlap works because I am able to get the gist of each question's answer without missing relevant information.

I did a lot of preprocessing and copy and pasted all of the text I wanted to use for this project.

**Final chunk count:** 52

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
## Sample Chunks

**Chunk 1** — Source: `sweetwater_study_spots.txt`
Being a top five public university, students at UF study a lot, so knowing your study spot options is important...Library W...

**Chunk 2** — Source: `staygainesville_study_spots.txt`
served weekdays. It's tradition, community, and convenience all rolled into one. Century Tower One of UF's most recognizable landmarks...

**Chunk 3** — Source: `collegemagazine_coffee_shops.txt`
homemade waffles pair perfectly with a hot vanilla latte. When driving down South Main St., stay on the lookout for Halo Potato Donuts...

**Chunk 4** — Source: `uflpb_libwest_review.txt`
floor mostly consists of administrative offices and solo seating scattered throughout the floor. You'll also find small, locked cubicles reserved for graduate students...

**Chunk 5** — Source: `carlymccullough.txt`
productive. It's nearly impossible not to feel inspired when immersed in the workings of Weimer Hall...
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**  all-MiniLM-L6-v2

**Production tradeoff reflection:** 
I would use this model again if I was doing a project on a similar size. Next time, I would love to use a model that supports multiple languages and can put from even more sources. I also want to find a way to get AI to scrape and find these websites for me.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:** What coffee shops do UF students recommend for studying?

Top returned chunks:
- Being a top five public university, students at UF study a lot, so knowing your study spot options is important in being ableto get all of your work done and getting good grades in your classes.Luckily, UF students have many options when it comes to where they want to study and meet for group proj...
- Reitz hungry. Marston’s Starbucks is always pretty busy and always takes a little longer for your order to come up, but beingso close to Marston is a perk. Also, it has the widest range of hours, closing at midnight on weekends. Perfect place to stop before a latenight study, but I would try to av...
- Study at the Ben Hill Griffin Stadium Studying at the stadium is probably one of my favorite activities on campus. Although being in BHG on a game day is definitely an experience, the serenity ofan empty stadium (particularly on a day with nice weather) is unbeatable. Try Maude’s Cafe’s coffee pitc...

Relevance explanation:
Results are partially relevant. Chunk 2 directly addresses the query — it mentions Marston's Starbucks hours, studyability, and proximity to the library, which is useful context for a coffee shop recommendation. Chunk 3 mentions Maude's Cafe as a coffee option at Ben Hill Griffin Stadium. Chunk 1 is a general introduction to UF study spots and is the weakest match. It doesn't mention coffee shops specifically. 

---

**Query 2:** Is Pascal's Coffeehouse open late enough for a night study session?

Top returned chunks:
- Coffeehouse Hours: 8am – 5pm weekdays, 8am – 3pm Sat., closed Sun. Vibes: Comfy cozy study session Studyability: 7/10, just alittle bit noisier, but nothing some earbuds can’t fix! With a cabin-like interior, functioning fireplace, custom tile, and a sunny balcony, Pascal’s offered the homiest aest...
- Home to student study groups and warm cups of coffee, Pascal’s Coffeehouse sits nestled in the backroads of Gainesville’s midtown. If you ever get stuck in a Gainesville summer storm or sweating from the raging humidity, duck for cover in this coffee shop. While there, you might as well stick around...
- drinks absolutely hold up. Karma Cream Hours: 8am – 8pm weekdays, 8am – 10pm Fri., 10am-10pm Sat., 10am-4pm Sun. Vibes: Lunchand some quick review Studyability: 6/10 (depending on how you study with some extra background noise) Because it is entirely vegan, Karma Cream offers alternative milk selec...

Relevance explanation: Results are highly relevant. Chunk 1 directly answers the query (it contains Pascal's exact hours 8am–5pm weekdays, 8am–3pm Saturday, closed Sunday), confirming it is not open late enough for a night study session. Chunk 2 provides additional context about Pascal's atmosphere and location. Chunk 3 is a weaker match (it covers Karma Cream's hours rather than Pascal's) but is still topically related as it covers coffee shop hours for studying.

---

**Query 3:** What do students say about studying outdoors at UF?

Top returned chunks:
- study, which makes it one of the only spaces on campus you can step into silence. Sometimes, the noise is good. It’s what gives this university color and life, but sometimes the kindest thing you can do for yourself is take a break. If you need a minute to let your mind think about other things, tak...
- campus that you can use the UF WiFi, and there is plenty of street parking for students who prefer to drive rather than walk. The Education Library, also known as Norman, is a popular study spot for students in sororities because it is located in close proximity to Sorority Row. Norman is typically ...
- Being a top five public university, students at UF study a lot, so knowing your study spot options is important in being able to get all of your work done and getting good grades in your classes. Luckily, UF students have many options when it comes to where they want to study and meet for group proj...

Relevance explanation: 
Results are loosely relevant. Chunk 1 discusses the need for silence and mental breaks on campus, which is adjacent to outdoor studying but doesn't explicitly mention it. Chunks 2 and 3 are general study spot overviews that don't specifically address outdoor spaces. The retrieval returned the closest semantic matches it could find. Adding a source specifically about Plaza of the Americas or other outdoor spots would improve retrieval on this query.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
Answer the question using ONLY the information provided in the context documents below. Do NOT use any outside knowledge or make assumptions beyond what is written in the documents. If the documents do not contain enough information to answer the question, respond with exactly: "I don't have enough information on that in my sources."

**How source attribution is surfaced in the response:**
There is a section at the end that says "Source:" and lists at least three sources referenced by the LLM.
---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query: Is Pascal's Coffeehouse open late enough for a night study session?

Response: According to Document 1, Pascal's Coffeehouse is open from 8am – 5pm weekdays, which suggests it may not be open late enough for a night study session. Additionally, Document 2 does not mention the hours of operation for Pascal's Coffeehouse, but it does describe it as a cozy study environment. Document 3 and Document 4 also do not provide information on the evening hours of Pascal's Coffeehouse. Based on the available information, it appears that Pascal's Coffeehouse is not open late enough for a night study session, as it closes at 5pm on weekdays. (Document 1)

Source attribution:
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/
  - https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/

---

**Grounded response 2**

Query: What coffee shops do UF students recommend for studying?

Response: According to Document 1, Opus Coffee is a great study spot option for students who prefer to work at a coffee shop with the perfect amount of background noise. Additionally, Document 2 recommends the Starbucks locations on campus, specifically the ones at Library West and the Reitz Student Union, as well as Marston's Starbucks, for their convenient locations and wide range of hours. Document 3 also mentions trying coffee at Maude's Cafe. Furthermore, Document 4 suggests Foxtail as a great place for a relaxing break between errands or as a more isolated evening study spot, and also reviews the on-campus Starbucks locations. (Documents 1, 2, 3, 4)

Source attribution:
  - https://sweetwatergainesville.com/resources/best-study-spots-uf/
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.hercampus.com/school/ufl/gainesville-bucket-list/
---

**Out-of-scope query**

Query: What is the best dining hall at UF?

System response (refusal): I don't have enough information on that in my sources.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:** Your query interface takes a single text input; a free-form question typed at the "Your question:" prompt in the CLI.

**Output format:** The system prints two sections after each query:
1. Answer: a grounded response generated by llama-3.3-70b-versatile via Groq, citing which document(s) the answer came from
2. Sources: a list of the URLs of the top-4 retrieved chunks that were passed as context

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:**  Is Pascal's Coffeehouse open late enough for a night study session?

> **System:** 
Answer:
According to Document 1, Pascal's Coffeehouse is open from 8am – 5pm weekdays, which suggests it may not be open late enough for a night study session. Additionally, Document 2 does not mention the hours of operation for Pascal's Coffeehouse, but it does describe it as a great place to study. Document 3 and Document 4 also do not provide information on the hours of operation for night study sessions. Based on the information provided in Document 1, it appears that Pascal's Coffeehouse may not be the best option for a night study session due to its limited hours.

Sources:
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/
  - https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

Question 1: 
What coffee shops do UF students recommend for studying?
Expected Answer: 
Everyone loves Opus and Pascal's. They are very close to campus and they are always packed. Opus has a location on campus and one close to campus.
Answer 1: 
According to Document 1, Opus Coffee is a great study spot option for students who prefer a coffee shop with the perfect amount of background noise. Additionally, Document 2 recommends the Starbucks locations on campus, specifically the ones at Library West and the Reitz Student Union, as well as Marston's Starbucks, for their convenient locations and hours. Document 3 also mentions trying coffee at Maude's Cafe, and Document 4 suggests Foxtail as a great place for a relaxing break or an isolated evening study spot. Therefore, the recommended coffee shops for studying are Opus Coffee, Starbucks (at Library West, Reitz Student Union, and Marston), Maude's Cafe, and Foxtail (Document 1, Document 2, Document 3, Document 4).
Sources: 
  - https://sweetwatergainesville.com/resources/best-study-spots-uf/
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.hercampus.com/school/ufl/gainesville-bucket-list/
Retrieval Quality: Relevant
Response Accuracy: Accurate



Question 2:
Is Pascal's Coffeehouse open late enough for a night study session?
Expected Answer:
No — Pascal's closes at 5pm weekdays and 3pm Saturday, so it's not a good late-night option despite its great atmosphere.
Answer 2:
According to Document 1, Pascal's Coffeehouse is open from 8am – 5pm weekdays, which suggests it may not be open late enough for a night study session. Additionally, Document 2 does not mention the hours of operation for Pascal's Coffeehouse, but it does describe it as a great place to study. Document 3 and Document 4 also do not provide information on the hours of operation for night study sessions. Based on the available information, it appears that Pascal's Coffeehouse may not be open late enough for a night study session. (Source: Document 1)
Sources:
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/
  - https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/
Retrieval Quality: Relevant
Response Accuracy: Accurate



Question 3:
What do students say about noise levels at Library West during finals week?
Expected Answer:
Students love it, especially when the weather is nice. Plaza of the Americas is great for studying and spending time with friends. You won't see a lot of it during the winter months.
Answer 3:
According to Document 3, during finals week, Library West hosts various events, but it does not specifically mention the noise levels. However, Document 3 does mention that "On the loud floors, you’ll find students chatting and hanging out between classes over coffee. On the quiet floors, you’ll find people really focusing to get work done." This implies that Library West has both loud and quiet areas, but it does not provide information specific to finals week. Additionally, Document 2 mentions that Library West is "the most popular library on campus, especially for undergrads" and that "You’ll find group study rooms, quiet floors, and plenty of computers," but it also does not provide information about noise levels during finals week.
Sources:
  - https://www.reddit.com/r/ufl/comments/oqbhhq/best_unknown_study_spots_on_campus/
  - https://www.staygainesville.com/uf-campus-insider-tips-best-study-spots-hidden-gems
  - https://ufl.pb.unizin.org/ulaguide/chapter/library-west/
Retrieval Quality: Off-Target
Response Quality: Partially Accurate



Question 4:
Do students recommend Opus Coffee at the Norman Hall location over other Opus locations?
Expected Answer:
Yes because it's on the quieter outer edge of campus and is near sorority row, for those involved in Greek life.
Answer 4:
According to Document 1, the author personally favors the Opus location in Norman Hall, stating it's their "personal favorite, as you’re able to study in the library as well. It’s also on the outer edge of campus, which tends to make it a little more peaceful than going to Marston or Library West." This suggests that the author recommends the Norman Hall location over other Opus locations due to its peaceful atmosphere and convenience of being able to study in the library.
Sources:
  - https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
  - https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/
  - https://www.swamprentals.com/help-finding-apartments/gainesville-study-spots-near-campus
Retrieval Quality: Partially Relevant
Response Quality: Partially Accurate



Question 5: What are the downsides students mention about studying at Plaza of the Americas?
Expected Answer:
It's weather-dependent. Great in cooler months, but gets extremely hot in Florida summer, making it uncomfortable for outdoor studying.
Answer 5:
According to Document 3, one downside of studying at Plaza of the Americas is that there is no WiFi available. Additionally, Document 2 mentions that the weather in Florida can be unpredictable, which may be a downside to studying outdoors at Plaza of the Americas, as students may need to seek shelter if it starts to rain.
Sources:
  - https://carlymccullough.com/2018/03/13/stress-free-study-spots-on-uf-campus/
  - https://sweetwatergainesville.com/resources/best-study-spots-uf/
  - https://www.reddit.com/r/ufl/comments/j0yaz0/pretty_outdoor_study_spots_around_gainesville/
  - https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/
Retrieval Quality: Partially Relevant
Response Quality: Partially Accurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**


Question 3 failed because none of the source documents specifically discuss Library West during finals week. The retrieval returned chunks about Library West generally, but the generation had no specific evidence to draw from and either gave a vague answer or said it didn't have enough information. This is a coverage failure. The domain was covered but the specific aspect of the query was not represented in any document.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec helped me with remembering my test questions, example responses, and keep track of my multiple sources. 

**One way your implementation diverged from the spec, and why:**
I ended up changing the questions based on the information readily available. It was easier to change the question rather than search the internet for one specific answer. The program and LLM still works the same way.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*


I gave Claude my chunking strategy section and asked it to implement ingest.py. It produced a script using tiktoken which failed in my environment, so I directed it to switch to a word-count approximation instead.

I gave Claude my pipeline diagram and asked it to implement query.py with a grounding system prompt. I reviewed the system prompt it generated and added the explicit 'say I don't have enough information' instruction myself.