import os
import http.client
from typing import Dict, Any
from urllib.parse import urlencode
from typing import List, Optional, Tuple

from dotenv import load_dotenv
load_dotenv()

from src.schemas.jsearch_user_view import (
    UserJobSearchResponse,
    UserJobSearchResponses,
    UserJobListing,
    JobHighlights,
    ApplyOption,
    Parameters
)

class JobListingsApi():
    """Class for parsing job listing data from OpenWebNinja API.
    
    This class handles API authentication, request building, and response 
    parsing for job search queries.
    """

    EXAMPLE_RESPONSE = {
        "status": "OK",
        "request_id": "819da6d4-ed87-4348-975b-252f206b96fe",
        "parameters": {
            "query": "developer jobs in chicago",
            "page": 1,
            "num_pages": 1,
            "country": "us",
            "language": "en"
        },
        "data": [
            {
            "job_id": "2F72zgtY-1oB3XaPAAAAAA==",
            "job_title": "Java with Mainframe",
            "employer_name": "Vista Applied Solutions Group Inc",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgB1bACiGCkWTbspOyQ5fJmboniOF8_4JBiS48&s=0",
            "employer_website": None,
            "job_publisher": "LinkedIn",
            "job_employment_type": "Contractor",
            "job_employment_types": [
                "CONTRACTOR"
            ],
            "job_apply_link": "https://www.linkedin.com/jobs/view/java-with-mainframe-at-vista-applied-solutions-group-inc-4328685011?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/java-with-mainframe-at-vista-applied-solutions-group-inc-4328685011?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Jobright",
                "apply_link": "https://jobright.ai/jobs/info/69499b08d1953b5d11c2a04a?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Iitjobs",
                "apply_link": "https://www.iitjobs.com/job/java-with-weblogic-chicago-il-usa-sharpedge-solutions-62948?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "BeBee",
                "apply_link": "https://us.bebee.com/job/31252f3ae7fb4886c60d2f110b84392f?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Job Summary:\n\nThe client is looking for a Full Stack Developer with a primary focus on React front-end (60%) and secondary expertise in Java/Spring Boot (40%). The role also requires experience with Oracle Database and CA 7 / CA 11 schedulers.\n\nResponsibilities:\n• The Enterprise Job Scheduling (EJS) team administers support of the CA7 and CA11 tool set and tasks and their associated processes.\n• This position will be focused on developing a Web application which will automate the CA7 scheduling workflow.\n• Demonstrate technical leadership and provide technical knowledge and capabilities as a team member and individual contributor.\n• Lead resolution processes for complex problems where analysis of situations or data requires an in-depth evaluation of various factors.\n• Develop programs in languages such as Shell Script/REXX/JAVA/REACTjs/SQL for Automation initiatives.\n• Must be able to communicate across differing audiences including technical, managerial and vendors.\n• Can develop technical solution requirements and lead individual or small team initiatives. Participate in 7x24x365 Oncall Support after proper training.\n\nRequired skills\n• Ability to manage multiple deliverables with various time deliveries from days to months.\n• Build interactive user interfaces using NodeJS/REACTJS ensuring responsive and dynamic web applications\n• Develop server-side applications using Java\n• Integrate frontend and backend components to deliver complete web solutions. Implement RESTful APIs and microservices.\n• Design/Develop and maintain databases using Oracle SQL. Write SQL queries, stored procedures and optimize database performance.\n• Ability to work with CI/CD tools/pipelines\n• Ability to work closely with clients to resolve Tool issues.\n• Work in Agile teams, participate in code reviews and use version control tools like GIT, Bitbucket\n• Good communication skills, both written and oral are required as the individual must interface with application developers, support teams, software vendors and management staff.\n• The successful candidate may be required (after suitable training) to participate in a 24x7 Oncall rotation and be required to provide off hours support as necessary.",
            "job_is_remote": False,
            "job_posted_at": "22 hours ago",
            "job_posted_at_timestamp": 1766426400,
            "job_posted_at_datetime_utc": "2025-12-22T18:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": None,
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D2F72zgtY-1oB3XaPAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "The role also requires experience with Oracle Database and CA 7 / CA 11 schedulers",
                "Ability to manage multiple deliverables with various time deliveries from days to months",
                "Build interactive user interfaces using NodeJS/REACTJS ensuring responsive and dynamic web applications",
                "Develop server-side applications using Java",
                "Integrate frontend and backend components to deliver complete web solutions",
                "Ability to work with CI/CD tools/pipelines",
                "Ability to work closely with clients to resolve Tool issues",
                "Work in Agile teams, participate in code reviews and use version control tools like GIT, Bitbucket",
                "Good communication skills, both written and oral are required as the individual must interface with application developers, support teams, software vendors and management staff",
                "The successful candidate may be required (after suitable training) to participate in a 24x7 Oncall rotation and be required to provide off hours support as necessary"
                ],
                "Responsibilities": [
                "The client is looking for a Full Stack Developer with a primary focus on React front-end (60%) and secondary expertise in Java/Spring Boot (40%)",
                "The Enterprise Job Scheduling (EJS) team administers support of the CA7 and CA11 tool set and tasks and their associated processes",
                "This position will be focused on developing a Web application which will automate the CA7 scheduling workflow",
                "Demonstrate technical leadership and provide technical knowledge and capabilities as a team member and individual contributor",
                "Lead resolution processes for complex problems where analysis of situations or data requires an in-depth evaluation of various factors",
                "Develop programs in languages such as Shell Script/REXX/JAVA/REACTjs/SQL for Automation initiatives",
                "Must be able to communicate across differing audiences including technical, managerial and vendors",
                "Can develop technical solution requirements and lead individual or small team initiatives",
                "Participate in 7x24x365 Oncall Support after proper training",
                "Implement RESTful APIs and microservices",
                "Design/Develop and maintain databases using Oracle SQL",
                "Write SQL queries, stored procedures and optimize database performance"
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "aUxpjZGwAgf0g9DZAAAAAA==",
            "job_title": "Developer - .Net/Angular, Loyalty IT",
            "employer_name": "United Airlines",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DMswunk7F25_BeXSf2w8JVHG65s4lc7v5wfG&s=0",
            "employer_website": "https://www.united.com",
            "job_publisher": "United Airlines Jobs",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://careers.united.com/us/en/job/WHQ00025753/Developer-Net-Angular-Loyalty-IT?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "United Airlines Jobs",
                "apply_link": "https://careers.united.com/us/en/job/WHQ00025753/Developer-Net-Angular-Loyalty-IT?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Dice",
                "apply_link": "https://www.dice.com/job-detail/12f73b7a-201b-432a-93d8-3816e014b6c5?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "ZipRecruiter",
                "apply_link": "https://www.ziprecruiter.com/c/United-Airlines,-Inc./Job/Developer-.Net-Angular,-Loyalty-IT/-in-Chicago,IL?jid=bc93d0d4ff2b33b6&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "Glassdoor",
                "apply_link": "https://www.glassdoor.com/job-listing/developer-net-angular-loyalty-it-united-airlines-JV_IC1128808_KO0,32_KE33,48.htm?jl=1009930404316&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Indeed",
                "apply_link": "https://www.indeed.com/viewjob?jk=f51a1e5b07f97a41&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "SimplyHired",
                "apply_link": "https://www.simplyhired.com/job/Wdn8dRyUdJ_dkvL5R_xEgTKdaNC_vgTxPd-xcSvvjY51Lga0trN-0w?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/developer-net-angular-loyalty-it-at-united-airlines-4334600338?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Hispanic Alliance For Career Enhancement",
                "apply_link": "https://jobs.haceonline.org/job/developer-netangular-loyalty-it/81526970/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Achieving our goals starts with supporting yours. Grow your career, access top-tier health and wellness benefits, build lasting connections with your team and our customers, and travel the world using our extensive route network.\n\nCome join us to create what’s next. Let’s define tomorrow, together.\n\nDescription\n\nThe Loyalty IT Developer role will be a contributor for the development of Loyalty critical applications. This role will need to have full stack expertise on technical development in Loyalty technologies including front end customer applications, API development and integration, database & AWS cloud-based services.\n• Contribute to development, execution, and delivery of artifacts/code for Loyalty applications\n• Collaborate with technology leads/developers, business SMEs, UX designers, and technology stakeholders to define technical deliveries as required\n• Integrate Loyalty services and UIs with back-end systems, APIs and analytics platforms\n• Participate in Agile/Scrum methodologies, participate in sprint planning, stand-ups, and retrospectives\n• Participate in integrations between internal platforms, external systems, and cloud services\n• Collaborate with development, infrastructure, and product teams to gather integration requirements and translate them into scalable technical solutions\n• Coordinate unit and integration testing and assist QA teams with end-to-end testing\n• Stay current with industry best practices and emerging technologies in development and integration\n• Escalate and document risks, issues, blockers and dependencies; discuss with team project manager on regular basis\n• Leverage Cloud infrastructure teams to ensure scalable, secure, and high-performance deployments\n• Maintain vendor relationships and third-party integrations when applicable\n• Support and guide the team in removing blockers, maintaining momentum, and ensuring quality\n• Experience delivering full stack applications.\n• Technical understanding of cloud platforms (AWS/Azure/GCP), APIs, CI/CD, web technologies, and DevOps practices\n• Experience with Agile/Scrum or SAFe frameworks and tools (e.g., Jira, Confluence, Azure DevOps)\n• Good communication, leadership, and documentation abilities\n• Knowledge of APIs, JSON, XML, and OAuth\n• Experience with language: Angular, .NET, Python\n• Familiarity with CI/CD pipelines/DevOps and version control tools like Git\n• Familiarity with compliance standards (e.g., Accessibility, GDPR, PCI-DSS) in cloud solutions\nQualifications\n\nWhat’s needed to succeed (Minimum Qualifications):\n\n· Bachelor's degree in Computer science, software engineering, or related field\n\n· 3+ years of related experience or successful completion of United DT Early Career Digital Leadership Program (ECDLP)\n\n· Proficient in a coding language and building back-end components\n\n· Problem solving\n\n· Attention to detail\n\n· Effective Communication (verbal + written)\n\n· Demonstrates and eagerness to learn\n\n· Demonstrate advanced knowledge of SDLC processes, inputs/outputs, standards and best practices\n\n· Demonstrate advance knowledge of development methodologies, software design and design patterns\n\n· Demonstrate advance knowledge of the application of development domain areas and specific technologies and tool set\n\n· Must be legally authorized to work in the United States for any employer without sponsorship\n\n· Successful completion of interview required to meet job qualification\n\n· Reliable, punctual attendance is an essential function of the position\n\nWhat will help you propel from the pack (Preferred Qualifications):\n\n· Knowledge of AWS ECS, S3, Lambdas and PostGres databases\n\n· Knowledge of Kong, Copilot, and UI Accessibility.\n\n· Cloud certification\n\n· SaFe Agile Certification\n\n· Exposure to Dynatrace\n\n· Agile Methodologies\n\n· SQL, Oracle Experience, Relational DB Experience\n\n· Code Repositories like Github\n\n· Microsoft Office tools, PowerPoint, Excel\n\n· Dev Ops Experience\n\n· UI Analytics (Google Analytics)\n\n· Continuous Integration & Continuous Deployment\n\nThe base pay range for this role is $87,780.00 to $114,376.00.\nThe base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills. This position is also eligible for bonus and/or long-term incentive compensation awards.\n\nYou may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges.\n\nUnited Airlines is an equal opportunity employer. United Airlines recruits, employs, trains, compensates and promotes regardless of race, religion, color, national origin, gender identity, sexual orientation, physical ability, age, veteran status and other protected status as required by applicable law. Equal Opportunity Employer - Minorities/Women/Veterans/Disabled/LGBT.\n\nWe will ensure that individuals with disabilities are provided reasonable accommodation to participate in the job application or interview process, to perform crucial job functions. Please contact JobAccommodations@united.com to request accommodation.",
            "job_is_remote": False,
            "job_posted_at": "2 days ago",
            "job_posted_at_timestamp": 1766275200,
            "job_posted_at_datetime_utc": "2025-12-21T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "dental_coverage",
                "paid_time_off",
                "health_insurance"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DaUxpjZGwAgf0g9DZAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "Technical understanding of cloud platforms (AWS/Azure/GCP), APIs, CI/CD, web technologies, and DevOps practices",
                "Experience with Agile/Scrum or SAFe frameworks and tools (e.g., Jira, Confluence, Azure DevOps)",
                "Good communication, leadership, and documentation abilities",
                "Knowledge of APIs, JSON, XML, and OAuth",
                "Experience with language: Angular, .NET, Python",
                "Familiarity with CI/CD pipelines/DevOps and version control tools like Git",
                "Familiarity with compliance standards (e.g., Accessibility, GDPR, PCI-DSS) in cloud solutions",
                "Bachelor's degree in Computer science, software engineering, or related field",
                "3+ years of related experience or successful completion of United DT Early Career Digital Leadership Program (ECDLP)",
                "Proficient in a coding language and building back-end components",
                "Problem solving",
                "Attention to detail",
                "Effective Communication (verbal + written)",
                "Demonstrates and eagerness to learn",
                "Demonstrate advanced knowledge of SDLC processes, inputs/outputs, standards and best practices",
                "Demonstrate advance knowledge of development methodologies, software design and design patterns",
                "Demonstrate advance knowledge of the application of development domain areas and specific technologies and tool set",
                "Must be legally authorized to work in the United States for any employer without sponsorship",
                "Successful completion of interview required to meet job qualification",
                "Reliable, punctual attendance is an essential function of the position"
                ],
                "Benefits": [
                "The base pay range for this role is $87,780.00 to $114,376.00",
                "The base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills",
                "This position is also eligible for bonus and/or long-term incentive compensation awards",
                "You may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges"
                ],
                "Responsibilities": [
                "The Loyalty IT Developer role will be a contributor for the development of Loyalty critical applications",
                "This role will need to have full stack expertise on technical development in Loyalty technologies including front end customer applications, API development and integration, database & AWS cloud-based services",
                "Contribute to development, execution, and delivery of artifacts/code for Loyalty applications",
                "Collaborate with technology leads/developers, business SMEs, UX designers, and technology stakeholders to define technical deliveries as required",
                "Integrate Loyalty services and UIs with back-end systems, APIs and analytics platforms",
                "Participate in Agile/Scrum methodologies, participate in sprint planning, stand-ups, and retrospectives",
                "Participate in integrations between internal platforms, external systems, and cloud services",
                "Collaborate with development, infrastructure, and product teams to gather integration requirements and translate them into scalable technical solutions",
                "Coordinate unit and integration testing and assist QA teams with end-to-end testing",
                "Stay current with industry best practices and emerging technologies in development and integration",
                "Escalate and document risks, issues, blockers and dependencies; discuss with team project manager on regular basis",
                "Leverage Cloud infrastructure teams to ensure scalable, secure, and high-performance deployments",
                "Maintain vendor relationships and third-party integrations when applicable",
                "Support and guide the team in removing blockers, maintaining momentum, and ensuring quality",
                "Experience delivering full stack applications"
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "rDsBeV_AmCEWMVo7AAAAAA==",
            "job_title": "Python Developer - Associate",
            "employer_name": "BlackRock",
            "employer_logo": None,
            "employer_website": "https://www.blackrock.com",
            "job_publisher": "BlackRock Careers",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://careers.blackrock.com/job/chicago/python-developer-associate/45831/86556589504?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "BlackRock Careers",
                "apply_link": "https://careers.blackrock.com/job/chicago/python-developer-associate/45831/86556589504?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Indeed",
                "apply_link": "https://www.indeed.com/viewjob?jk=fa1793c877b39b55&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Built In Chicago",
                "apply_link": "https://www.builtinchicago.org/job/python-developer-associate/7951673?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "ZipRecruiter",
                "apply_link": "https://www.ziprecruiter.com/c/BlackRock/Job/Python-Developer-Associate/-in-Chicago,IL?jid=a011fd60700d1a33&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "Built In",
                "apply_link": "https://builtin.com/job/python-developer-associate/7951673?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Jobright",
                "apply_link": "https://jobright.ai/jobs/info/693d9c50aa598a08c3ee2a82?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/python-developer-associate-at-blackrock-4343610029?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Institute Of Data Jobs",
                "apply_link": "https://jobs.institutedata.com/job/4503961/python-developer-associate/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "About this role\n\nAbout This Role \nWe are a dynamic, data-driven team at the intersection of finance and technology.\n\nAs a software engineer, you will build applications and processes to help drive business growth. This position requires strong programming skills, analytical thinking, and a passion for learning. You will collaborate with experienced engineers to develop and improve software systems. \n\nRole Responsibilities:\n• Design, code, test, and support reliable, robust software applications and services that meet high-quality standards \n• Participate in cross-functional feature requirements gathering, design, and implementation \n• Collaborate with product management to prioritize and organize development sprints \n• Perform code reviews and provide timely, constructive feedback to fellow engineers \n\nKey Qualifications \n• 2–5 years of experience in Python programming \n• Strong background in mathematics, algorithms, logic, and statistics \n• Extensive database experience (MySQL preferred; SQL/Postgres also valuable)\n• Bachelor’s or Master’s degree in Computer Science or STEM field \n\nRelevant Experience:\n• Proficiency with Python packages, such as Pandas, NumPy, DashApps \n• Hands-on experience with AWS (RDS, EC2, serverless) and Open Container Initiative (OCI) container packaging and runtime \n• Interest and knowledge in finance, particularly Options, Stocks, and Bonds\n\nFor Chicago, IL Only the salary range for this position is USD$96,000.00 - USD$124,000.00 . Additionally, employees are eligible for an annual discretionary bonus, and benefits including healthcare, leave benefits, and retirement benefits. BlackRock operates a pay-for-performance compensation philosophy and your total compensation may vary based on role, location, and firm, department and individual performance.\n\nOur benefits\n\nTo help you stay energized, engaged and inspired, we offer a wide range of benefits including a strong retirement plan, tuition reimbursement, comprehensive healthcare, support for working parents and Flexible Time Off (FTO) so you can relax, recharge and be there for the people you care about.\n\nOur hybrid work model\n\nBlackRock’s hybrid work model is designed to enable a culture of collaboration and apprenticeship that enriches the experience of our employees, while supporting flexibility for all. Employees are currently required to work at least 4 days in the office per week, with the flexibility to work from home 1 day a week. Some business groups may require more time in the office due to their roles and responsibilities. We remain focused on increasing the impactful moments that arise when we work together in person – aligned with our commitment to performance and innovation. As a new joiner, you can count on this hybrid model to accelerate your learning and onboarding experience here at BlackRock.\n\nAbout BlackRock\n\nAt BlackRock, we are all connected by one mission: to help more and more people experience financial well-being. Our clients, and the people they serve, are saving for retirement, paying for their children’s educations, buying homes and starting businesses. Their investments also help to strengthen the global economy: support businesses small and large; finance infrastructure projects that connect and power cities; and facilitate innovations that drive progress.\n\nThis mission would not be possible without our smartest investment – the one we make in our employees. It’s why we’re dedicated to creating an environment where our colleagues feel welcomed, valued and supported with networks, benefits and development opportunities to help them thrive.\n\nFor additional information on BlackRock, please visit @blackrock | Twitter: @blackrock | LinkedIn: www.linkedin.com/company/blackrock\n\nBlackRock is proud to be an equal opportunity workplace. We are committed to equal employment opportunity to all applicants and existing employees, and we evaluate qualified applicants without regard to race, creed, color, national origin, sex (including pregnancy and gender identity/expression), sexual orientation, age, ancestry, physical or mental disability, marital status, political affiliation, religion, citizenship status, genetic information, veteran status, or any other basis protected under applicable federal, state, or local law. View the EEOC’s Know Your Rights poster and its supplement and the pay transparency statement.\n\nBlackRock is committed to full inclusion of all qualified individuals and to providing reasonable accommodations or job modifications for individuals with disabilities. If reasonable accommodation/adjustments are needed throughout the employment process, please email Disability.Assistance@blackrock.com. All requests are treated in line with our privacy policy.\n\nBlackRock will consider for employment qualified applicants with arrest or conviction records in a manner consistent with the requirements of the law, including any applicable fair chance law.",
            "job_is_remote": False,
            "job_posted_at": "12 days ago",
            "job_posted_at_timestamp": 1765411200,
            "job_posted_at_datetime_utc": "2025-12-11T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "health_insurance"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DrDsBeV_AmCEWMVo7AAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "This position requires strong programming skills, analytical thinking, and a passion for learning",
                "2–5 years of experience in Python programming ",
                "Strong background in mathematics, algorithms, logic, and statistics ",
                "Bachelor’s or Master’s degree in Computer Science or STEM field ",
                "Proficiency with Python packages, such as Pandas, NumPy, DashApps ",
                "Hands-on experience with AWS (RDS, EC2, serverless) and Open Container Initiative (OCI) container packaging and runtime ",
                "Interest and knowledge in finance, particularly Options, Stocks, and Bonds"
                ],
                "Benefits": [
                "For Chicago, IL Only the salary range for this position is USD$96,000.00 - USD$124,000.00 ",
                "Additionally, employees are eligible for an annual discretionary bonus, and benefits including healthcare, leave benefits, and retirement benefits",
                "BlackRock operates a pay-for-performance compensation philosophy and your total compensation may vary based on role, location, and firm, department and individual performance",
                "To help you stay energized, engaged and inspired, we offer a wide range of benefits including a strong retirement plan, tuition reimbursement, comprehensive healthcare, support for working parents and Flexible Time Off (FTO) so you can relax, recharge and be there for the people you care about",
                "Employees are currently required to work at least 4 days in the office per week, with the flexibility to work from home 1 day a week"
                ],
                "Responsibilities": [
                "As a software engineer, you will build applications and processes to help drive business growth",
                "You will collaborate with experienced engineers to develop and improve software systems. ",
                "Design, code, test, and support reliable, robust software applications and services that meet high-quality standards ",
                "Participate in cross-functional feature requirements gathering, design, and implementation ",
                "Collaborate with product management to prioritize and organize development sprints ",
                "Perform code reviews and provide timely, constructive feedback to fellow engineers "
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "O7svObPo50ybJFzDAAAAAA==",
            "job_title": "Java Software Engineer (Trading Infrastructure)",
            "employer_name": "NJF Global Holdings Ltd",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKkUjCOniaj-RvOkeI4Yeau_oYoJpb2XIwLqOm&s=0",
            "employer_website": None,
            "job_publisher": "LinkedIn",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://www.linkedin.com/jobs/view/java-software-engineer-trading-infrastructure-at-njf-global-holdings-ltd-4345824659?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/java-software-engineer-trading-infrastructure-at-njf-global-holdings-ltd-4345824659?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Java Software Engineer (Trading Infrastructure)\n\nSalary: $200k-300k\n\nTotal compensation: $400k-800k depending on seniority and performance\n\nWe’re partnered with a leading high frequency trading firm looking for a Java Software Engineer to join their core engineering team in Chicago.\n\nYou’ll collaborate with Research, Systems, and Operations groups to design and maintain the software infrastructure that underpins large-scale, automated trading and research systems.\n\nThis is a high-impact engineering role, offering the chance to work on mission-critical systems at scale while collaborating with some of the brightest minds in the industry.\n\nWhat you’ll do:\n• Enhance and expand core research and trading infrastructure.\n• Design and implement distributed storage and compute systems with demanding performance and reliability requirements.\n• Improve network communications for ultra-low-latency systems.\n• Identify and resolve performance bottlenecks across software, open-source libraries, and operating systems.\n• Research and integrate new technologies to drive stability, scalability, and speed.\n\nWhat we’re looking for:\n• Strong foundation in software engineering principles.\n• Proven expertise in Java (with experience in writing, refactoring, and debugging complex systems).\n• Solid understanding of distributed systems\n• Experience with Linux; familiarity with C++ is a plus.\n• Ideally good knowledge of networking and storage systems\n• A problem-solver with a hands-on mindset and ability to work both independently and in collaborative teams.",
            "job_is_remote": False,
            "job_posted_at": "1 day ago",
            "job_posted_at_timestamp": 1766361600,
            "job_posted_at_datetime_utc": "2025-12-22T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": None,
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DO7svObPo50ybJFzDAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_min_salary": 200000,
            "job_max_salary": 300000,
            "job_salary_period": "YEAR",
            "job_highlights": {
                "Qualifications": [
                "Strong foundation in software engineering principles",
                "Proven expertise in Java (with experience in writing, refactoring, and debugging complex systems)",
                "Solid understanding of distributed systems",
                "Ideally good knowledge of networking and storage systems",
                "A problem-solver with a hands-on mindset and ability to work both independently and in collaborative teams"
                ],
                "Benefits": [
                "Salary: $200k-300k",
                "Total compensation: $400k-800k depending on seniority and performance"
                ],
                "Responsibilities": [
                "You’ll collaborate with Research, Systems, and Operations groups to design and maintain the software infrastructure that underpins large-scale, automated trading and research systems",
                "This is a high-impact engineering role, offering the chance to work on mission-critical systems at scale while collaborating with some of the brightest minds in the industry",
                "Enhance and expand core research and trading infrastructure",
                "Design and implement distributed storage and compute systems with demanding performance and reliability requirements",
                "Improve network communications for ultra-low-latency systems",
                "Identify and resolve performance bottlenecks across software, open-source libraries, and operating systems",
                "Research and integrate new technologies to drive stability, scalability, and speed"
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "bwzGviK0m_f48GYVAAAAAA==",
            "job_title": "Front End Developer - Angular, Information Technology",
            "employer_name": "United Airlines",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DMswunk7F25_BeXSf2w8JVHG65s4lc7v5wfG&s=0",
            "employer_website": "https://www.united.com",
            "job_publisher": "United Airlines Jobs",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://careers.united.com/us/en/job/WHQ00025791/Front-End-Developer-Angular-Information-Technology?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "United Airlines Jobs",
                "apply_link": "https://careers.united.com/us/en/job/WHQ00025791/Front-End-Developer-Angular-Information-Technology?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "ZipRecruiter",
                "apply_link": "https://www.ziprecruiter.com/c/United-Airlines,-Inc./Job/Front-End-Developer-Angular,-Information-Technology/-in-Chicago,IL?jid=ce938474365cf56a&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "Indeed",
                "apply_link": "https://www.indeed.com/viewjob?jk=12ce22290eb8bbd6&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "SimplyHired",
                "apply_link": "https://www.simplyhired.com/job/ToQpNB3rYlxsyyM53t5KRGLIRdVIIv3NxBROD6f-67oDhDHriMvoEQ?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/front-end-developer-angular-information-technology-at-united-airlines-4344845151?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JSfirm.com",
                "apply_link": "https://www.jsfirm.com/job/Other-Front-End-Developer---Angular,-Information-Technology/Chicago-Illinois/jobID_1801539?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Hispanic Alliance For Career Enhancement",
                "apply_link": "https://jobs.haceonline.org/job/front-end-developer-angular-information-technology/81720528/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JobGet",
                "apply_link": "https://www.jobget.com/jobs/job/f125b3c7-0ef5-4859-985a-b237e136ee68?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Achieving our goals starts with supporting yours. Grow your career, access top-tier health and wellness benefits, build lasting connections with your team and our customers, and travel the world using our extensive route network.\n\nCome join us to create what’s next. Let’s define tomorrow, together.\n\nDescription\n\nUnited's Digital Technology team is comprised of many talented individuals all working together with cutting-edge technology to build the best airline in the history of aviation. Our team designs, develops and maintains massively scaling technology solutions brought to life with innovative architectures, data analytics, and digital solutions.\n\nJob overview and responsibilities\n\nThe Front-End Developer plays an important role in creating and maintaining the strategic partnership between business needs and technology delivery. The Developer's role is to plan, design, develop and launch efficient systems and solutions in support of core Contact Center applications and organizational functions. This individual will utilize effective communication, analytical, and problem-solving skills to help identify, communicate / resolve issues, opportunities, or problems to maximize the benefit of IT and Business investments. The Developer is experienced and self - sufficient in performing their responsibilities requiring little supervision, but general guidance and direction.\n• Develop, maintain, and optimize web applications using Angular, TypeScript, HTML5, and CSS3.\n• Implement clean, modular, and maintainable code following established standards and best practices.\n• Collaborate with backend developers to integrate RESTful APIs built with .NET Core and C#.\n• Participate in code reviews, design discussions, and architectural decision-making.\n• Troubleshoot, debug, and resolve issues in both front-end and API layers.\n• Contribute to UI/UX improvements, focusing on scalability, accessibility, and performance.\n• Assist in deployment and continuous integration activities, with exposure to DevOps pipelines and tools.\n• Stay current with emerging technologies, frameworks, and tools in web development.\n• Use AI-assisted tools (e.g., for code completion, documentation, or testing) thoughtfully to enhance productivity while maintaining code integrity and accuracy.\n\nQualifications\n\nWhat’s needed to succeed (Minimum Qualifications):\n• Bachelor's degree in Computer science, software engineering, or related field of study\n• 3+ years of professional experience in web application development or successful completion of United DT Early Career Digital Leadership Program (ECDLP)\n• Experience in JavaScript (ES6+), TypeScript, HTML5, and CSS3/SASS or similar.\n• Hands-on experience with modern Angular (v12 or newer).\n• Understanding of cloud platforms (AWS preferred).\n• Solid understanding of core web concepts such as (or similar):\n• Component-based architecture\n• Reactive programming (RxJS)\n• State management and routing\n• Routing and lazy loading\n• Reusable UI patterns\n• Experience consuming and integrating RESTful APIs.\n• Understanding of source control systems (Git).\n• Familiarity with Agile/Scrum or Waterfall development practices.\n• Strong problem-solving and analytical abilities.\n• Effective communication skills with both technical and non-technical stakeholders.\n• Self-motivated with a proactive approach to learning and skill growth.\n• Must be legally authorized to work in the United States for any employer without sponsorship\n\nWhat will help you propel from the pack (Preferred Qualifications):\n• Exposure to or interest in .NET Core and C# backend development.\n• Collaborative mindset and ability to mentor junior developers when needed.\n• Awareness of AI-powered developer tools (e.g., GitHub Copilot, ChatGPT, etc.) and how to use them responsibly.\n• Knowledge of DevOps practices — CI/CD pipelines, build automation, containerization (Docker).\n• Experience with solution design or contributing to architectural discussions.\n• Familiarity with testing frameworks (Cypress, Jasmine, Karma, Jest, or similar).\n• Awareness of AI ethics, data privacy, and security considerations in code generation.\n\nThe base pay range for this role is $87,780.00 to $114,376.00.\nThe base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills. This position is also eligible for bonus and/or long-term incentive compensation awards.\n\nYou may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges.\n\nUnited Airlines is an equal opportunity employer. United Airlines recruits, employs, trains, compensates and promotes regardless of race, religion, color, national origin, gender identity, sexual orientation, physical ability, age, veteran status and other protected status as required by applicable law. Equal Opportunity Employer - Minorities/Women/Veterans/Disabled/LGBT.\n\nWe will ensure that individuals with disabilities are provided reasonable accommodation to participate in the job application or interview process, to perform crucial job functions. Please contact JobAccommodations@united.com to request accommodation.",
            "job_is_remote": False,
            "job_posted_at": "16 hours ago",
            "job_posted_at_timestamp": 1766448000,
            "job_posted_at_datetime_utc": "2025-12-23T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "paid_time_off",
                "health_insurance",
                "dental_coverage"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DbwzGviK0m_f48GYVAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "Bachelor's degree in Computer science, software engineering, or related field of study",
                "3+ years of professional experience in web application development or successful completion of United DT Early Career Digital Leadership Program (ECDLP)",
                "Experience in JavaScript (ES6+), TypeScript, HTML5, and CSS3/SASS or similar",
                "Hands-on experience with modern Angular (v12 or newer)",
                "Solid understanding of core web concepts such as (or similar):",
                "Component-based architecture",
                "Reactive programming (RxJS)",
                "State management and routing",
                "Routing and lazy loading",
                "Reusable UI patterns",
                "Experience consuming and integrating RESTful APIs",
                "Understanding of source control systems (Git)",
                "Familiarity with Agile/Scrum or Waterfall development practices",
                "Strong problem-solving and analytical abilities",
                "Effective communication skills with both technical and non-technical stakeholders",
                "Self-motivated with a proactive approach to learning and skill growth",
                "Must be legally authorized to work in the United States for any employer without sponsorship"
                ],
                "Benefits": [
                "The base pay range for this role is $87,780.00 to $114,376.00",
                "The base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills",
                "This position is also eligible for bonus and/or long-term incentive compensation awards",
                "You may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges"
                ],
                "Responsibilities": [
                "The Front-End Developer plays an important role in creating and maintaining the strategic partnership between business needs and technology delivery",
                "The Developer's role is to plan, design, develop and launch efficient systems and solutions in support of core Contact Center applications and organizational functions",
                "This individual will utilize effective communication, analytical, and problem-solving skills to help identify, communicate / resolve issues, opportunities, or problems to maximize the benefit of IT and Business investments",
                "The Developer is experienced and self - sufficient in performing their responsibilities requiring little supervision, but general guidance and direction",
                "Develop, maintain, and optimize web applications using Angular, TypeScript, HTML5, and CSS3",
                "Implement clean, modular, and maintainable code following established standards and best practices",
                "Collaborate with backend developers to integrate RESTful APIs built with .NET Core and C#",
                "Participate in code reviews, design discussions, and architectural decision-making",
                "Troubleshoot, debug, and resolve issues in both front-end and API layers",
                "Contribute to UI/UX improvements, focusing on scalability, accessibility, and performance",
                "Assist in deployment and continuous integration activities, with exposure to DevOps pipelines and tools",
                "Stay current with emerging technologies, frameworks, and tools in web development",
                "Use AI-assisted tools (e.g., for code completion, documentation, or testing) thoughtfully to enhance productivity while maintaining code integrity and accuracy"
                ]
            },
            "job_onet_soc": "15113400",
            "job_onet_job_zone": "3"
            },
            {
            "job_id": "XS3f9Qt13Iou8EpwAAAAAA==",
            "job_title": "Application Developer",
            "employer_name": "CFS",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl24XkFtIe3rWI6Gn-TfM5-QL7AHFGAmVr_Oeb&s=0",
            "employer_website": None,
            "job_publisher": "ZipRecruiter",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://www.ziprecruiter.com/c/CFS/Job/Application-Developer/-in-Chicago,IL?jid=55926a07121af1be&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": True,
            "apply_options": [
                {
                "publisher": "ZipRecruiter",
                "apply_link": "https://www.ziprecruiter.com/c/CFS/Job/Application-Developer/-in-Chicago,IL?jid=55926a07121af1be&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "Glassdoor",
                "apply_link": "https://www.glassdoor.com/job-listing/application-developer-factivity-JV_IC1128808_KO0,21_KE22,31.htm?jl=1006704224136&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "SimplyHired",
                "apply_link": "https://www.simplyhired.com/job/jdugrFXIr0tNN-qumtJojzI5vXbJDNBmfeDSuQQIAmfQLlSp8W1L8A?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/application-developer-at-cfs-4349807275?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "BeBee",
                "apply_link": "https://us.bebee.com/job/0a70bf59313e7b5342489b714b861181?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Talents By Vaia",
                "apply_link": "https://talents.vaia.com/companies/law-firm/application-developer-24017008/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JobLeads",
                "apply_link": "https://www.jobleads.com/us/job/application-developer--chicago--eb1b118ecbb259a156a0b0560c580e15f?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Jobs.weekday.works",
                "apply_link": "https://jobs.weekday.works/1872-consulting-application-developer?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                }
            ],
            "job_description": "Application Developer\n• LOCAL CANDIDATES ONLY*\n• NO SPONSORSHIP*\n\nTitle: Application Developer\nCompensation: $120,000 – $140,000\nWork Environment: Hybrid (2 days onsite per week)\nLocation: Chicago, IL\nBenefits: M/D/V, 401K + PTO and Sick days\n\nApplication Developer\nPrimary Responsibilities:\n• Perform both application development and support responsibilities\n• Codes, tests, debugs, and implements applications from complex requirements\n• Design and develop custom applications and integrations with 3rd party systems\n• Analyze, design, and develop new applications when necessary\n• Provide support for incoming IS application support requests and/or questions\n• Answer queries and resolve issues with software applications\n• Escalate or close tickets and tasks via online tools including FreshService, JIRA, etc\n• Conduct regular quality checks with product teams ensure issues are resolved\n• Manages application CI/CD pipelines in tools such as DevOps\n• Prepares technical documentation including architecture diagrams, design documents, and guidelines to facilitate knowledge transfer and ensure maintainability of applications\n• Performs other duties as assigned\n\nApplication Developer\nMinimum Educational & Experiential Qualifications:\n• Bachelor’s degree in computer science, engineering, or related field or equivalent experience\n• 3+ years’ experience as an Applications Developer or in a similar role\n• Strong proven experience with Azure DevOps and the Azure Cloud Environment\n• Familiarity with Microsoft Power Platform including Power Automate, Power BI, Power Apps, and Dataverse\n• Experience using Microsoft SQL Server to write and debug Transact-SQL\n• Proven experience working on SSO including OAuth/OIDC and SAML\n• Strong experience with the following: C#, ASP.NET, LINQ, MVC, web APIs (RESTful and SOAP)\n• Ample experience with HTML5, CSS, React, Responsive design, and web layout design\n\nBuild a rewarding long-term career with us at CFS—when we knock, doors open.\n\nApply now!\n\nCFS Technology is a Chicagoland based, IT dedicated search practice. We provide technology specialists on a temporary and permanent basis across a broad range of industries. We work closely with our clients to better understand their specific needs, which ensures that each placement we do is the absolute best.\n#INDEC2025\n\n#ZRCFSTECH\n\n#LI-AC7\n\nCompany DescriptionCFS is the industry’s leading employee-owned staffing firm, connecting top talent in accounting, finance, technology, and human resources. We provide skilled professionals on both a temporary and permanent basis across diverse industries, leveraging our extensive network to match the right people with the right opportunities.\n\nOur dedication to excellence extends to our award-winning culture, recognized repeatedly for growth, recruiting, workplace environment, and employee support. Honors include Forbes’ “America’s Best Recruiting and Temporary Staffing Firms,” Staffing Industry Analysts’ top U.S. staffing rankings, FlexJobs’ Top 100 Companies for Remote and Hybrid Work, Top Workplaces USA, Newsweek’s Best Practices awards, and more.",
            "job_is_remote": False,
            "job_posted_at": "11 days ago",
            "job_posted_at_timestamp": 1765497600,
            "job_posted_at_datetime_utc": "2025-12-12T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "paid_time_off",
                "health_insurance"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DXS3f9Qt13Iou8EpwAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_min_salary": 120000,
            "job_max_salary": 140000,
            "job_salary_period": "YEAR",
            "job_highlights": {
                "Qualifications": [
                "Bachelor’s degree in computer science, engineering, or related field or equivalent experience",
                "3+ years’ experience as an Applications Developer or in a similar role",
                "Strong proven experience with Azure DevOps and the Azure Cloud Environment",
                "Familiarity with Microsoft Power Platform including Power Automate, Power BI, Power Apps, and Dataverse",
                "Experience using Microsoft SQL Server to write and debug Transact-SQL",
                "Proven experience working on SSO including OAuth/OIDC and SAML",
                "Strong experience with the following: C#, ASP.NET, LINQ, MVC, web APIs (RESTful and SOAP)",
                "Ample experience with HTML5, CSS, React, Responsive design, and web layout design"
                ],
                "Benefits": [
                "NO SPONSORSHIP*",
                "Compensation: $120,000 – $140,000",
                "Work Environment: Hybrid (2 days onsite per week)",
                "Benefits: M/D/V, 401K + PTO and Sick days"
                ],
                "Responsibilities": [
                "Perform both application development and support responsibilities",
                "Codes, tests, debugs, and implements applications from complex requirements",
                "Design and develop custom applications and integrations with 3rd party systems",
                "Analyze, design, and develop new applications when necessary",
                "Provide support for incoming IS application support requests and/or questions",
                "Answer queries and resolve issues with software applications",
                "Escalate or close tickets and tasks via online tools including FreshService, JIRA, etc",
                "Conduct regular quality checks with product teams ensure issues are resolved",
                "Manages application CI/CD pipelines in tools such as DevOps",
                "Prepares technical documentation including architecture diagrams, design documents, and guidelines to facilitate knowledge transfer and ensure maintainability of applications",
                "Performs other duties as assigned"
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "qxpNhUunuUN810mdAAAAAA==",
            "job_title": "C++ Software Developer – Trading Strategy Execution",
            "employer_name": "Edgehog Trading",
            "employer_logo": None,
            "employer_website": "https://www.edgehogtrading.com",
            "job_publisher": "Indeed",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://www.indeed.com/viewjob?jk=6fca8169da4f9942&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "Indeed",
                "apply_link": "https://www.indeed.com/viewjob?jk=6fca8169da4f9942&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Built In Chicago",
                "apply_link": "https://www.builtinchicago.org/job/c-software-developer-trading-strategy-execution/7582418?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Built In",
                "apply_link": "https://builtin.com/job/c-software-developer-trading-strategy-execution/7582418?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "SimplyHired",
                "apply_link": "https://www.simplyhired.com/job/ZpLErjZ0y24_BKcdXy440PoZJP3ElUqz4JLFvUIm-GU4hbJK4xJpeQ?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/c%2B%2B-software-developer-%E2%80%93-trading-strategy-execution-at-edgehog-trading-4333839333?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Teal",
                "apply_link": "https://www.tealhq.com/job/c-software-developer-trading-strategy-execution_7ea1a62cbf029698ddc3d97b420789d83cdce?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Jobright",
                "apply_link": "https://jobright.ai/jobs/info/6932bdca764507023d1b04af?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "BeBee",
                "apply_link": "https://us.bebee.com/job/a982932bf5eef19d58325ed203b956d3?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "About Us\n\nEdgehog Trading is a technology-driven trading firm specializing in trading options on futures. We combine deep market expertise with high-performance software to capitalize on opportunities in one of the most competitive electronic markets in the world. Our edge comes from tight integration between traders and engineers, enabling rapid development and precise execution of trading strategies.\n\nThe Role\n\nWe are looking for an experienced C++ Software Developer to join our trading technology team. You’ll play a critical role in building and maintaining the systems responsible for executing our trading strategies with speed and precision. Your work will directly impact our ability to respond to market opportunities in real time.\n\nWhat You’ll Do\n• Design, implement, and maintain low-latency C++ applications for trading strategy execution\n• Collaborate closely with traders, quants, and other engineers to translate strategies into robust, production-ready systems\n• Optimize performance at every level: networking, OS, compiler, and code\n• Contribute to system architecture, instrumentation, and deployment pipelines\n• Debug, monitor, and improve systems operating under real-world conditions\n\nWhat We’re Looking For\n• Strong proficiency in modern C++ (C++17 and above)\n• Deep understanding of computer science fundamentals (data structures, algorithms, concurrency)\n• Strong debugging, profiling, and performance-tuning skills\n• Comfortable working in a Linux environment and familiar with system-level programming\n• Ability to work independently and drive projects from idea to production\n• Effective communication and collaboration skills in a high-stakes, fast-moving environment\n\nNice to Have\n• Experience building low-latency, high-throughput systems, preferably in a trading environment\n• Experience with market data feeds, exchange connectivity, or order management systems\n• Familiarity with scripting languages (Python, Bash) for tooling and automation\n• Background in finance, quantitative systems, or high-frequency trading\n• Knowledge of networking (TCP/UDP, kernel bypass, packet capture)\n• Exposure to FPGA acceleration, GPU computing, or other hardware optimizations\n\nWhy Join Us\n• Competitive compensation with performance-based bonuses\n• Cutting-edge technology and infrastructure\n• Flat organizational structure and direct impact on trading results\n• Collaborative, intellectually rigorous environment\n• Strong focus on mentorship, autonomy, and growth\n\nThe base salary range for this position is listed below. Base salary represents just one part of overall compensation; all full-time, permanent roles are eligible for a discretionary bonus and benefits, such as paid leave and insurance.\n\nThe pay range for this role is:\n130,000 - 185,000 USD per year(Edgehog - Primary Office)",
            "job_is_remote": False,
            "job_posted_at": None,
            "job_posted_at_timestamp": None,
            "job_posted_at_datetime_utc": None,
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "health_insurance",
                "paid_time_off"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DqxpNhUunuUN810mdAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_min_salary": 130000,
            "job_max_salary": 185000,
            "job_salary_period": "YEAR",
            "job_highlights": {
                "Qualifications": [
                "Strong proficiency in modern C++ (C++17 and above)",
                "Deep understanding of computer science fundamentals (data structures, algorithms, concurrency)",
                "Strong debugging, profiling, and performance-tuning skills",
                "Comfortable working in a Linux environment and familiar with system-level programming",
                "Ability to work independently and drive projects from idea to production",
                "Effective communication and collaboration skills in a high-stakes, fast-moving environment",
                "Experience building low-latency, high-throughput systems, preferably in a trading environment",
                "Experience with market data feeds, exchange connectivity, or order management systems",
                "Familiarity with scripting languages (Python, Bash) for tooling and automation",
                "Background in finance, quantitative systems, or high-frequency trading",
                "Knowledge of networking (TCP/UDP, kernel bypass, packet capture)",
                "Exposure to FPGA acceleration, GPU computing, or other hardware optimizations",
                "Collaborative, intellectually rigorous environment"
                ],
                "Benefits": [
                "Competitive compensation with performance-based bonuses",
                "Cutting-edge technology and infrastructure",
                "Flat organizational structure and direct impact on trading results",
                "Strong focus on mentorship, autonomy, and growth",
                "The base salary range for this position is listed below",
                "Base salary represents just one part of overall compensation; all full-time, permanent roles are eligible for a discretionary bonus and benefits, such as paid leave and insurance",
                "130,000 - 185,000 USD per year(Edgehog - Primary Office)"
                ],
                "Responsibilities": [
                "You’ll play a critical role in building and maintaining the systems responsible for executing our trading strategies with speed and precision",
                "Your work will directly impact our ability to respond to market opportunities in real time",
                "Design, implement, and maintain low-latency C++ applications for trading strategy execution",
                "Collaborate closely with traders, quants, and other engineers to translate strategies into robust, production-ready systems",
                "Optimize performance at every level: networking, OS, compiler, and code",
                "Contribute to system architecture, instrumentation, and deployment pipelines",
                "Debug, monitor, and improve systems operating under real-world conditions"
                ]
            },
            "job_onet_soc": "41303100",
            "job_onet_job_zone": "3"
            },
            {
            "job_id": "-pBD9bz37FFRzq6YAAAAAA==",
            "job_title": "Full Stack Python Developer - Independent Visa - Remote",
            "employer_name": "Global Business Ser. 4u",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz7XcQ62M9fya_J1XLJ9TJ4e4G4QgQa7zdQMLu&s=0",
            "employer_website": None,
            "job_publisher": "LinkedIn",
            "job_employment_type": "Contractor",
            "job_employment_types": [
                "CONTRACTOR"
            ],
            "job_apply_link": "https://www.linkedin.com/jobs/view/full-stack-python-developer-independent-visa-remote-at-global-business-ser-4u-4344405005?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/full-stack-python-developer-independent-visa-remote-at-global-business-ser-4u-4344405005?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Title : full Stack Python Developer\n\nLocation : Remote (Must have GCP/ML/AI)\n\nPosition: Contract ( Independest Visa )\n\nPython full-stack engineer with strong hands-on experience in data engineering, data pipelines, automation, and AI/ML-driven solutions. She has deep expertise in Python, Django, FastAPI, and REST APIs, combined with strong data processing and analytics capabilities using Pandas, PySpark, and SQL.\n\nShe has built and maintained large-scale data pipelines and ETL workflows, processing millions to terabytes of data using PySpark, Airflow, and cloud-native services. Her experience includes data automation, validation, orchestration, and performance optimization in enterprise environments.\n\nHas worked across cloud platforms, including GCP (BigQuery, Cloud Storage) and AWS, supporting analytics, reporting, and data-driven applications. She also brings practical AI/ML exposure, including model integration, NLP-based data processing, anomaly detection, and AI-enabled microservices.\n\nBest Regards\n\nVIK\n\nAccount Manager\n\nGlobal Business Ser 4u Inc.\n\nEmail: Vik@gbs4u.com\n\nWeb: www.gbs4u.com\n\nUSA: 1755 Park Street, Suite 200, Naperville, IL 60563\n\nINDIA: City Vista Tower A, 4th Floor, Suite – A-408 Fountain Road, Kharadi,\n\nPune, Maharashtra – 411014\n\nwww.Zinterview.AI, powered by GBS4u, is an AI-driven candidate screening and evaluation platform. We use in-house models and rigorous validation to ensure submissions meet high quality benchmarks, delivering reliable, efficient, and unbiased assessments that enable data-driven hiring decisions.\n\nZINTERVIEW.AI Transform Hiring Process wt Zinterview.AI | Smarter, Faster, & Unbiased recruitme…",
            "job_is_remote": False,
            "job_posted_at": "6 days ago",
            "job_posted_at_timestamp": 1765929600,
            "job_posted_at_datetime_utc": "2025-12-17T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": None,
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D-pBD9bz37FFRzq6YAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "Location : Remote (Must have GCP/ML/AI)",
                "Python full-stack engineer with strong hands-on experience in data engineering, data pipelines, automation, and AI/ML-driven solutions",
                "She has deep expertise in Python, Django, FastAPI, and REST APIs, combined with strong data processing and analytics capabilities using Pandas, PySpark, and SQL",
                "She has built and maintained large-scale data pipelines and ETL workflows, processing millions to terabytes of data using PySpark, Airflow, and cloud-native services"
                ],
                "Responsibilities": [
                "Her experience includes data automation, validation, orchestration, and performance optimization in enterprise environments",
                "Has worked across cloud platforms, including GCP (BigQuery, Cloud Storage) and AWS, supporting analytics, reporting, and data-driven applications",
                "She also brings practical AI/ML exposure, including model integration, NLP-based data processing, anomaly detection, and AI-enabled microservices"
                ]
            },
            "job_onet_soc": "15113300",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "V9BIUoXzJOOuhgNtAAAAAA==",
            "job_title": "Sr Software Engineer, Web SDK",
            "employer_name": "PayPal",
            "employer_logo": None,
            "employer_website": None,
            "job_publisher": "ZipRecruiter",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://www.ziprecruiter.com/c/PayPal/Job/Sr-Software-Engineer,-Web-SDK/-in-Chicago,IL?jid=9025485e00052e7a&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": True,
            "apply_options": [
                {
                "publisher": "ZipRecruiter",
                "apply_link": "https://www.ziprecruiter.com/c/PayPal/Job/Sr-Software-Engineer,-Web-SDK/-in-Chicago,IL?jid=9025485e00052e7a&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "Built In Chicago",
                "apply_link": "https://www.builtinchicago.org/job/sr-software-engineer-web-sdk/8039289?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Built In Austin",
                "apply_link": "https://www.builtinaustin.com/job/sr-software-engineer-web-sdk/8039289?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "SimplyHired",
                "apply_link": "https://www.simplyhired.com/job/TgFs5adxmOaBWIydMMZBDlvo1S6YhQ9BQ4UYPAB4s3Mhsa1Dhx9lsQ?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Indeed",
                "apply_link": "https://www.indeed.com/viewjob?jk=32865f1c8eacbab4&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JobzMall",
                "apply_link": "https://www.jobzmall.com/gusto/job/sr-staff-software-engineer-hr-apps-ausg7xz0l4?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": True
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/sr-software-engineer-web-sdk-at-paypal-4350334704?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "AnitaB.org Job Board",
                "apply_link": "https://jobs.anitab.org/companies/paypal/jobs/63922329-sr-software-engineer-web-sdk?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "The Company\n\nPayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personalized, and secure, PayPal empowers consumers and businesses in approximately 200 markets to join and thrive in the global economy.\n\nWe operate a global, two-sided network at scale that connects hundreds of millions of merchants and consumers. We help merchants and consumers connect, transact, and complete payments, whether they are online or in person. PayPal is more than a connection to third-party payment networks. We provide proprietary payment solutions accepted by merchants that enable the completion of payments on our platform on behalf of our customers.\n\nWe offer our customers the flexibility to use their accounts to purchase and receive payments for goods and services, as well as the ability to transfer and withdraw funds. We enable consumers to exchange funds more safely with merchants using a variety of funding sources, which may include a bank account, a PayPal or Venmo account balance, PayPal and Venmo branded credit products, a credit card, a debit card, certain cryptocurrencies, or other stored value products such as gift cards, and eligible credit card rewards. Our PayPal, Venmo, and Xoom products also make it safer and simpler for friends and family to transfer funds to each other. We offer merchants an end-to-end payments solution that provides authorization and settlement capabilities, as well as instant access to funds and payouts. We also help merchants connect with their customers, process exchanges and returns, and manage risk. We enable consumers to engage in cross-border shopping and merchants to extend their global reach while reducing the complexity and friction involved in enabling cross-border trade.\n\nOur beliefs are the foundation for how we conduct business every day. We live each day guided by our core values of Inclusion, Innovation, Collaboration, and Wellness. Together, our values ensure that we work together as one global team with our customers at the center of everything we do - and they push us to ensure we take care of ourselves, each other, and our communities.\n\nJob Summary:\nJob Summary\nAs part of PayPal's Braintree Web SDK team, we are looking for a talented and motivated engineer to contribute to delivering innovative and scalable solutions in the payments ecosystem. Your expertise will be key in creating exceptional developer experiences, driving technical excellence, and supporting merchants worldwide in accepting payments seamlessly on their apps and websites.\n\nJob Description:\n\nEssential Responsibilities:\n• Delivers complete solutions spanning all phases of the Software Development Lifecycle (SDLC) (design, implementation, testing, delivery and operations), based on definitions from more senior roles.\n• Advises immediate management on project-level issues\n• Guides junior engineers\n• Operates with little day-to-day supervision, making technical decisions based on knowledge of internal conventions and industry best practices\n• Applies knowledge of technical best practices in making decisions\n\nExpected Qualifications:\n• 3+ years relevant experience and a Bachelor's degree OR Any equivalent combination of education and experience.\n\nAdditional Responsibilities & Preferred Qualifications:\n\nWhat You'll Do\n• Collaborate within a high-performing team of 7-9 experienced U.S.-based engineers.\n• Deliver high-quality, scalable solutions while engaging closely with external developer communities.\n• Set clear goals, define project requirements, and manage priorities alongside cross-functional teams.\n• Implement best practices, promote technical standards, and continually enhance the SDK developer experience.\n• Lead the development of cutting-edge payment features and support the evolution of our developer tools.\n• Be an advocate for developers, working to understand their needs and provide innovative solutions through tutorials, blogs, and public speaking opportunities.\n• Contribute directly to reinventing online payments and building tools that set the standard in e-commerce innovation.\n\nMeet the Team\n• Open-Source Development: Many of our SDKs are hosted on public GitHub repositories, and we actively maintain open-source projects.\n• Impactful Engineering: We build and maintain Braintree's SDKsthe primary gateway for merchants to integrate payment solutions into their websites and mobile apps.\n• Innovation: We design and launch new payment methods, making transactions more accessible and effortless.\n• Developer Tools: Our easy-to-use supplement tools enhance SDK integrations and foster seamless implementation.\n• Community Engagement: We work with external developers by participating in events, creating educational resources like tutorials and blogs, and speaking at industry conferences to elevate the developer experience.\n\nWhat We're Looking For\n\nBasic Qualifications\n• At least 4 years of hands-on web development experience.\n• 2+ years of experience working in a large-scale organization.\n• Proven leadership skills with a passion for mentoring and nurturing engineering talent.\n• Proficiency in building applications using JavaScript and TypeScript.\n• Experience designing and developing developer-facing products (e.g., SDKs, REST APIs, GraphQL).\n\nPreferred Qualifications (Nice to Have)\n• Familiarity with payment processing, e-commerce, or financial technology is a strong plus.\n\nSubsidiary:\nPayPal\n\nTravel Percent:\n0\n\n-\n\nPayPal is committed to fair and equitable compensation practices.\n\nActual Compensation is based on various factors including but not limited to work location, and relevant skills and experience.\n\nThe total compensation for this practice may include an annual performance bonus (or other incentive compensation, as applicable), equity, and medical, dental, vision, and other benefits. For more information, visit https://www.paypalbenefits.com.\nThe US national annual pay range for this role is $123,500 to $212,850\n\nPayPal does not charge candidates any fees for courses, applications, resume reviews, interviews, background checks, or onboarding. Any such request is a red flag and likely part of a scam. To learn more about how to identify and avoid recruitment fraud please visit https://careers.pypl.com/contact-us.\n\nFor the majority of employees, PayPal's balanced hybrid work model offers 3 days in the office for effective in-person collaboration and 2 days at your choice of either the PayPal office or your home workspace, ensuring that you equally have the benefits and conveniences of both locations.\n\nOur Benefits:\n\nAt PayPal, we're committed to building an equitable and inclusive global economy. And we can't do this without our most important asset-you. That's why we offer benefits to help you thrive in every stage of life. We champion your financial, physical, and mental health by offering valuable benefits and resources to help you care for the whole you.\n\nWe have great benefits including a flexible work environment, employee shares options, health and life insurance and more. To learn more about our benefits please visithttps://www.paypalbenefits.com.\n\nWho We Are:\n\nClick Here to learn more about our culture and community.\n\nCommitment to Diversity and Inclusion\n\nPayPal provides equal employment opportunity (EEO) to all persons regardless of age, color, national origin, citizenship status, physical or mental disability, race, religion, creed, gender, sex, pregnancy, sexual orientation, gender identity and/or expression, genetic information, marital status, status with regard to public assistance, veteran status, or any other characteristic protected by federal, state, or local law. In addition, PayPal will provide reasonable accommodations for qualified individuals with disabilities. If you are unable to submit an application because of incompatible assistive technology or a disability, please contact us at paypalglobaltalentacquisition@paypal.com.\n\nBelonging at PayPal:\n\nOur employees are central to advancing our mission, and we strive to create an environment where everyone can do their best work with a sense of purpose and belonging. Belonging at PayPal means creating a workplace with a sense of acceptance and security where all employees feel included and valued. We are proud to have a diverse workforce reflective of the merchants, consumers, and communities that we serve, and we continue to take tangible actions to cultivate inclusivity and belonging at PayPal.\n\nAny general requests for consideration of your skills, please Join our Talent Community.\n\nWe know the confidence gap and imposter syndrome can get in the way of meeting spectacular candidates. Please don't hesitate to apply.",
            "job_is_remote": False,
            "job_posted_at": "4 days ago",
            "job_posted_at_timestamp": 1766102400,
            "job_posted_at_datetime_utc": "2025-12-19T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "health_insurance",
                "dental_coverage"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DV9BIUoXzJOOuhgNtAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "3+ years relevant experience and a Bachelor's degree OR Any equivalent combination of education and experience",
                "At least 4 years of hands-on web development experience",
                "2+ years of experience working in a large-scale organization",
                "Proven leadership skills with a passion for mentoring and nurturing engineering talent",
                "Proficiency in building applications using JavaScript and TypeScript",
                "Experience designing and developing developer-facing products (e.g., SDKs, REST APIs, GraphQL)"
                ],
                "Benefits": [
                "PayPal is committed to fair and equitable compensation practices",
                "Actual Compensation is based on various factors including but not limited to work location, and relevant skills and experience",
                "The total compensation for this practice may include an annual performance bonus (or other incentive compensation, as applicable), equity, and medical, dental, vision, and other benefits",
                "The US national annual pay range for this role is $123,500 to $212,850",
                "We champion your financial, physical, and mental health by offering valuable benefits and resources to help you care for the whole you",
                "We have great benefits including a flexible work environment, employee shares options, health and life insurance and more"
                ],
                "Responsibilities": [
                "We offer our customers the flexibility to use their accounts to purchase and receive payments for goods and services, as well as the ability to transfer and withdraw funds",
                "We enable consumers to exchange funds more safely with merchants using a variety of funding sources, which may include a bank account, a PayPal or Venmo account balance, PayPal and Venmo branded credit products, a credit card, a debit card, certain cryptocurrencies, or other stored value products such as gift cards, and eligible credit card rewards",
                "We also help merchants connect with their customers, process exchanges and returns, and manage risk",
                "We enable consumers to engage in cross-border shopping and merchants to extend their global reach while reducing the complexity and friction involved in enabling cross-border trade",
                "Your expertise will be key in creating exceptional developer experiences, driving technical excellence, and supporting merchants worldwide in accepting payments seamlessly on their apps and websites",
                "Delivers complete solutions spanning all phases of the Software Development Lifecycle (SDLC) (design, implementation, testing, delivery and operations), based on definitions from more senior roles",
                "Advises immediate management on project-level issues",
                "Guides junior engineers",
                "Operates with little day-to-day supervision, making technical decisions based on knowledge of internal conventions and industry best practices",
                "Applies knowledge of technical best practices in making decisions",
                "Collaborate within a high-performing team of 7-9 experienced U.S.-based engineers",
                "Deliver high-quality, scalable solutions while engaging closely with external developer communities",
                "Set clear goals, define project requirements, and manage priorities alongside cross-functional teams",
                "Implement best practices, promote technical standards, and continually enhance the SDK developer experience",
                "Lead the development of cutting-edge payment features and support the evolution of our developer tools",
                "Be an advocate for developers, working to understand their needs and provide innovative solutions through tutorials, blogs, and public speaking opportunities",
                "Contribute directly to reinventing online payments and building tools that set the standard in e-commerce innovation",
                "Open-Source Development: Many of our SDKs are hosted on public GitHub repositories, and we actively maintain open-source projects",
                "Impactful Engineering: We build and maintain Braintree's SDKsthe primary gateway for merchants to integrate payment solutions into their websites and mobile apps",
                "Innovation: We design and launch new payment methods, making transactions more accessible and effortless",
                "Developer Tools: Our easy-to-use supplement tools enhance SDK integrations and foster seamless implementation",
                "Community Engagement: We work with external developers by participating in events, creating educational resources like tutorials and blogs, and speaking at industry conferences to elevate the developer experience"
                ]
            },
            "job_onet_soc": "15113200",
            "job_onet_job_zone": "4"
            },
            {
            "job_id": "8zWD0FV_9giZtFbZAAAAAA==",
            "job_title": "Developer Node.js/AWS  - Information Technology",
            "employer_name": "United Airlines",
            "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DMswunk7F25_BeXSf2w8JVHG65s4lc7v5wfG&s=0",
            "employer_website": "https://www.united.com",
            "job_publisher": "United Airlines Jobs",
            "job_employment_type": "Full-time",
            "job_employment_types": [
                "FULLTIME"
            ],
            "job_apply_link": "https://careers.united.com/us/en/job/WHQ00025801/Developer-Node-js-AWS-Information-Technology?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "job_apply_is_direct": False,
            "apply_options": [
                {
                "publisher": "United Airlines Jobs",
                "apply_link": "https://careers.united.com/us/en/job/WHQ00025801/Developer-Node-js-AWS-Information-Technology?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JSfirm.com",
                "apply_link": "https://www.jsfirm.com/Other/Developer+Nodejs/AWS++-+Information+Technology/Chicago-Illinois/jobID_1769858?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "LinkedIn",
                "apply_link": "https://www.linkedin.com/jobs/view/developer-node-js-aws-information-technology-at-united-airlines-4335597612?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "JobGet",
                "apply_link": "https://www.jobget.com/jobs/job/8d937421-0075-4ac3-be36-1c4a57bf7804?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "Snagajob",
                "apply_link": "https://www.snagajob.com/jobs/1186017407?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                },
                {
                "publisher": "AirlineJobs.com",
                "apply_link": "https://airlinejobs.com/jobs/183285907-developer-node-js-aws-information-technology?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                "is_direct": False
                }
            ],
            "job_description": "Achieving our goals starts with supporting yours. Grow your career, access top-tier health and wellness benefits, build lasting connections with your team and our customers, and travel the world using our extensive route network.\n\nCome join us to create what’s next. Let’s define tomorrow, together.\n\nDescription\n\nThe Developer plays a vital role in creating and maintaining the strategic partnership between business needs and technology delivery. The Developer plans, designs, develops, and launches efficient systems and solutions supporting core organizational functions. This individual will utilize effective communication, analytical, and problem-solving skills to help identify, communicate/resolve issues, opportunities, or problems to maximize the benefit of IT and Business investments.\n\n· Writes code and develops software applications and tools using agile development methodologies. Designs, develops, and modifies software applications/systems that meet specifications. Provides support to the software development leads (Ex, Senior Developer)\n\n· Helps partner and collaborates with cross-functional teams to understand business requirements and deliver solutions. Participates in the design, architecture, and build phases aimed at producing high-quality deliverables. Assists in contributing to software documentation and user manuals\n\n· Complete comprehensive unit testing and debugging on all developed/enhanced software and support the deployment of software applications. Participates in code reviews to ensure code adheres to standards. Use design principles and product specifications to enhance software continuously\n\n· Demonstrates working knowledge of all core and common programming languages critical to the organization. Demonstrates technical proficiency in areas critical to the specific team/application. Applies security code best practices throughout the development cycle\n\n· Support and troubleshoot software systems as required, optimizing performance, resolving problems, and providing follow-up on all issues and solutions\n\n· Works on problems of moderate scope where analysis of situations or data requires a review of multiple considerations. Exercises judgment within defined procedures and practices to determine appropriate action\n\n· Receives general instructions on routine work and detailed instructions on new projects or assignments. Usually works with some supervision, working with the leader on unusual or complex matters\nQualifications\n\nRequired Skills:\n\n· Bachelor's degree in Computer Science, Engineering, Mathematics or related field\n\n· 3+ Experience with Cloud Automation Development Tool such as Git, Python/Bash/PowerShell Scripting\n\n· Hands-on development and proficient excellence in backend API development using Node.js Java and Python\n\n· Proficient in a coding language and building back-end components\n\n· Problem solving\n\n· Demonstrate advanced knowledge of SDLC processes inputs/outputs, standards and best practice\n\n· Demonstrate advanced knowledge of development methodologies, software design, and design patterns\n\n· Demonstrate advanced knowledge of the application of development domain areas and specific technologies and tool sets\n\nPreferred Experience:\n\n· AWS highly preferred\n\n· Dev Ops highly Experience\n\n· Exposure to APPD & Dynatrace\n\n· Agile Methodologies\n\n· .Net, C, C++, C#, Java · HTML, Java Script (Angular 2.0, JS), CSS\n\n· SQL, Oracle Experience, Relational DB Experience\n\n· Code Repositories like TFS\n\n· Chef/Ansible, Configuration tools\n\n· Continuous Integration & Continuous Deployment\n\n· Exposure to Couchbase NoSQL DB\n\nThe base pay range for this role is $87,780.00 to $114,376.00.\nThe base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills. This position is also eligible for bonus and/or long-term incentive compensation awards.\n\nYou may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges.\n\nUnited Airlines is an equal opportunity employer. United Airlines recruits, employs, trains, compensates and promotes regardless of race, religion, color, national origin, gender identity, sexual orientation, physical ability, age, veteran status and other protected status as required by applicable law. Equal Opportunity Employer - Minorities/Women/Veterans/Disabled/LGBT.\n\nWe will ensure that individuals with disabilities are provided reasonable accommodation to participate in the job application or interview process, to perform crucial job functions. Please contact JobAccommodations@united.com to request accommodation.",
            "job_is_remote": False,
            "job_posted_at": "2 days ago",
            "job_posted_at_timestamp": 1766275200,
            "job_posted_at_datetime_utc": "2025-12-21T00:00:00.000Z",
            "job_location": "Chicago, IL",
            "job_city": "Chicago",
            "job_state": "Illinois",
            "job_country": "US",
            "job_latitude": 41.88325,
            "job_longitude": -87.6323879,
            "job_benefits": [
                "dental_coverage",
                "paid_time_off",
                "health_insurance"
            ],
            "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D8zWD0FV_9giZtFbZAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            "job_salary": None,
            "job_min_salary": None,
            "job_max_salary": None,
            "job_salary_period": None,
            "job_highlights": {
                "Qualifications": [
                "Bachelor's degree in Computer Science, Engineering, Mathematics or related field",
                "3+ Experience with Cloud Automation Development Tool such as Git, Python/Bash/PowerShell Scripting",
                "Hands-on development and proficient excellence in backend API development using Node.js Java and Python",
                "Proficient in a coding language and building back-end components",
                "Problem solving",
                "Demonstrate advanced knowledge of SDLC processes inputs/outputs, standards and best practice",
                "Demonstrate advanced knowledge of development methodologies, software design, and design patterns",
                "Demonstrate advanced knowledge of the application of development domain areas and specific technologies and tool sets"
                ],
                "Benefits": [
                "The base pay range for this role is $87,780.00 to $114,376.00",
                "The base salary range/hourly rate listed is dependent on job-related, factors such as experience, education, and skills",
                "This position is also eligible for bonus and/or long-term incentive compensation awards",
                "You may be eligible for the following competitive benefits: medical, dental, vision, life, accident & disability, parental leave, employee assistance program, commuter, paid holidays, paid time off, 401(k) and flight privileges"
                ],
                "Responsibilities": [
                "The Developer plays a vital role in creating and maintaining the strategic partnership between business needs and technology delivery",
                "The Developer plans, designs, develops, and launches efficient systems and solutions supporting core organizational functions",
                "This individual will utilize effective communication, analytical, and problem-solving skills to help identify, communicate/resolve issues, opportunities, or problems to maximize the benefit of IT and Business investments",
                "Writes code and develops software applications and tools using agile development methodologies",
                "Designs, develops, and modifies software applications/systems that meet specifications",
                "Provides support to the software development leads (Ex, Senior Developer)",
                "Helps partner and collaborates with cross-functional teams to understand business requirements and deliver solutions",
                "Participates in the design, architecture, and build phases aimed at producing high-quality deliverables",
                "Assists in contributing to software documentation and user manuals",
                "Complete comprehensive unit testing and debugging on all developed/enhanced software and support the deployment of software applications",
                "Participates in code reviews to ensure code adheres to standards",
                "Use design principles and product specifications to enhance software continuously",
                "Demonstrates working knowledge of all core and common programming languages critical to the organization",
                "Demonstrates technical proficiency in areas critical to the specific team/application",
                "Applies security code best practices throughout the development cycle",
                "Support and troubleshoot software systems as required, optimizing performance, resolving problems, and providing follow-up on all issues and solutions",
                "Works on problems of moderate scope where analysis of situations or data requires a review of multiple considerations",
                "Exercises judgment within defined procedures and practices to determine appropriate action",
                "Receives general instructions on routine work and detailed instructions on new projects or assignments",
                "Usually works with some supervision, working with the leader on unusual or complex matters"
                ]
            },
            "job_onet_soc": "15113400",
            "job_onet_job_zone": "3"
            }
        ]
        }

    def __init__(
        self, 
        role: str,
        uk_locations: Optional[List[str]],
        date_posted: Optional[str],
        off_site: Optional[bool],
        employment_types: Optional[List[str]]
    ):
        """Initialize JobListingsApi instance.

        Args:
            role (str): Job role or keyword to search for.
            uk_locations (Optional[List[str]]): List of UK city names, or None 
                if no location filter is applied.
            date_posted (Optional[str]): Date filter for job postings, or None 
                if no date filter is applied.
            off_site (Optional[bool]): Boolean flag to filter for remote/hybrid 
                positions, or None if no off_site filter is applied.
            employment_types (Optional[List[str]]): List of employment types 
                to filter by, or None if no employment_types filter is applied.
        """

        self.role = role
        self.uk_locations = uk_locations
        self.date_posted = date_posted
        self.off_site = off_site
        self.employment_types = employment_types

        self.api_key = os.getenv("OPEN_WEB_NINJA_API_KEY")
        self.conn = http.client.HTTPSConnection("api.openwebninja.com")
    
    def run(self) -> UserJobSearchResponses:
        """Main orchestration workflow method. (Alter when return type is found).

        Returns:
            UserJobSearchResponses: List of the schema for the parsed job
                search response.
        """

        uk_locs = [None] if self.uk_locations == [] else self.uk_locations
        emp_types = [None] if self.employment_types == [] else self.employment_types

        job_listings = []
        query_list = []

        for uk_loc in uk_locs:
            for emp_type in emp_types:
                param_url, params = self.parse_params(uk_loc, emp_type)
                # retrieved_data = self.retrieve_own_data(param_url)
                # own_data = json.loads(retrieved_data)
                job_listing = self.parse_job_listing(self.EXAMPLE_RESPONSE)
                response = UserJobSearchResponse(root=job_listing)

                job_listings.append(response)
                query_list.append(params["query"])
    
        parsed_params = {
            "query": query_list,
            "country": "uk",
            "date_posted": self.date_posted,
            "off_site": self.off_site
        }

        if emp_types[0] is not None:
            parsed_params["employment_types"] = emp_types
        else:
            parsed_params["employment_types"] = None
        
        job_search_response = {
            "parameters": Parameters(**parsed_params),
            "job_listings": job_listings
        }
        
        return UserJobSearchResponses(**job_search_response)

    def retrieve_own_data(self, params: str) -> str:
        """Retrieves job listings.

        Args:
            params (str): Contains parsed parameters.

        Returns:
            str: Returns job listings in string representation.
        """

        headers = {
            "x-api-key": self.api_key
        }

        endpoint = f"/jsearch/search{params}"
        self.conn.request("GET", endpoint, headers=headers)
        res = self.conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    
    def parse_params(self, 
        loc: Optional[str], 
        emp_type: Optional[str]) -> Tuple[str, Dict[str, Any]]:
        """Parses retrieved query parameters from frontend.

        Params:
            loc (Optional[str]): Contains UK location, or None
                if no location filter is applied.
            emp_type (Optional[str]): Contains employment type, or
                None if not employment type filter is applied.

        Returns:
            Tuple[str, Dict[str, Any]]: Returns parsed query parameters.
        """

        query = f"{self.role} roles in the United Kingdom"
        params = {"query": query, "country": "uk"}

        if loc is not None:
            params["query"] = f"{self.role} roles in {loc}."

        if self.date_posted:
            params["date_posted"] = self.date_posted

        if self.off_site is not None:
            params["off_site"] = str(self.off_site).lower()

        if self.employment_types is not None:
            params["employment_types"] = emp_type

        

        return f"?{urlencode(params)}", params
    
    def parse_apply_options(self, 
        job: Dict[str, Dict]) -> List[ApplyOption]:
        """Populates a list of ApplyOption schemas.

        Args:
            job (Dict[str, Dict]): Retrieved data from OpenWebNinja API.
        
        Returns:
            List[ApplyOption]: List of the schema for parsed apply
                options data.
        """

        apply_options = []
        for app_opts in job["apply_options"]:
            app_opt_vals = {
                "publisher": app_opts.get("publisher"),
                "apply_link": app_opts.get("apply_link"),
                "is_direct": app_opts.get("is_direct")
            }

            apply_options.append(ApplyOption(**app_opt_vals))
        
        return apply_options
    
    def parse_job_highlights(self,
        job: Dict[str, Any]) -> JobHighlights:
        """Populates a JobHighlights schemas.

        Args:
            job (Dict[str, Any]): Retrieved data from OpenWebNinja API.
        
        Returns:
            JobHighlights: The schema for parsed job highlights
                data.
        """

        job_high = job["job_highlights"]
        job_high_vals = {
            "Qualifications": job_high.get("Qualifications"),
            "Responsibilites": job_high.get("Responsibilities"),
            "Benefits": job.get("job_benefits")
        }
        
        return JobHighlights(**job_high_vals)
    

    def parse_job_listing(self, 
        own_data: Dict[str, Dict]) -> List[UserJobListing]:
        """Populates a list of UserJobListing schemas.

        Args:
            own_data (Dict[str, Dict]): Retrieved data from OpenWebNinja API.
        
        Returns:
            List[UserJobListing]: List of the schema for parsed 
                job listing data.
        """

        job_listings = []
        for job in own_data["data"]:
            apply_options = self.parse_apply_options(job)
            job_highlight = self.parse_job_highlights(job)
            jl_values = {
                "job_id": job.get("job_id"),
                "job_title": job.get("job_title"),
                "employer_name": job.get("employer_name"),
                "employer_logo": job.get("employer_logo"),
                "employer_website": job.get("employer_website"),
                "job_location": job.get("job_location"),
                "job_city": job.get("job_city"),
                "job_state": job.get("job_state"),
                "job_country": job.get("job_country"),
                "job_is_remote": job.get("job_is_remote"),
                "job_employment_type": job.get("job_employment_type"),
                "job_employment_types": job.get("job_employment_types"),
                "job_posted_at": job.get("job_posted_at"),
                "job_posted_at_timestamp": job.get("job_posted_at_timestamp"),
                "job_posted_at_datetime_utc": job.get("job_posted_at_datetime_utc"),
                "job_salary": job.get("job_salary"),
                "job_min_salary": job.get("job_min_salary"),
                "job_max_salary": job.get("job_max_salary"),
                "job_salary_period": job.get("job_salary_period"),
                "job_apply_link": job.get("job_apply_link"),
                "job_apply_is_direct": job.get("job_apply_is_direct"),
                "apply_options": apply_options,
                "job_description": job.get("job_description"),
                "job_highlights": job_highlight,
                "job_benefits": job.get("job_benefits"),
                "job_publisher": job.get("job_publisher"),
            }

            job_listings.append(UserJobListing(**jl_values))

        return job_listings

        

