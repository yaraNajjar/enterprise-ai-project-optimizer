import random
import csv

def generate_project():
    team_size = random.randint(2, 15)
    issues = random.randint(0, 10)
    duration = team_size * random.randint(10, 20) + issues * 5
    cost = duration * team_size * 100
    delay = 1 if issues > 5 else 0

    return [team_size, issues, duration, cost, delay]

with open("projects.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["team_size", "issues", "duration", "cost", "delay"])
    for _ in range(1000):
        writer.writerow(generate_project())

print("Data generated")
