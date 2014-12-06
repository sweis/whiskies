Quick script to compare whisky flavors

Sample output:
$ python whisky.py lagavulin
Top 10 closest matches to Lagavulin:
	Ardbeg (3.0)
	Laphroig (3.0)
	Clynelish (6.0)
	Caol ila (8.0)
	Talisker (11.0)
	Isle of jura (16.0)
	Oban (18.0)
	Glenscotia (19.0)
	Oldpulteney (19.0)
Least closest matches to Lagavulin:
	Speyburn (49.0)
	Glenlivet (50.0)
	Glenfarclas (51.0)
	Strathisla (52.0)
	Edradour (53.0)
	Glengoyne (54.0)
	Tomintoul (56.0)
	Glenmoray (57.0)
	Aberlour (64.0)
	Auchentoshan (66.0)

usage: Find closest whisky matches [-h] [-s SOURCE] whisky

positional arguments:
  whisky                The whisky to match

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source file

Supported whiskies:
aberfeldy aberlour ancnoc ardbeg ardmore arranisleof auchentoshan auchroisk aultmore balblair balmenach belvenie bennevis benriach benrinnes benromach bladnoch blairathol bowmore bruichladdich bunnahabhain caol ila cardhu clynelish craigallechie craigganmore dailuaine dalmore dalwhinnie deanston dufftown edradour glenallachie glendeveronmacduff glendronach glendullan glenelgin glenfarclas glenfiddich glengarioch glengoyne glengrant glenkeith glenkinchie glenlivet glenlossie glenmorangie glenmoray glenord glenrothes glenscotia glenspey glenturret highland park inchgower isle of jura knochando lagavulin laphroig linkwood loch lomond longmorn macallan mannochmore miltonduff mortlach oban oldfettercairn oldpulteney royalbrackla royallochnagar scapa speyburn speyside springbank strathisla strathmill talisker tamdhu tamnavulin teaninich tobermory tomatin tomintoul tormore tullibardine

Data and much more interesting analysis from:
https://www.mathstat.strath.ac.uk/outreach/nessie/nessie_whisky.html
