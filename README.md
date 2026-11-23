# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/framicks/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/framicks/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Monday, 23 November 2026, packed into a single broadsheet page. The front page leads with the COP31 climate summit in Türkiye falling apart, after the EU and other delegations turned down a closing draft that left out any fossil-fuel phase-out. The rest of the page carries five more stories from the same day: the Houthis saying they hit a Saudi oil refinery, the Democrats locking in a 258-seat majority in the US House, Mexican forces capturing the FBI most-wanted cartel figure known as "El Chapo Isidro", South Korea's education minister stepping down amid an AI exam-cheating scandal, and Liverpool beating Manchester United 4-0 in Mauricio Pochettino's first match in charge. Six stories, one crowded news day, set out as a classic newspaper front page in `front-page.png`.

## Stories

1. COP31 talks collapse
2. Houthis claim strikes on Saudi refinery
3. Democrats seal 258-seat House majority
4. Mexico captures "El Chapo Isidro"
5. Seoul minister quits over AI exam scandal
6. Liverpool rout United 4-0

## Run it

```sh
python3 main.py
```

This copies `front-page.png` (a real PNG, 1024×1024, under 1 MiB) to `/output/entry.png`. Set `MAKEFUN_OUTPUT_DIR` to pick a different destination. Running it twice produces byte-identical output, since the image is shipped in the repository and only copied, never redrawn.

## Verification

You can check the output yourself in a minute. Run `python3 main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two different folders, then compare the two `entry.png` files with `sha256sum` — both hashes should match each other and the shipped `front-page.png`, since the script only copies the image and never redraws it. The PNG itself should stay 1024×1024 pixels and under 1 MiB, which you can confirm with `file` or `identify`. If either run prints an error instead, the source image is missing or its first eight bytes are not a PNG signature, and the script exits with code 1.

## Sources

Headlines were checked against reporting dated 23 November 2026: The Hindu on the COP31 collapse, the Indian Express on the Houthi claim, the Associated Press and Reuters on the Democrats' 258th House seat, Mexican and wire reporting on the capture of Fausto Isidro Meza Flores in Sinaloa, Korean and wire reporting on the education minister's resignation, and Reuters on Liverpool's 4-0 win at Anfield. Claims are worded as claims where only one side has spoken.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jjs4n5n8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
