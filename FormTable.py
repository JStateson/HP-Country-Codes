
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
    StartIndex = [0] * ColumnsWanted 


    # Read the contents of the file
    with open(Unsorted, 'r') as file:
        lines = file.readlines() 

    # Filter out empty or whitespace-only lines
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Remove duplicates and sort
    unique_lines = sorted(set(non_empty_lines))
    
    NumItems = len(unique_lines)
    n = make_divisible(NumItems,ColumnsWanted)
    for i in range (ColumnsWanted):
        StartIndex[i] = i * n   

    if n != NumItems:
        d = n - NumItems
        for i in range (d):
            unique_lines.append("")
            
    # Write the sorted, unique lines back to the file
    with open(SortedUnique, 'w') as file:
        file.writelines("This file is not used\r\nNumber slots:" + str(n) + "\r\n")
        file.writelines(unique_lines)
    nRows = n // ColumnsWanted    

    with open(TableList, 'w') as file:
        file.writelines("<table border='1' width='100%'>")
        for i in range (nRows):
            LineOut ="<tr>"
            for j in range (ColumnsWanted):
                aLine = "<td>" +unique_lines[i+j*nRows].replace('\n', '') + "</td>" 
                LineOut+= aLine;
            LineOut += "</tr>"
            file.writelines(LineOut)
        file.writelines("</table>")


    with open(ReadMe, 'w') as file:
        file.writelines("# HP-Country-Codes\n## List of known country codes gathered from the Internet.\n")
        file.writelines("To update this list, add new codes to 'Unsorted-Raw-List.txt'\n\n")
        file.writelines("Then run the python program 'FormTable.py'\n\n")
        file.writelines(dup_n("|",ColumnsWanted) + "|\n")
        file.writelines(dup_n("| ------------- ",ColumnsWanted) + "|\n")
        for i in range (nRows):
            LineOut = ""
            for j in range (ColumnsWanted):
                aLine = "|" +unique_lines[i+j*nRows].replace('\n', '')
                LineOut += aLine
            LineOut += "|\n"
            file.writelines(LineOut)


sort_and_remove_duplicates()
