## Data Input
  Took input and validated with input_hannder such that
    1. Its a csv file
    2. a valid path was provided

## Query Options
  1. added flags via argparse
  2. flags are optional by default and if provided have type safety so validation should be good

## Output
  1. added flags via argparse
  2. flags are optional by default and if provided have type safety so validation should be good
  3. Didnt provide domain constraints e.g
    1. years (invalid years or years after current year + 1)  
    2. ratings (less than 0 or greater than 10)
    3. runtime (less than 0)


## Bonus
  1. Added output-format, output-file, export-log flags
  2. assumed that .txt are for logs so only valid output formats are for json and csv
  3. added flag for votes-min (werent in the requirements, didnt notice until I ran the examples)

Ran out of time wasnt able to do the rest of the bonus features
