
ColumnsWanted = 3
Unsorted = "Unsorted-Raw-List.txt"
SortedUnique = "Sorted-Raw-List.txt"
TableList = "HP_CountryCodes.html"
ReadMe = "README.md"

def make_divisible(n, int_m):
    remainder = n % int_m
    if remainder == 0:
        return n 
    return n + (int_m - remainder)

def dup_n(s,n):
    t = ""
    for i in range (n):
        t+= s
    return t;

def add_phrase_to_strings(strings, phrase):
    return [s + phrase for s in strings]

def sort_and_remove_duplicates():

    # Read the contents of the file
    with open(Unsorted, 'r') as file:
        lines = file.readlines() 

    # Filter out empty or whitespace-only lines
    non_empty_lines = [line for line in lines if line.strip()]
    
    modified_lines = ['#' + line if not '#' in line else line for line in lines]
            
    
    # Remove duplicates and sort
    #unique_lines = sorted(set(modified_lines))
    # Sort the lines based on the first four characters
    
    sorted_lines = sorted(modified_lines, key=lambda line: line[:4])
    
    # Remove duplicates
    seen = set()
    unique_lines = []
    for line in sorted_lines:
        line = line.replace(" - "," ")
        if line[:4] not in seen:
            unique_lines.append(line)
            seen.add(line[:4])
            
    NumItems = len(unique_lines)
    n = make_divisible(NumItems,ColumnsWanted)
    nRows = n // ColumnsWanted  
    
    if n != NumItems:
        d = n - NumItems
        for i in range (d):
            unique_lines.append("")        
          
    # Write the sorted, unique lines back to the file
    with open(SortedUnique, 'w') as file:
        LineOut = "This file is used by MacroViewer\r\n"
        LineOut += "Number Countries:" + str(NumItems) + "\r\n"
        LineOut += "Columns wanted:" + str(ColumnsWanted) + "\r\n"
        LineOut += "Number Rows:" + str(nRows) + "\r\n"
        LineOut += "Number slots:" + str(n) + "\r\n"
        file.writelines(LineOut);
        file.writelines(unique_lines)
    

    with open(TableList, 'w') as file:
        LineOut ="<table border='1' width='100%'>"
        for i in range (nRows):
            LineOut +="<tr>"
            for j in range (ColumnsWanted):
                aLine = "<td>" +unique_lines[i+j*nRows].replace('\n', '') + "</td>" 
                LineOut+= aLine;
            LineOut += "</tr>"
        LineOut += "</table>"
        file.writelines(LineOut)

    with open(ReadMe, 'w') as file:
        LineOut = ""
        LineOut += "# HP-Country-Codes\n## List of known country codes gathered from the Internet.\n"
        LineOut += "To update this list, add new codes to 'Unsorted-Raw-List.txt'\n\n"
        LineOut += "Then run the python program 'FormTable.py'\n\n"
        LineOut += dup_n("|",ColumnsWanted) + "|\n"
        LineOut += dup_n("| ------------- ",ColumnsWanted) + "|\n"
        for i in range (nRows):
            for j in range (ColumnsWanted):
                aLine = "|" +unique_lines[i+j*nRows].replace('\n', '')
                LineOut += aLine
            LineOut += "|\n"
        file.writelines(LineOut)


sort_and_remove_duplicates()
