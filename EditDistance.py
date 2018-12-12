class Edit:
# Calculates edit distance, creates command file based on minimum edit distance (i.e., the minimum number of edit operations) for
# transforming string 1 to string 2, where the edit operations are add, delete and update.

    # I used this as a source:
    # https://www.geeksforgeeks.org/print-all-possible-ways-to-convert-one-string-into-another-string-edit-distance/
    def edit_distance(self, s1, s2):
        # Calculates the minimum number of edits to transform s1 to s2, where the options are add, delete and update
        # (each counts as one edit).

        m = len(s1)
        n = len(s2)

        # Initialize the table for this DP algorithm (a list of m n-element lists).
        # The algorithm is O(nm).
        self.table = [[0 for x in range(n+1)] for x in range(m+1)] 

        # We compare the two strings s1 and s2 from the right to left.
        # i and j == the number of elements we're considering in s1 and s2.
        for i in range(m+1): 
            for j in range(n+1): 
                # The first string is empty, so inserting all of the second string is the only option; it takes j operations.
                if i == 0: 
                    self.table[i][j] = j

                # The second string is empty, so removing all of the first string is the only option; it takes i operations.
                elif j == 0: 
                    self.table[i][j] = i
  
                # If the last characters of s1 and s2 are equal, the edit distance
                # is just the edit distance for s1 and s2 with their last characters removed.
                elif s1[i-1] == s2[j-1]: 
                    self.table[i][j] = self.table[i-1][j-1]
  
                else: 
                    # The edit distances of s1 and s2 after inserting, removing or replacing the last character of s1 
                    # is 1 plus the answer to the corresponding edit-distance subproblem.
                    self.table[i][j] = 1 + min(self.table[i][j-1],   # Inserting
                                               self.table[i-1][j],   # Removing
                                               self.table[i-1][j-1]) # Replacing

        return self.table[m][n] 

    def list_of_edit_operations(self, s1, s2):
        i = len(s1)
        j = len(s2)

        self.edit_distance(s1, s2)

        lst = []

        while i != 0 and j != 0:
            if s1[i-1] == s2[j-1]:
                i -= 1
                j -= 1
            elif self.table[i][j] == self.table[i-1][j-1] + 1:
                lst.append("Update " + str(i-1) + " to " + str(s2[j-1]))
                i -= 1
                j -= 1
            elif self.table[i][j] == self.table[i-1][j] + 1:
                lst.append("Delete " + str(i-1))
                i -= 1
            elif self.table[i][j] == self.table[i][j-1] + 1:
                lst.append("Add " + str(s2[j-1]) + " to " + str(i))
                j -= 1

        if i < j: # if s2 is larger
            for elt in s2[j-i-1::-1]: # the leftover elts of s2 are simply added to s1 in the beginning
                lst.append("Add " + elt + " to 0")
        elif i > j: # if s1 is larger
            for idx in range(i-j-1, -1, -1):
                lst.append("Delete " + str(idx))

        return lst

    def restore_file(self, list_of_edit_ops, list_of_lines):
     #   with open(file_name, "r") as f:
     #       list_of_lines = f.readlines()

        x = len(list_of_edit_ops) - 1 # edit ops are in reverse order, so we'll process them from back to front
        shift = 0 # when we add or delete elements, the line numbers shift; this variable is added to offset the change

        while x >= 0:
            op = list_of_edit_ops[x]

            if op[0] == "Add":
                content = op[4:op.rfind(' ')-3] + "\n" # e.g., "Add <something> to k" -> <something>
                list_of_lines.insert(int(op[-1]) + shift, content)
                shift += 1
            elif op[0] == "Delete": # op = "Delete k"
                del list_of_lines[int(op[1]) + shift]
                shift -= 1
            elif op[0] == "Update": # op = "Update k to <xyz>"
                content = op[op.index(' ', (op.index(' ', (op.index(' ')+1))+1))+1:] + "\n" # content <xyz> starts at the index just after the 3rd space
                list_of_lines[int(op[1]) + shift] = content
            x -= 1

        return list_of_lines


#editdist = EditDistance()
#ops = editdist.list_of_edit_operations(file1, file2)


#with open('file3.txt', 'w') as f:
#    for item in restore_file(ops, "file1.txt"):
#        f.write("%s" % item)

#with open("file1.txt", "r") as f, open("file2.txt", "r") as g:
#    file1 = f.read()
#    file2 = g.read()

#file1 = file1.split('\n')
#file2 = file2.split('\n')

##editdist = Edit()
#ops = editdist.list_of_edit_operations(file1, file2)
#editdist.restore_file(ops, "file3.txt")

