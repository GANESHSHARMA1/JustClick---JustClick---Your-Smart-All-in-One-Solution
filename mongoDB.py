from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<Username>:<Password>@justclick.ps3ayrm.mongodb.net/?appName=JustClick"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['ATS']
collection = db['Job_desc']

# Documents to insert
documents = [
    {"job_role": "Software Developer",
      "job_desc": """
Job Description: Software Developer

Job Overview:
We are seeking a highly skilled Software Developer to join our dynamic team. The ideal candidate will be responsible for designing, developing, and maintaining software applications that meet the needs of our users. You will work closely with other developers, product managers, and designers to ensure the delivery of high-quality software products.

Key Responsibilities:
- *Design and Development*: Write clean, maintainable, and efficient code based on specifications.
- *Testing and Debugging*: Test and debug software to ensure reliability and performance.
- *Collaboration*: Work with cross-functional teams to define, design, and ship new features.
- *Maintenance*: Maintain existing software applications by making modifications as required.
- *Documentation*: Create and maintain software documentation for future reference.
- *Code Review*: Participate in code reviews to ensure code quality and adherence to best practices.
- *Problem-Solving*: Identify bottlenecks and bugs, and devise solutions to mitigate these issues.
- *Learning and Development*: Stay updated with the latest industry trends and technologies to ensure continuous improvement.

Requirements:
- *Education*: Bachelor’s degree in Computer Science, Software Engineering, or a related field.
- *Experience*: Experience in software development (internships, projects, or previous jobs).
- *Technical Skills*:
  - Proficiency in programming languages such as Java, Python, C++, or similar.
  - Familiarity with web development technologies (HTML, CSS, JavaScript) is a plus.
  - Experience with version control systems like Git.
  - Knowledge of databases and SQL.
- *Soft Skills*:
  - Strong problem-solving skills.
  - Excellent communication and teamwork abilities.
  - Attention to detail and a proactive attitude.

Preferred Qualifications:
- Experience with agile development methodologies.
- Knowledge of software development frameworks and tools.
- Experience with cloud platforms (AWS, Azure, Google Cloud) is a plus.
- Contributions to open-source projects or a strong GitHub profile.

Benefits:
- Competitive salary and performance-based bonuses.
- Comprehensive health insurance.
- Professional development opportunities.
- Flexible working hours and remote work options.
- Friendly and collaborative work environment.

Join us to be a part of a team where your skills and creativity can make a significant impact on the success of our projects. We look forward to your application!
        """
      },
      {"job_role": "Web Developer",
        "job_desc":"""

    Job Description:
    We are looking for a talented Full Stack Web Developer to join our team. The ideal candidate will have experience in both front-end and back-end development, with a strong understanding of web technologies and best practices. You will be responsible for building and maintaining web applications, ensuring high performance and responsiveness.

    Key Responsibilities:
    - Design, develop, and maintain web applications using modern technologies and frameworks.
    - Collaborate with designers and product managers to create user-friendly and visually appealing interfaces.
    - Implement and optimize back-end services and APIs to ensure seamless integration with front-end components.
    - Troubleshoot and resolve issues in a timely manner, providing ongoing support and enhancements.
    - Write clean, scalable, and maintainable code while adhering to best practices and coding standards.
    - Participate in code reviews and contribute to the continuous improvement of development processes.

    Qualifications:
    - Bachelor’s degree in Computer Science, Software Engineering, or a related field.
    - Proven experience as a Full Stack Web Developer or similar role, with a portfolio of completed projects.
    - Proficiency in front-end technologies such as HTML, CSS, and JavaScript, and frameworks like React, Angular, or Vue.js.
    - Strong experience with back-end technologies and frameworks, such as Node.js, Express, Django, or Ruby on Rails.
    - Knowledge of database systems (e.g., SQL, NoSQL) and experience with RESTful APIs and web services.
    - Familiarity with version control systems (e.g., Git) and agile development methodologies.

    Preferred Skills:
    - Experience with cloud platforms (e.g., AWS, Azure) and containerization technologies (e.g., Docker).
    - Knowledge of DevOps practices and CI/CD pipelines.
    - Ability to work in a fast-paced environment and manage multiple priorities effectively.

    Benefits:
    - Competitive salary and performance-based bonuses.
    - Comprehensive health, dental, and vision insurance.
    - Flexible work hours and remote work options.
    - Opportunities for career growth and professional development.
    - Collaborative and innovative work environment.


"""
      },
      {
    "job_role": "Data Scientist",

    "job_desc": """

    Job Description:
    We are seeking a Data Scientist with expertise in data analysis, machine learning, and statistical modeling to join our dynamic team. The ideal candidate will possess strong analytical skills and the ability to interpret complex data, develop predictive models, and derive actionable insights to drive business decisions.

    Key Responsibilities:
    - Analyze and interpret complex data sets using statistical methods and machine learning techniques.
    - Develop and implement data models to solve business problems and optimize processes.
    - Create data visualizations and reports to communicate findings and recommendations to stakeholders.
    - Collaborate with cross-functional teams to understand business needs and develop data-driven solutions.
    - Stay updated with the latest industry trends and technologies to continuously improve data practices.

    Qualifications:
    - Bachelor’s degree in Computer Science, Statistics, Mathematics, or a related field; Master’s degree preferred.
    - Proven experience as a Data Scientist or similar role, with a strong portfolio of completed projects.
    - Proficiency in programming languages such as Python, R, or SQL.
    - Experience with data visualization tools (e.g., Tableau, Power BI) and machine learning libraries (e.g., scikit-learn, TensorFlow).
    - Strong analytical and problem-solving skills with the ability to work independently and as part of a team.
    - Excellent communication skills, with the ability to explain complex data concepts to non-technical stakeholders.

    Preferred Skills:
    - Experience with big data technologies (e.g., Hadoop, Spark) is a plus.
    - Knowledge of cloud platforms (e.g., AWS, Azure) and data warehousing solutions.
    - Familiarity with Agile methodologies and project management tools.

    Benefits:
    - Competitive salary and performance-based incentives.
    - Health, dental, and vision insurance.
    - Opportunities for professional growth and development.
    - Flexible work hours and remote work options.

    """  
      },
      
      {"job_role": "Graphics designer",
      "job_desc": """
Job Description: Graphics Designer
Position: Graphics Designer
Department: Marketing/Design

Job Summary:
We are seeking a creative and talented Graphics Designer to join our team. The Graphics Designer will be responsible for creating visually appealing and impactful designs for various digital and print media. The ideal candidate should have a strong eye for detail, a good understanding of design principles, and the ability to work collaboratively with different teams.

Key Responsibilities:
Create Visual Concepts: Develop creative concepts and visual styles for marketing materials, social media posts, advertisements, and other promotional content.
Design Collateral: Design brochures, flyers, posters, banners, and other printed materials.
Digital Media: Produce graphics for websites, email campaigns, and digital advertisements.
Branding: Maintain consistency in branding and visual identity across all platforms and materials.
Collaborate: Work closely with marketing, product, and content teams to understand project requirements and deliver designs that meet business objectives.
Review and Edit: Review final designs and suggest improvements as needed. Ensure all graphics and layouts are visually appealing and align with brand standards.
Stay Updated: Keep up-to-date with industry trends, tools, and techniques to continually improve design skills and deliver cutting-edge designs.
Required Skills and Qualifications:
Education: Bachelor's degree in Graphic Design, Fine Arts, or a related field.
Experience: Proven experience as a Graphics Designer or in a similar role.
Software Proficiency: Strong proficiency in design software such as Adobe Creative Suite (Photoshop, Illustrator, InDesign), Sketch, or other relevant tools.
Creativity: Strong creative and artistic skills with a keen eye for aesthetics and details.
Communication: Excellent verbal and written communication skills.
Time Management: Ability to handle multiple projects and meet deadlines in a fast-paced environment.
Portfolio: A strong portfolio showcasing a variety of design projects and styles.
Preferred Skills:
Animation: Knowledge of animation and motion graphics software (e.g., After Effects).
UX/UI Design: Experience with user interface (UI) and user experience (UX) design.
Photography: Basic photography and photo editing skills.
Print Production: Understanding of print production processes and requirements.
Work Environment:
Team-Oriented: Ability to work effectively in a collaborative team environment.
Remote/Onsite: [Specify if the job is remote, onsite, or hybrid]
Application Process:
Interested candidates should submit their resume, cover letter, and portfolio to [email/contact information]. Applications will be reviewed on a rolling basis.
        """
      },
      {"job_role": "Systems Analyst",
      "job_desc": """
Job Description: Systems Analyst
Position Overview:
The Systems Analyst is responsible for analyzing, designing, and implementing information systems to meet business needs. This role involves working closely with stakeholders to understand their requirements, translating these into technical specifications, and ensuring that the system solutions are effectively integrated and functioning.

Key Responsibilities:

Requirements Gathering:

Work with business stakeholders to understand their needs and requirements.
Conduct interviews, workshops, and surveys to gather comprehensive requirements.
Document business processes and requirements.
System Design:

Analyze requirements to design system solutions that align with business goals.
Create detailed technical specifications and system designs.
Develop and maintain system documentation.
Implementation:

Collaborate with developers and IT teams to implement system solutions.
Oversee system configuration, customization, and integration.
Test systems to ensure they meet specified requirements and perform as expected.
Troubleshooting and Support:

Provide support for system issues, bugs, and user queries.
Diagnose and resolve technical problems related to system performance or functionality.
Implement solutions and workarounds to address system issues.
Project Management:

Participate in project planning and management activities.
Monitor project progress, manage timelines, and ensure deliverables are met.
Communicate project status and updates to stakeholders.
Continuous Improvement:

Identify opportunities for system and process improvements.
Stay updated with industry trends, technologies, and best practices.
Recommend and implement enhancements to improve system performance and user experience.
Key Skills and Qualifications:

Technical Skills:

Proficiency in system analysis tools and methodologies.
Knowledge of programming languages and database management.
Experience with system development life cycle (SDLC) methodologies.
Analytical Skills:

Strong problem-solving and analytical skills.
Ability to translate business needs into technical solutions.
Communication Skills:

Excellent written and verbal communication skills.
Ability to present complex technical information to non-technical stakeholders.
Education and Experience:

Bachelor's degree in Computer Science, Information Technology, or a related field.
Previous experience as a Systems Analyst or in a similar role is preferred.
Personal Attributes:

Detail-oriented with strong organizational skills.
Ability to work independently and as part of a team.
Adaptability to changing technologies and business requirements.
This job description provides a general overview of the responsibilities and qualifications required for the Systems Analyst role. Specific duties may vary depending on the organization and the nature of the projects.
        """
      },
      {"job_role": "Product Manager",
      "job_desc": """
General Job Description for a Product Manager
Position Title: Product Manager

Job Summary:
The Product Manager is responsible for overseeing the development, launch, and lifecycle of a product or product line. This role involves working closely with cross-functional teams to ensure the product meets customer needs and business objectives. The Product Manager manages the product roadmap, prioritizes features, and drives product strategy to achieve company goals.

Key Responsibilities:

Product Strategy and Vision:

Define the product vision and strategy in alignment with company goals.
Conduct market research and analysis to understand customer needs and competitive landscape.
Roadmap and Planning:

Develop and maintain the product roadmap, including timelines and milestones.
Prioritize features and enhancements based on customer feedback, market trends, and business needs.
Cross-Functional Collaboration:

Work with engineering, design, marketing, sales, and other teams to deliver high-quality products.
Facilitate communication and collaboration among stakeholders to ensure successful product development and launch.
Product Development:

Oversee the product development process from concept to launch.
Define product requirements, create user stories, and work with the development team to ensure timely delivery.
Customer and Market Insights:

Gather and analyze customer feedback to identify opportunities for improvement.
Monitor market trends and competitive products to inform product decisions.
Performance Tracking:

Define key performance indicators (KPIs) to measure product success.
Track and analyze product performance metrics, and adjust strategy as needed to achieve objectives.
Product Launch and Go-to-Market:

Plan and execute product launches, including coordinating with marketing and sales teams.
Develop product positioning and messaging to effectively communicate value to customers.
Continuous Improvement:

Iterate on the product based on feedback, performance data, and market changes.
Ensure ongoing product improvements and updates to maintain competitiveness.
Qualifications:

Education: Bachelor’s degree in Business, Marketing, Engineering, or a related field. MBA or relevant advanced degree is a plus.
Experience: 2-5 years of experience in product management or a related role.
Skills:
Strong understanding of product development processes and methodologies.
Excellent communication, leadership, and collaboration skills.
Ability to analyze data and make data-driven decisions.
Familiarity with market research and competitive analysis.
Proficiency in product management tools and software (e.g., JIRA, Asana).
Preferred Qualifications:

Experience in [specific industry or domain relevant to the company].
Experience with agile development methodologies.
Knowledge of user experience (UX) principles and design thinking.
Working Conditions:

Full-time position, typically office-based with potential for remote work.
May require occasional travel to meet with clients or attend industry events.
This description provides a general overview of the Product Manager role and can be tailored to fit specific company needs or industry requirements.
        """
      },
      {"job_role": "Data Analyst",
      "job_desc": """
Job Title: Data Analyst

Job Overview:
A Data Analyst is responsible for collecting, processing, and analyzing data to provide actionable insights that support business decision-making. They work closely with various departments to understand their data needs and help interpret trends, patterns, and anomalies to drive strategic decisions.

Key Responsibilities:

Data Collection: Gather data from various sources, including databases, spreadsheets, and external systems.
Data Processing: Clean, transform, and organize data to ensure accuracy and usability.
Data Analysis: Perform statistical analysis to identify trends, patterns, and correlations.
Reporting: Create and maintain reports, dashboards, and visualizations to present data insights to stakeholders.
Collaboration: Work with cross-functional teams to understand their data requirements and provide analytical support.
Problem-Solving: Identify and resolve data-related issues, ensuring data integrity and consistency.
Data Management: Maintain and update databases and data systems to ensure data is current and accurate.
Research: Stay updated on industry trends and best practices in data analysis and data management.
Qualifications:

Education: Bachelor's degree in Data Science, Statistics, Mathematics, Computer Science, or a related field.
Technical Skills: Proficiency in data analysis tools and software (e.g., Excel, SQL, Python, R), and data visualization tools (e.g., Tableau, Power BI).
Analytical Skills: Strong ability to analyze data, draw insights, and make data-driven recommendations.
Attention to Detail: High level of accuracy and attention to detail in data handling and analysis.
Communication Skills: Excellent verbal and written communication skills for presenting findings and collaborating with team members.
Problem-Solving: Strong problem-solving skills and the ability to think critically about data challenges.
Preferred Qualifications:

Experience: Previous experience in a data analyst role or relevant internships.
Certifications: Relevant certifications (e.g., Microsoft Certified Data Analyst Associate) can be advantageous.
Industry Knowledge: Familiarity with industry-specific data and business processes.
        """
      },
]


result = collection.insert_many(documents)
print(f"Inserted document IDs: {result.inserted_ids}")
