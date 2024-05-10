#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
import numpy as np


# In[19]:


# Department ETRX
# Define courses, professors, rooms, days, and timeslots
courses = ['Apti', 'Maths', 'Power System', 'Control System', 'Network Theory','Digital Electronics', 'Analog Circuits']
professors = ['Dr. A', 'Dr. B', 'Dr. C', 'Dr. D', 'Dr. E', 'Dr. F']
rooms = ['101', '102', '103', '104', '105']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#days ={1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
timeslots = [ '10:00 AM - 11:00 AM','11:00 AM - 12:00 PM', '12:00 PM - 1:00 PM', '1:00 PM - 2:00 PM',
             '2:00 PM - 3:00 PM', '3:00 PM - 4:00 PM', '4:00 PM - 5:00 PM']


# In[20]:


# Initialize population
def initialize_population(population_size):
    population = []
    for i in range(population_size):
        timetable = []
        for course in courses:
            professor = random.choice(professors)
            day = random.choice([i for i in range(len(days))])
            timeslot = random.choice([j for j in range(len(timeslots))])
            room = random.choice(rooms)
            timetable.append((course, professor, day, timeslot, room))
        population.append(timetable)
    return population
initialize_population(5)


# In[5]:


# Calculate fitness score
def calculate_fitness(timetable):
    conflicts = 0
    for i in range(len(timetable)):
        for j in range(i+1, len(timetable)):
            if timetable[i][3] == timetable[j][3] and timetable[i][4] == timetable[j][4]:
                conflicts += 1
            elif timetable[i][1] == timetable[j][1] and timetable[i][3] == timetable[j][3]:
                conflicts += 1
    return 1 / (conflicts + 1)


# In[6]:


# Select parents
def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [fitness_score / total_fitness for fitness_score in fitness_scores]
    parents = []
    for i in range(2):
        r = random.uniform(0, 1)
        index = 0
        while r > 0:
            r -= probabilities[index]
            index += 1
        parents.append(population[index - 1])
    return parents


# In[7]:


# Crossover
def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child


# In[8]:


# Mutation
def mutate(timetable, mutation_rate):
    for i in range(len(timetable)):
        if random.random() < mutation_rate:
            course = timetable[i][0]
            professor = random.choice(professors)
            day = random.choice([i for i in range(len(days))])
            timeslot = random.choice([j for j in range(len(timeslots))])
            #timeslot = random.choice(timeslots)
            room = random.choice(rooms)
            timetable[i] = (course, professor, day, timeslot, room)
    return timetable


# In[9]:


# Genetic algorithm
def genetic_algorithm(population_size, mutation_rate, generations):
    # Initialize population
    population = initialize_population(population_size)
    for generation in range(generations):
        # Calculate fitness scores
        fitness_scores = [calculate_fitness(timetable) for timetable in population]
        
        # Select parents
        parents = [select_parents(population, fitness_scores) for i in range(population_size)]
        
        # Crossover
        children = [crossover(parents[i][0], parents[i][1]) for i in range(population_size)]
        
        # Mutation
        mutated_children = [mutate(child, mutation_rate) for child in children]
        
        # Create new population
        population = mutated_children
        
        # Print best timetable in each generation
        best_timetable = max(population, key=calculate_fitness)
        print(f"Generation {generation + 1}: Best fitness score = {calculate_fitness(best_timetable)}, Best timetable = {best_timetable}")
    
    return best_timetable


# In[ ]:


# Example usage
best_timetable = genetic_algorithm(population_size=10, mutation_rate=0.1, generations=10)
print(f"Final timetable: {best_timetable}")


# In[11]:


best_timetable


# In[66]:


'''
y = []
for i in range(len(best_timetable)):
    y.append(best_timetable[i][2][1])
y
'''


# In[13]:


#Outputting data into a grid

timings = ['',
    '3:00 PM - 4:00 PM',
 '2:00 PM - 3:00 PM',
 '12:00 PM - 1:00 PM',
 '11:00 AM - 12:00 PM',
 '10:00 AM - 11:00 AM',
 '1:00 PM - 2:00 PM',
 '3:00 PM - 4:00 PM',
 '1:00 PM - 2:00 PM']

def make_grid(items):
    max_col = 7
    max_row = 6
    return [[' ' for dummy_col in range(max_col)] for dummy_row in range(max_row)]


def place_on_grid(grid, val, key):
    col, row = val
    grid[row][col] = key


l = []
for i in best_timetable:
    l.append(len(i))
#print(max(l))    


def place_items_on_grid(data):
    grid = make_grid(data.values())
    for k, v in data.items():
        place_on_grid(grid, v, k)
    return grid
    
#defining coordinates

y = []
x = []
for i in range(len(best_timetable)-1):
    y.append(best_timetable[i][2])
    x.append(best_timetable[i][3])
#print(x,'\n',y)
x = np.array(x)
y = np.array(y)
z = np.concatenate((x.reshape(-1, 1), y.reshape(-1, 1)), axis=1)

#defining results

results = []
for k in range(len(best_timetable)-1):
    results.append(best_timetable[k][0] + ' [' + best_timetable[k][1]+ '] ' +best_timetable[k][4])


data = {k: val for k, val in zip((results), (z))}

final_TT = place_items_on_grid(data)

###################
#Adding the timings and days in final_TT

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for row in final_TT:
    row.insert(0, days[final_TT.index(row)])

###################
#final_TT.insert(0, timings)

print(final_TT)


# In[15]:


from tabulate import tabulate



# Define CSS styles for the table
timings = ['',
           '10:00 AM - 11:00 AM',
           '11:00 AM - 12:00 PM',
           '12:00 PM - 1:00 PM',
           '1:00 PM - 2:00 PM',
           '2:00 PM - 3:00 PM',
           '3:00 PM - 4:00 PM',
           '4:00 PM - 5:00 PM']

tablefmt = "html"
css = """
<style type=\"text/css\">
    table {
        border-collapse: collapse;
        width: 100%;
    }
    td {
        border: 1px solid black;
        padding: 10px;
        vertical-align: middle;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f5f5f5;
    }
</style>
"""

# Format the table using tabulate
table = tabulate(final_TT, headers=timings, tablefmt=tablefmt)

# Add CSS styles to the table
output = css + table

# Display the table in a web browser
with open("table + Dept.html", "w") as f:
    f.write('<h1 style="font-family: Arial, sans-serif; color: #333; padding: 20px;text-align: center;">Department - Computer Science</h1>')
    f.write(output)
print('Done')

