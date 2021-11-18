from misc import smallest, larger

# alignment table defined through a class 
class Align_Table:
	# constructs the base table
	# ===============================
	# str1 is the horizontal word length
	# str2 is the vertical word length	
	def __init__(self, str1, str2):
		table = []
		x = len(str1)
		y = len(str2)
		for c in range(0, y + 2):
			row = []
			for r in range(0, x + 2):
				row.append(None)
			table.append(row)
		
		# first row (horizontal word)
		for i in range(2, x + 2):
			table[0][i] = str1[i - 2]
			
		# first column (vertical word)
		for i in range(2, y + 2):
			table[i][0] = str2[i - 2]
		
		# second row are the numbers
		for i in range(1, x + 2):
			table[1][i] = i - 1
			
		# second column are also the numbers
		for i in range(1, y + 2):
			table[i][1] = i - 1
		
		#  ==================================
		# start the alignment
		end = False
		row = 2
		column = 2
		while not end:
			current_row_value = table[0][column]
			current_column_value = table[row][0]
			current_node = None
			
			# set value of the current node we are on 
			if current_row_value == current_column_value:
				# set to previous diagonal
				current_node = table[row - 1][column - 1]
			else:
				# set to minimum of the 3 (prev diagonal, left, and top) + 1
				prev_diagonal = table[row - 1][column - 1]
				left = table[row][column - 1]
				top = table[row - 1][column]
				current_node = smallest([prev_diagonal, left, top]) + 1
			table[row][column] = current_node
			
			# test for end of row
			try:
				# if there is more to the row, then continue
				test_next_in_row = table[row][column + 1]
				column += 1
			except:
				try:
					# test if there are more rows, and if so then reset to next row
					test_next_row = table[row + 1][column]
					column = 2
					row += 1
				except:
					# no more nodes to visit, so end
					end = True
		
		self.table = table
		self.string1 = str1
		self.string2 = str2
		
	def display(self):
		# display the matrix
		# =======================
		display_str = "The matrix: \n"
		for r in self.table:
			for c in r:
				display_str += "   "
				if c == None:
					display_str += " "
				else:
					display_str += str(c)
			display_str += "\n"	
		print(display_str)
		
		# display the edit distance
		# ============================
		display_str = "The edit distance is: "
		display_str += str(self.table[len(self.string2) + 1][len(self.string1) + 1])
		print(display_str)
		
		# display alignment
		# ====================
		display_str = "\nThe alignment is: \n"
		r = len(self.string2) + 1
		c = len(self.string1) + 1
		# tuple of (value, next direction)
		alignment = [(self.table[r][c], "")]
		# get the alignment order
		while r > 2 and c > 2:
			# set to minimum of the 3 (prev diagonal, left, and top) + 1
			prev_diagonal = self.table[r - 1][c - 1]
			left = self.table[r][c - 1]
			top = self.table[r - 1][c]
			least = smallest([prev_diagonal, left, top])
			direction = ""
			if prev_diagonal == least:
				r -= 1
				c -= 1
				direction = "diagonal"
			elif left == least:
				c -= 1
				direction = "right"
			elif top == least:
				r -= 1
				direction = "down"
			alignment.insert(0, (least, direction))
		
		# stuck at left side
		if r != 2:
			missing_scores = []
			for i in range(2, r):
				missing_scores.append((self.table[i][2], "down"))
			alignment = missing_scores + alignment
		# stuck at the top side
		elif c != 2:
			missing_scores = []
			for i in range(2, c):
				missing_scores.append((self.table[2][i], "right"))
			alignment = missing_scores + alignment
		alignment.insert(0, (0, "diagonal"))
		
		# word 1 to word 2 (horizontal to vertical)
		aligned_word1 = ""
		index = 0
		for i in range(1, len(alignment)):
			# no action required
			if alignment[i - 1][0] == alignment[i][0]:
				aligned_word1 += str(self.string1[index])
				index += 1
			else:
				if alignment[i - 1][1] == "down":
					# insert from vertical
					aligned_word1 += str(self.string2[index])
					index += 1
				elif alignment[i - 1][1] == "right":
					# remove from horizontal
					aligned_word1 += "_"
				elif alignment[i - 1][1] == "diagonal":
					# replace from vertical
					aligned_word1 += str(self.string2[index])
					index += 1
		
		# word 2 to word 1 (vertical to horizontal)
		aligned_word2 = ""
		index = 0
		for i in range(1, len(alignment)):
			# no action required
			if alignment[i - 1][0] == alignment[i][0]:
				aligned_word2 += str(self.string2[index])
				index += 1
			else:
				if alignment[i - 1][1] == "down":
					# remove from vertical
					aligned_word2 += "_"
				elif alignment[i - 1][1] == "right":
					# insert from horizontal
					aligned_word2 += str(self.string1[index])
					index += 1
				elif alignment[i - 1][1] == "diagonal":
					# replace from horizontal
					aligned_word2 += str(self.string1[index])
					index += 1
		
		display_str += aligned_word1
		display_str += "\n"
		display_str += aligned_word2
		print(display_str)
		
# =========================================
string1 = input("Enter your first string for comparison: ")
string2 = input("Enter your second string for comparison: ")
example = Align_Table(string1, string2)
example.display()
