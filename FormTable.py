from telnetlib import theNULL


Unsorted = "Unsorted-Raw-List.txt"
SortedUnique = "Sorted-Raw-List.txt"
TableList = "HP_CountryCodes.html"
ReadMe = "README.md"

def round_to_even(n):
    return n if n % 2 == 0 else n + 1 if n % 2 != 0 else n - 1

def add_phrase_to_strings(strings, phrase):
    return [s + phrase for s in strings]

def sort_and_remove_duplicates():
    # Read the contents of the file
    with open(Unsorted, 'r') as file:
        lines = file.readlines() 

    # Filter out empty or whitespace-only lines
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Remove duplicates and sort
    unique_lines = sorted(set(non_empty_lines))
    
    NumItems = len(unique_lines)
    n = round_to_even(NumItems)
    if n != NumItems:
        unique_lines.append("")
    # Write the sorted, unique lines back to the file
    with open(SortedUnique, 'w') as file:
        file.writelines("This file is not used\r\nNumber slots:" + str(n) + "\r\n")
        file.writelines(unique_lines)
    nRows = n >> 1
    j = nRows
    with open(TableList, 'w') as file:
        file.writelines("<table border='1' width='50%'>")
        for i in range (nRows):
            LineOut = "<tr><td>" +unique_lines[i].replace('\n', '') + "</td><td>" + unique_lines[j].replace('\n', '') + "</td></tr>"
            j+= 1;
            file.writelines(LineOut)
        file.writelines("</table>")

    j = nRows
    with open(ReadMe, 'w') as file:
        file.writelines("# HP-Country-Codes\n## List of known country codes gathered from Internet.\n")
        file.writelines("To update this list, add new codes to 'Unsorted-Raw-List.txt'\n")
        file.writelines("Then run the python program 'FormTable.py'\n\n")
        file.writelines("|||\n")
        file.writelines("| ------------- |:-------------:|\n")
        for i in range (nRows):
            LineOut = "|" +unique_lines[i].replace('\n', '') + "|" + unique_lines[j].replace('\n', '') + "|\n"
            j+= 1;
            file.writelines(LineOut)


sort_and_remove_duplicates()
