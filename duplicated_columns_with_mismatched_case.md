# Handling Duplicates Due to Mismatched Column Case
## Problem:
The data in test_1.json has two brand columns: "brand" and "Brand"
When we attempt to create a dataframe, spark doesn't know what to do!
There are many ways to handle this, for example:

1. You can read the json file using spark.sql.caseSensitive = true
2. You can read the json file as text and then process it with a regular python function to rename the columns.