PROJECT_GEN_PROMPT = """
Generate a list of three projects based off this information:

{data}

The project achievements for each project must align with job qualifications above,
use the job description to provide context for the qualifications.
"""

EXAMPLE_RESPONSE = [
  {
    "title": "AI Job Listing Insight Dashboard",
    "problem_statement": "Job listings are noisy and inconsistent, making it hard for candidates to understand what skills are actually in demand for a target role and location. This project aggregates listings and extracts repeatable skill signals and requirements.",
    "target_users": ["Job seekers", "Career switchers", "University students"],
    "core_features": [
      "Upload or fetch job listings for a role/location and display a searchable list",
      "Extract and rank top skills/tools mentioned across listings",
      "Show per-skill evidence snippets from listings (qualifications/responsibilities)",
      "Filter insights by employment type and remote/hybrid preference"
    ],
    "recommended_tech_stack": ["Python", "Flask", "Pydantic", "React", "Redis"],
    "achieved_qualifications": [
      "Knowledge of APIs, JSON, XML, and OAuth",
      "Familiarity with CI/CD pipelines/DevOps and version control tools like Git",
      "Experience consuming and integrating RESTful APIs",
      "Experience with language: Angular, .NET, Python"
    ]
  },
  {
    "title": "Portfolio Project Generator (Job-Market Driven)",
    "problem_statement": "Candidates struggle to pick portfolio projects that align with real job requirements. This project generates project ideas grounded in job listing qualifications and provides traceable evidence for each idea.",
    "target_users": ["Job seekers", "Bootcamp graduates", "Junior developers"],
    "core_features": [
      "Accept role/location filters and retrieve relevant job listings",
      "Generate 3–5 portfolio project ideas based on extracted qualifications",
      "Attach evidence: show which listings and snippets motivated each idea",
      "Export project plan outline (milestones and feature list) as JSON"
    ],
    "recommended_tech_stack": ["Python", "Flask", "Pydantic", "React", "OpenAI API/Azure OpenAI"],
    "achieved_qualifications": [
      "Technical understanding of cloud platforms (AWS/Azure/GCP), APIs, CI/CD, web technologies, and DevOps practices",
      "Experience with Agile/Scrum or SAFe frameworks and tools (e.g., Jira, Confluence, Azure DevOps)",
      "Experience designing and developing developer-facing products (e.g., SDKs, REST APIs, GraphQL)",
      "Familiarity with scripting languages (Python, Bash) for tooling and automation"
    ]
  },
  {
    "title": "AI-Assisted Requirements-to-Features Mapper",
    "problem_statement": "Job requirements are often vague and duplicated across listings. This project converts requirement text into structured skills and proposes feature implementations that demonstrate those skills in a portfolio project.",
    "target_users": ["Junior developers", "Technical recruiters", "Hiring managers"],
    "core_features": [
      "Paste job description and extract qualifications into structured bullets",
      "Map each qualification to a suggested project feature and acceptance criteria",
      "Generate a recommended tech stack aligned to the extracted skills",
      "Provide a checklist that can be used as a rubric for portfolio readiness"
    ],
    "recommended_tech_stack": ["Python", "Pydantic", "React", "LLM (Azure OpenAI/OpenAI)", "Docker"],
    "achieved_qualifications": [
      "2–5 years of experience in Python programming",
      "Proficiency with Python packages, such as Pandas, NumPy, DashApps",
      "Hands-on experience with AWS (RDS, EC2, serverless) and Open Container Initiative (OCI) container packaging and runtime",
      "Proficiency in building applications using JavaScript and TypeScript"
    ]
  }
]