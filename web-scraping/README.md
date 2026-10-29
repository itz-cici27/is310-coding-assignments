# Web Scraping: K-pop Groups on Wikipedia

## How I Chose My Wiki

I really wanted to scrape a wiki about something I'm personally into, so I started by looking for sites about webtoons, manhwas, K-pop, or music. But that turned out to be harder than I expected, as most of the fan wikis for these topics (like webtoon.fandom.com) are hosted on Fandom, which blocks automated requests with Cloudflare. Other sites I looked at, like KProfiles, aren't actually community-run wikis. I also tried IMSLP (imslp.org), a community-run sheet music library, because I used to use this website a lot back in high school (I went to an arts high school for violin!) It returned a `200`, but the list of works on its category pages is loaded with JavaScript, so BeautifulSoup found zero links in the HTML.

Next, I tried Bulbapedia (bulbapedia.bulbagarden.net), since a lot of my friends are really into Pokémon and I was curious to learn more about it. My plan was to compare Generation I and Generation IX Pokémon pages, but both category pages returned **HTTP 403**. Following the course guidance, I switched sites instead of trying to get around the block.

In the end, I settled on **English Wikipedia**. It's a community-run wiki built on MediaWiki (the same software as Tolkien Gateway), and it let me go back to my original interest: K-pop!

## My Question

**How does English Wikipedia distribute attention between South Korean girl groups and South Korean boy bands?**

I scraped two category pages:
- [Category:South Korean girl groups](https://en.wikipedia.org/wiki/Category:South_Korean_girl_groups)
- [Category:South Korean boy bands](https://en.wikipedia.org/wiki/Category:South_Korean_boy_bands)

For the first 40 groups listed in each category, I visited each group's article and measured:
- `word_count`: number of words in the article
- `character_count`: number of characters (including spaces and punctuation)
- `internal_link_count`: every link to another Wikipedia page
- `unique_internal_link_count`: the number of *different* Wikipedia pages linked

## Why This Might Interest Researchers

K-pop is one of South Korea's biggest cultural exports, and Wikipedia is often the first place international fans go to learn about a group. Comparing how much documentation girl groups and boy bands get could be a starting point for researchers studying gender in fandom, how online communities decide what's worth documenting, or how K-pop is represented to English-speaking audiences.

## robots.txt and Policies

Wikipedia's robots.txt: https://en.wikipedia.org/robots.txt

The file was way longer than I expected, but most of it is rules for specific bots that have caused problems in the past, like ones that copy entire sites or send requests way too fast. The part that applies to my scraper is the `User-agent: *` section. It blocks things like `/w/`, `/api/`, and `Special:` pages, plus a bunch of admin pages like deletion discussions and noticeboards. Regular article pages and category pages under `/wiki/` are allowed, and those are the only pages my scraper visits. I liked that one of the comments says "friendly, low-speed bots are welcome viewing article pages," and it also warns that bots going too fast might get blocked. There's no `Crawl-delay` for general bots, but I still added a 1 second pause between requests to be safe.

Wikipedia's text is shared under a Creative Commons license, so it's meant to be reused as long as it's credited. To be a respectful scraper, my script sends an honest `User-Agent` with my school email so Wikipedia knows who I am, waits between requests, and skips any page that doesn't return a `200` status code.

## How to Run

```python
python wiki_scraping.py
```

This creates `wikipedia_kpop_groups.csv` in the `web-scraping` folder, with one row per group.

## Results

I analyzed 40 girl groups and 40 boy bands (the first 40 alphabetically in each category, excluding the "List of..." pages).

| Measure | Girl groups (average / median) | Boy bands (average / median) |
|---|---|---|
| Words | 5,157 / 2,220 | 3,814 / 2,042 |
| Characters | 28,354 / 11,915 | 20,787 / 11,141 |
| All internal links | 408 / 95 | 226 / 87 |
| Unique internal links | 199 / 64 | 118 / 72 |

On average, girl group pages were longer and had more links. But the medians tell a different story: the typical page is about the same length in both categories, and boy band pages actually had slightly more unique links. The averages are pulled up by a few very long pages, like Blackpink (32,877 words), 2NE1, Aespa, and Apink. So the difference seems to come from a handful of very famous groups, not from girl groups getting more attention overall.

## Reflection

Honestly, I went into this thinking word count would be a pretty good way to measure "attention," but the more I looked at my data, the less sure I was! A longer Wikipedia page doesn't automatically mean a group is more popular. Older groups like 2NE1 or 4Minute have just had more years to release music, win awards, and get written about. K-pop pages also tend to have huge discography and awards tables, so a lot of those words are really just lists of songs and trophies. Even the links can be misleading, since the navigation boxes at the bottom of each page link to a bunch of other groups from the same company, which bumps up the count without saying much about the group itself.

The part that surprised me the most was the difference between averages and medians. If I only looked at the averages, I'd say girl groups get way more attention on Wikipedia. But the medians are almost the same, and boy bands actually had slightly more unique links! It turns out a few really famous groups like Blackpink and Aespa were pulling the girl group average way up. I also learned something from a bug: my first run said every single page had zero links, because Wikipedia formatted its links differently than I expected. If I hadn't noticed, I would have saved a whole column of wrong data without realizing it.

So someone would be wrong to look at my results and say girl groups (or boy bands) are more popular or more important. My data only covers the first 40 groups alphabetically, it only reflects what English-speaking Wikipedia editors chose to write about, and page length depends on a lot of things besides fan interest. To actually make a claim about attention, I'd want to look at things like debut years, edit histories, or page view statistics too.
