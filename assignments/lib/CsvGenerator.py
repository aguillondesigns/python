class CsvGenerator:
    outputFile = ''     # string - file name
    columns = []        # list - list of type ColumnConfig

    def Generate(this, instances):
        # Using the class params, generate a cvs
        if instances <= 0:
            exit("Nothing to do here...")
        
        f = open(this.outputFile, 'w')  # use 'w' to clear out the file each time
        count = 0
        while count < instances:
            columnsWritten = 0
            for column in this.columns:
                # each column is of type ColumnConfig
                f.write(str(column.GetValue()))
                columnsWritten += 1 
                if columnsWritten <= len(this.columns) - 1:
                    f.write(',')
            f.write('\n')   # done writing the line new line it
            count += 1      # increment our instance counter
        f.close()   # done writing our values, close our file