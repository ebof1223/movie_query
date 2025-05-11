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
