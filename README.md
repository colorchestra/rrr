# rrr
## the stupidest feed reader

watch out: currently only supports rss 1.0, 2.0 and atom 1.0. if you're not sure which versions your feeds are, set `versionsOnly` to `True`.

### usage
- put your feeds in the feeds file
- run rrr without arguments to build the cache
- run rrr with the numbers of the articles you want to read as arguments to open them in your browser

### to do
- stable support for various kinds of rss and atom
- ~~error handling: when `d['feed']['title']` is empty~~
- ~~monday mode: display last 72 hours on mondays (insted of default 24 hours on other weekdays)~~
- maybe: color (if not: throw out defined colors)
- ~~maybe: opml import (oof)~~
- maybe: if there's a cool way: dump articles into the terminal
- maybe: index read articles so they don't show up in the next run (when to purge those though?)
