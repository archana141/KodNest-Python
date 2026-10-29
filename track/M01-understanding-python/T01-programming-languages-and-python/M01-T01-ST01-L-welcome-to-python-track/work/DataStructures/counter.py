#Manually
languages = ["Python"," Java","Python","SQL","Java","Python"]
frequency = {}
for language in languages:
    if language in frequency:
        frequency[language] += 1
    else:
        frequency[language] = 1
print(frequency)

# Using Counter
from collections import Counter
language = ["Python","Java","Python","SQL","Java","Python"]
frequency = Counter(language)
print(frequency)
print(frequency["Python"])
print(frequency["Java"])

languages = ["Python","Java","Python","SQL"]
frequency = Counter(languages)
for language, count in frequency.items():
    print(language, count)

letter_counts = Counter("banana")
print(letter_counts)

# Most common
skills = [
    "Python",
    "Java",
    "Python",
    "SQL",
    "Java",
    "Python"
]
skill_counts = Counter(skills)
print(skill_counts)
frequent_skills = skill_counts.most_common()
print(frequent_skills)

most_required = skill_counts.most_common(1)

skill = most_required[0][0]
count = most_required[0][1]

print(skill)
print(count)
