import numpy as np
student_scores = np.array([[85, 90, 78, 88],  
                            [82, 75, 85, 80],  
                            [90, 92, 88, 86],  
                            [70, 80, 78, 90],  
                            [88, 76, 82, 89],  
                            [75, 85, 90, 92],  
                            [80, 85, 87, 84],  
                            [90, 88, 89, 91],  
                            [78, 74, 80, 76],  
                            [85, 89, 84, 83],  
                            [80, 82, 77, 75], 
                            [88, 92, 90, 94],  
                            [82, 78, 75, 80],  
                            [91, 89, 88, 87], 
                            [74, 80, 82, 78],  
                            [85, 90, 91, 92],  
                            [72, 75, 79, 77],  
                            [80, 85, 88, 89],  
                            [90, 95, 92, 91],  
                            [78, 84, 80, 79],  
                            [88, 91, 93, 87],  
                            [76, 82, 85, 80],  
                            [82, 86, 88, 91],  
                            [85, 84, 83, 82], 
                            [88, 90, 92, 93],  
                            [75, 80, 79, 78],  
                            [89, 91, 94, 90],  
                            [82, 84, 85, 86],  
                            [90, 88, 86, 87],  
                            [78, 75, 72, 80], 
                            [81, 83, 85, 82],  
                            [88, 89, 90, 91]])
average_scores = np.mean(student_scores, axis=0)
highest_average_index = np.argmax(average_scores)
highest_average_subject = ["Math", "Science", "English", "History"][highest_average_index]

print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", highest_average_subject)
