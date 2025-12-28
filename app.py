from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- DATA ----------

personal_info = {
    "name": "Uppara Pallavi",
    "title": "B.Tech Graduate – Seeking Opportunities",
    "objective": "To work in challenging environmental set up where I can get an opportunity to learn, improve skills for my personal growth as well as to contribute positively for the growth of organization.",
    "about": """I am a B.Tech CSE graduate with good skills in Python, SQL, and basic front-end development (HTML & CSS),
    along with a basic understanding of Java. I enjoy learning new technologies, practicing coding, and building small projects.""",
    "technical_skills": [
        "Python",
        "SQL",
        "HTML",
        "CSS",
        "Java – Basic"
    ],
    "soft_skills": ["Team Work", "Adaptability", "Leadership"],
    "hobbies": [
        "Listening to Music",
        "Cooking Indian-style dishes"
    ],
    "email": "pallavi23210@gmail.com",
    "phone": "8576195765",
    "linkedin": "https://www.linkedin.com/in/pallavi-u-00b073270/",
    "github": "https://github.com/Pallavi3271"
}

projects = [
    {
        "name": "Portfolio Website",
        "technologies": "Flask, HTML, CSS",
        "description": "My personal portfolio website showcasing projects, skills, and achievements.",
        "link": "/portfolio_project"  # Internal Flask route
    },
    {
        "name": "Tourism Website",
        "technologies": "HTML, CSS, JavaScript",
        "description": "Developed a tourism website showcasing popular destinations with images and videos.",
        "link": "https://pallavi3271.github.io/Tourism-Website/"  # External link
    },
    {
        "name": "Suicidal Ideation Detection",
        "technologies": "Python, Machine Learning",
        "description": "Machine learning system to detect suicidal ideation using surveys, social media, and clinical records.",
        "link": "/suicidal_project"  # Internal Flask route
    }
]

achievements = [
    "Participated in Ideathon conducted by college",
    "3rd Prize in ML Hackathon at Pulla Reddy Engineering College",
    "Top 7th team in 8-hour Virtual Hackathon by Lumen Quest 2025"
]

education = [
    {
        "degree": "B.Tech - Computer Science and Engineering (Data Science)",
        "institute": "Srinivasa Ramanujan Institute of Technology",
        "year": "2021 – 2025",
        "cgpa": "8.03"
    },
    {
        "degree": "Intermediate (MPC)",
        "institute": "Sri Chaitanya Junior College",
        "year": "2019 – 2021",
        "cgpa": "7.51"
    },
    {
        "degree": "SSC",
        "institute": "Lakshmi English Medium High School",
        "year": "2019",
        "cgpa": "9.3"
    }
]

internships = [
    {
        "title": "Process Mining Intern",
        "organization": "AICTE",
        "duration": "May 2023 – July 2023",
        "description": "Completed virtual internship on Process Mining.",
        "certificate": "process_mining_cert.png"
    },
    {
        "title": "Salesforce Developer Intern",
        "organization": "SmartInternz (Salesforce)",
        "duration": "Aug 2023 – Oct 2023",
        "description": "Completed Salesforce Developer virtual internship.",
        "certificate": "salesforce_cert.png"
    }
]

certifications = [
    "SQL – Great Learning",
    "Python Programming – Cisco",
    "Salesforce Certified AI Associate",
    "Upper-Intermediate English – edX"
]

# ---------- ROUTES ----------

@app.route("/")
def index():
    return render_template("index.html", personal_info=personal_info)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", personal_info=personal_info, projects=projects)

# Internal page for Portfolio Website
@app.route("/portfolio_project")
def portfolio_project_page():
    return render_template("portfolio_project.html", personal_info=personal_info)

# Internal page for Suicidal Ideation Detection
@app.route("/suicidal_project")
def suicidal_project_page():
    return render_template("suicidal_project.html", personal_info=personal_info)

@app.route("/achievements")
def achievements_page():
    return render_template("achievements.html", personal_info=personal_info, achievements=achievements)

@app.route("/education")
def education_page():
    return render_template("education.html", personal_info=personal_info, education=education)

@app.route("/internships")
def internships_page():
    return render_template("internships.html", personal_info=personal_info, internships=internships)

@app.route("/certifications")
def certifications_page():
    return render_template("certifications.html", personal_info=personal_info, certifications=certifications)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "<h2>Thank you! Your message has been sent.</h2>"
    return render_template("contact.html", personal_info=personal_info)

# ---------- RUN ----------

if __name__ == "__main__":
    app.run(debug=True)
