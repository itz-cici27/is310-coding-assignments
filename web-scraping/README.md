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

The `User-agent: *` section (which applies to my scraper) disallows dynamically generated pages and tools, such as `/w/`, `/api/`, `/trap/`, and `Special:` pages, plus specific administrative pages like deletion discussions and noticeboards. Regular article pages and category pages under `/wiki/` are allowed, which is all my scraper visits. The file also notes that "friendly, low-speed bots are welcome viewing article pages" and warns that bots that go too fast may be blocked, which is why my script waits 1 second between requests. There is no `Crawl-delay` set for general bots.

Wikipedia's text is shared under a Creative Commons license, and my scraper only reads public article and category pages. To scrape responsibly, my script sends an honest `User-Agent` with my contact email, waits 1 second between requests, and skips any page that doesn't return a `200` status code.

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

## Reflection: What Did I Actually Measure?

Word counts and link counts are proxies for "attention," not attention itself. A longer page doesn't necessarily mean a group is more popular or more important. A few things could make a page longer that have nothing to do with fan interest:

- **Age:** Groups that debuted earlier have had more time to release music, win awards, and be written about.
- **Tables and lists:** K-pop articles often include large discography, awards, and filmography sections, so word counts may reflect *how many releases or awards* a group has rather than how much editors care about them. Citations at the bottom are counted too.
- **Navigation boxes:** Links at the bottom of an article often point to label-mates and related groups, which inflates link counts without saying much about the group itself.
- **Language:** This is *English* Wikipedia, so it reflects what English-speaking editors chose to document, not Korean fans or the Korean-language Wikipedia.
- **Sampling:** I took the first 40 groups alphabetically, not a random sample, so my results might not represent each category as a whole.

So someone would be wrong to conclude from my data that boy bands (or girl groups) are more popular, more successful, or more culturally important. At most, my data shows where English Wikipedia's documentation is concentrated, and answering *why* would need more evidence, like debut years, edit histories, or page view statistics.