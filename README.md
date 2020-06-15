# Random-Sampling
Takes in a .csv and randomly samples based on user input.
Input:
- A .csv file
- File path of .csv

Features:
- User can specify a group by function before sampling. Enabling sampling X amount of tasks per group.
- Can sample the entire population normally.

Prompts a user must answer:

- "Would you like to sample tasks per group? y/n"
- "Which column would you like to group by?" (Columns will be listed in console)
- "How many tasks per group would you like to sample? (Sample size must be less than or equal to the number of tasks of the smallest group) " OR "How many tasks would you like to sample? "

To Do:
- Needs to handle cases when sample size is greater than the smallest group population.
    - Include all tasks when sample size is greater
    - Prompt user for action first.
