# -TIME-TABLE-GENERATION-USING-GENETIC-ALGORITHM

In educational institutions, creating a schedule that meets all the requirements and
preferences while allocating scarce resources, such as classrooms, professors, and
courses, can be difficult. The use of genetic algorithms as a practical method for
automating the timetable generating process is examined in this project. The main goal is
to create an effective system that can create timetables of the highest caliber while
adhering to a variety of constraints.

Utilizing a chromosomal representation to describe the timeline and selection,
crossover, and mutation operators to evolve the population, the genetic algorithm
approach is used. The effectiveness of any timetable option is measured using a thorough
fitness evaluation function. Several techniques are used, such as elitism, adaptive
parameter control, and population diversity preservation, to improve the performance of
the algorithm.

# Introduction
The creation of time tables is a difficult undertaking in educational institutions
because it calls for effective resource allocation and satiation of several limitations.
Because of the scheduling problem's intricacy and dynamic nature, conventional
approaches frequently have trouble handling it. In this paper, we suggest a novel method
for creating time tables using a genetic algorithm. In order to iteratively evolve a
population of alternative timetables towards an ideal solution, the genetic algorithm
makes use of the concepts of natural selection and genetic operators.

The genetic algorithm starts by initialising a heterogeneous initial population and
recording the timings as chromosomes. The algorithm explores the solution space and
steadily raises the calibre of the timetables by a sequence of selection, crossover, and
mutation operations. When evaluating fitness, various goals are taken into account,
including scheduling requirements, room utilisation, and clash minimization.

The genetic algorithm produces timetables of excellent quality, according to
experimental data. The programme consistently generated workable and balanced
schedules while accounting for a variety of restrictions and preferences. The genetic
algorithm is superior in terms of solution quality and computational efficiency when
compared to older methods. The suggested approach shows potential for automating and
optimising the creation of time tables at educational institutions, resulting in better
resource utilisation, fewer scheduling conflicts, and higher scheduling efficiency.

# How Genetic Algorithm Works
the following is a general idea of how to create such an algorithm in Python:
1. Define problem space: The schedule problem's variables and constraints need to
be identified. For instance, the courses, instructors, and time slots might be the
variables whereas the room, professor, and course prerequisite availability might
be the constraints.

2. Initialize Population: Create a random population of prospective timetables that
satisfies the restrictions of the issue space as step two of the population
initialization process. A list of tuples, each of which represents a course, a
professor, and a time slot, should be used to describe each schedule.

3. Evaluate Fitness: Give each timetable in the population a fitness score. The
degree to which the timetable complies with the restrictions and preferences of
the problem space should be reflected in the fitness score.

4. Choose parents: Choose the population's fittest members to be parents using a
selection technique.

5. Create offspring: To produce offspring from the chosen parents, use the
crossover and mutation operators. While mutation entails randomly altering
parent schedules, crossover entails switching portions of the parent timetables to
produce new offspring.

6. Evaluate fitness of progeny: Determine the fitness of the progeny produced in
step 5

7. Choose the next generation: Select the people who will replace the current
generation by using a replacement strategy like elitism or generational
replacement.

8. Repeat 4-7 until constraints are satisfied or maximum number of generations are
reached.

# Dataset Used

The dataset was taken from the teacher load assignment data of the Department of
Electronics Engineering for Even semester provided by the curtesy of Dr. Vibha Bora,
Professor & Incharge, BETiC Lab, GHRCE.

The data contains data of 16 professors, and four departments (ETC, ETRX, M.
Tech VSLI and FY). The variables were input to the genetic algorithm to create the
initial population were in the form of a dictionary. Some samples of the input data is
shown below-

>[{'ETRX': {'Analog Communication': {'total_classes': 1,
>'professor': 'Dr. L. P.Thakre',
>'room': 'C02',
>'days': [2],
>'timeslots': [3],
>'slot_durations': [1]},
>'DSP': {'total_classes': 1,
>'professor': 'Dr. D. V. Padole',
>'room': 'C01',
>'days': [0],
>'timeslots': [6],
>'slot_durations': [1]},
>'VLSI': {'Lab-II': {'total_classes': 1,
>'professor': 'Dr. L. P.Thakre',
>'room': 'C01',
>'days': [1],
>'timeslots': [0],
>'slot_durations': [1]}
>}]

# Results

The data was passed into the custom defined genetic_algorithm function with –
population_size=10, mutation_rate=0.1, and generations=10

The resulting timetables for respective departments generated by the genetic
algorithm are depicted in fig.1. These output best timetables are returned in the form of
a list. In Fig. 2 the list of best timetables generated by the genetic_algorithm
function are visualized with the help of the Python Tabulate function, CSS and HTML
and displayed in a supporting browser.

![image](https://github.com/Virja-Kawade/-TIME-TABLE-GENERATION-USING-GENETIC-ALGORITHM/assets/71089824/9c60c4ba-d082-4f05-961e-be16ae3aa831)

Fig.1.Best timetable generated by the Genetic Algorithm in list datatype for the
specified number of Departments (ETRX and VLSI Design)

![image](https://github.com/Virja-Kawade/-TIME-TABLE-GENERATION-USING-GENETIC-ALGORITHM/assets/71089824/903ce8ae-df65-4cd1-812e-d681883ecd1f)

Fig.2.Time Table of Electronics Engineering Department generated using
Genetic Algorithm displayed in HTML file using Tabulate (Python Function), CSS
and HTML

