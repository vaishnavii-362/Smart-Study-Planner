# Smart Study Planner (AI-Based)

## Project Description
The Smart Study Planner is an AI-based application that helps students manage their study time effectively. It generates a personalized study plan based on subject difficulty, priority, and total available study hours.

## Features
- Input subjects, difficulty level, and priority
- Automatically generates a smart study plan
- Allocates time proportionally using weighted logic
- Displays results in a simple GUI
- Visualizes study plan using a bar graph

##  How It Works
The system uses a weighted decision-making approach:
- Difficulty levels are assigned numerical values (easy = 1, medium = 2, hard = 3)
- Priority levels (1–5) are taken as input
- Final weight = difficulty × priority
- Study time is distributed proportionally based on weights

##  Technologies Used
- Python
- Tkinter (GUI)
- Matplotlib (Visualization)

##  How to Run
1. Install required libraries:
pip install matplotlib
2. Run the Python file:
python study_planner.py

##  Example Input
Subjects: Maths, Physics, Chemistry  
Difficulty: hard, medium, easy  
Priority: 5, 3, 2  
Total Hours: 6  

##  Output
- Maths → Highest time allocation  
- Physics → Medium time allocation  
- Chemistry → Lowest time allocation  
- Bar graph visualization

## Future Scope
- Integration with real ML models
- Tracking student performance over time
- Mobile application development
