#axis=1 (Horizontal): Operates left-to-right across columns.
# Gives you 1 answer per row $\rightarrow$ [345, 270, 373]
# axis=0 (Vertical): Operates top-to-bottom down rows.
# Gives you 1 answer per column $\rightarrow$ [80., 81., 80., 88.33]


 numpy as np

# Rows = Students (Student 0, Student 1, Student 2)
# Columns = Subjects (Math, Physics, Chemistry, Biology)
scores = np.array([
    [85, 90, 78, 92],  # Student 0
    [60, 65, 70, 75],  # Student 1
    [95, 88, 92, 98]   # Student 2
     ])
student_total_scores = np.array([sum(scores[0,:]),sum(scores[1,:]),sum(scores[2,:])])
print(student_total_scores)

student_total_score =scores.sum(axis=1)
print("studenttotal",student_total_score)
subject_averages = scores.mean(axis=0).round(2)
print("Subject Averages:", subject_averages)

# Set terminal display precision globally to 2 decimal places
np.set_printoptions(precision=3, suppress=True)
#Note: suppress=True prevents NumPy from defaulting to scientific notation for small/large floats.
subject_averages1 = scores.mean(axis=0)
print("Subject Averages:", subject_averages1)