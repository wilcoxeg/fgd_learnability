
# Learnability of Syntactic Structures: Filler--Gap Dependency

• `/data/`

--- • `combined_results.csv` contains the results of all the test suites for GRNN, JRNN, GPT2 and 5-Gram models.

--- • `/test_suites/` contains all the test items in `.csv` format. Files are are organized in the following way: `item | condition | region 1 | ... |region n|`.

--- --- • `test_sents.txt` contains all of the items, one item per row, which can be fed into a neural language model.

--- --- • `test_items.txt` contains one token per row, harmonized with region and test item information.

• `/scripts/` 

--- • `analysis.Rmd` reads in `combined_results.csv` and produces plots plus statistical analysis. N.B.: Right now it only does `basic` and `unboundedness`.

--- • `template_to_csv.py` takes in the template test suite files from `data/test_suites` and produces the `test_sents.txt` and `test_items.txt` files.

• `/images/` contains paper figures, both bar-charts of model behavior in critical regions and region-by-region plots of model behavior across the whole sentence (`*region.png`)
