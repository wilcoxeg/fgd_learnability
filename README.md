
# Learnability of Syntactic Structures: Filler--Gap Dependency

• `/data/`

--- • `combined_results.csv` contains the results of all the test suites for GRNN, JRNN, GPT2 and 5-Gram models.

--- • `/test_suites/` contains all the test items in `.csv` format. Files are are organized in the following way: `item | condition | region 1 | ... |region n|`.

--- --- • `test_sents.txt` contains all of the items, one item per row, which can be fed into a neural language model.

--- --- • `test_items.txt` contains one token per row, harmonized with region and test item information.

• `/scripts/` 

--- • `analysis.Rmd` reads in `combined_results.csv` and produces plots plus statistical analysis. N.B.: Right now it only does `basic` and `unboundedness`.

Currently, the `analysis.Rmd` script reads in a `.csv` file that was compiled elsewhere. I plan on adding the by-model results and a script that combines them shortly, at which point the whole pipeline should be reproducable from this repo.

--- • `template_to_csv.py` takes in the template test suite files from `data/test_suites` and produces the `test_sents.txt` and `test_items.txt` files.

• `/images/` contains paper figures, both bar-charts of model behavior in critical regions and region-by-region plots of model behavior across the whole sentence (`*region.png`)

### To-Do List:

• GPT2 seems to be diverging between the +/- gap positions *before* the gap. This could be something wrong with the way regions are getting labled in my gpt-2 code, so need to check this!

• Currently, we're not taking the surprisal of periods or end-of-sentence punctuation.

• Check start of sentence tokens for the various models

• Add in custom x-axis and y-axis labels for the region-by-region plotting script

• Add raw-surprisal plotting script and run on the `basic` test, to illustrate how the wh-effects work in the paper.

• By-model results + combining script.
