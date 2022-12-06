import lib.CsvGenerator as gen
import lib.ColumnConfig as cc

# Our csv generator class
generator = gen.CsvGenerator()

# Set our export file name
generator.outputFile = "test.csv"

# Setup the columsn for the file to generate
generator.columns = [
    cc.ColumnConfig('string', 11, 0, 0),  # Random name
    cc.ColumnConfig('int', 0, 40, 150),   # phone
    cc.ColumnConfig('int', 0, 750, 1900),    # house
    cc.ColumnConfig('int', 0, 125, 350),    # electric
    cc.ColumnConfig('int', 0, 60, 150),    # water
    cc.ColumnConfig('int', 0, 200, 800),     # food
]

# Run the Generate method with how man rows we want created
generator.Generate(72000)