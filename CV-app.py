import streamlit as st

# Bilingual content dictionaries
content = {
    "en": {
        "title": "Curriculum Vitae - Gonzalo Cortés Leal",
        "personal_info": "📋 Personal Information",
        "name": "Gonzalo Cortés Leal",
        "contact": "Contact Information",
        "email": "Email: 0224381@up.edu.mx",
        "phone": "Phone: 3317590101",
        "linkedin": "LinkedIn: [Add your LinkedIn profile]",
        "github": "GitHub: [Add your GitHub profile]",
        "summary": "📝 Professional Summary",
        "summary_text": ("Highly motivated and ambitious recent graduate with a Bachelor's degree in Administration and Finance, complemented by international study experience in Europe. "
                         "Skilled in financial analysis, project management, and strategic planning. Demonstrated ability to analyze complex financial data, identify investment opportunities, "
                         "and develop actionable business strategies during a five-month tenure as a Project Analyst. Equipped with strong technical skills in financial modeling, data analysis, "
                         "and proficiency in financial software tools such as Excel and Bloomberg Terminal. Possesses excellent communication, problem-solving, and analytical skills. "
                         "Aspires to leverage background in finance and passion for investment to establish and grow a successful investment firm in Mexico."),
        "work_experience": "💼 Work Experience",
        "education": "🎓 Education",
        "skills": "🛠️ Skills",
        "projects": "📊 Projects",
        "certifications": "🏅 Certifications and Awards",
        "languages": "🌐 Languages",
        "interests": "🎯 Interests and Hobbies",
        "why_hire_me": "🤔 Why Hire Me?",
        "why_hire_me_text": ("I bring a strong background in finance and administration, enriched with international study experience. My technical skills in financial analysis, "
                             "project management, and strategic planning are complemented by my ability to communicate effectively and solve complex problems. My ambition to establish "
                             "an investment firm reflects my dedication and passion for the field. I am committed to driving financial success and growth through innovative and strategic initiatives."),
        "work_experience_details": [
            {
                "job_title": "Project Analyst",
                "company": "DA FIN LAB Soluciones Financieras, Guadalajara, Jalisco",
                "duration": "April 2022 – August 2022",
                "responsibilities": [
                    "Conducted comprehensive market research to identify and evaluate investment opportunities.",
                    "Developed initial investment strategies, ensuring alignment with the company's financial objectives.",
                    "Projected free cash flow to aid in financial planning and decision-making.",
                    "Formulated cost structures and set competitive sales prices to optimize profitability.",
                    "Determined the break-even point and forecasted expected demand to support business planning.",
                    "Calculated the weighted average cost of capital (WACC) to assess the cost of equity and debt.",
                    "Assigned optimal locations for new projects, considering strategic and financial factors."
                ]
            },
            {
                "job_title": "Administrative Assistant",
                "company": "Grupo AM PM, Guadalajara, Jalisco",
                "duration": "December 2017 – December 2018",
                "responsibilities": [
                    "Managed inventory and ordered office supplies to ensure smooth daily operations.",
                    "Created, issued, and canceled invoices, maintaining accurate financial records.",
                    "Updated and developed company workflows to improve efficiency.",
                    "Performed daily administrative tasks and managed accounting processes to support business functions."
                ]
            }
        ],
        "education_details": {
            "degree": "Bachelor’s in Administration and Finance",
            "institution": "Universidad Panamericana de Guadalajara",
            "graduation_year": "2024"
        },
        "skills_details": {
            "technical": [
                "Financial modeling",
                "Data analysis",
                "Proficiency in financial software tools (e.g., Excel, R Studio, Python)",
                "Investment analysis",
                "Risk management"
            ],
            "soft": [
                "Strategic planning",
                "Communication",
                "Problem-solving",
                "Analytical thinking",
                "Project management"
            ]
        },
        "projects_details": [
            {
                "name": "Stock Investment Predictor Web Page",
                "description": ("Developed a web application to determine the viability of investing in a stock using multivariable regressions and Monte Carlo forecasting."),
                "technologies": "Streamlit, Python, multivariable regression, Monte Carlo simulation",
                "link": "https://predictor-de-precios-gonzalocl.streamlit.app/"
            }
        ],
        "certifications_details": [
            {
                "name": "Python for Finance: Investment Fundamentals & Data Analytics",
                "organization": "Udemy",
                "date": "2024"
            },
            {
                "name": "High School Debate Tournament Winner",
                "description": "Two-time winner of the high school debate tournament.",
                "years": "2018-2019"
            }
        ],
        "languages_details": [
            "Spanish (Native)",
            "English (Fluent)"
        ],
        "interests_details": [
            "Extreme sports",
            "University volleyball team member",
            "Traveling",
            "Camping"
        ]
    },
    "es": {
        "title": "Curriculum Vitae - Gonzalo Cortés Leal",
        "personal_info": "📋 Información Personal",
        "name": "Gonzalo Cortés Leal",
        "contact": "Información de Contacto",
        "email": "Correo electrónico: 0224381@up.edu.mx",
        "phone": "Teléfono: 3317590101",    
        "summary": "📝 Resumen Profesional",
        "summary_text": ("Soy un reciente graduado altamente motivado y ambicioso con un título en Administración y Finanzas, complementado con experiencia de estudio internacional en Europa. "
                         "Tengo habilidades en análisis financiero, gestión de proyectos y planificación estratégica. He demostrado la capacidad de analizar datos financieros complejos, "
                         "identificar oportunidades de inversión y desarrollar estrategias comerciales accionables durante un período de cinco meses como Analista de Proyectos. Estoy equipado con sólidas habilidades técnicas "
                         "en modelado financiero, análisis de datos y competencia en herramientas de software financiero. Poseo excelentes habilidades de comunicación, "
                         "resolución de problemas y análisis. Aspiro a aprovechar mi experiencia en finanzas y mi pasión por la inversión para establecer "
                         "y hacer crecer una firma de inversiones exitosa en México."),
        "work_experience": "💼 Experiencia Laboral",
        "education": "🎓 Educación",
        "skills": "🛠️ Habilidades",
        "projects": "📊 Proyectos",
        "certifications": "🏅 Certificaciones y Premios",
        "languages": "🌐 Idiomas",
        "interests": "🎯 Intereses y Pasatiempos",
        "why_hire_me": "🤔 ¿Por qué contratarme?",
        "why_hire_me_text": ("Aporto una sólida formación en finanzas y administración, enriquecida con experiencia de estudio internacional. Mis habilidades técnicas en análisis financiero, "
                             "gestión de proyectos y planificación estratégica se complementan con mi capacidad para comunicarme eficazmente y resolver problemas complejos. Mi ambición de establecer "
                             "una firma de inversión refleja mi dedicación y pasión por el campo. Estoy comprometido a impulsar el éxito y el crecimiento financiero a través de iniciativas innovadoras y estratégicas."),
        "work_experience_details": [
            {
                "job_title": "Analista de Proyectos",
                "company": "DA FIN LAB Soluciones Financieras, Guadalajara, Jalisco",
                "duration": "Abril 2022 – Agosto 2022",
                "responsibilities": [
                    "Realicé investigaciones de mercado exhaustivas para identificar y evaluar oportunidades de inversión.",
                    "Desarrollé estrategias de inversión iniciales, asegurando la alineación con los objetivos financieros de la empresa.",
                    "Proyecté el flujo de caja libre para ayudar en la planificación y toma de decisiones financieras.",
                    "Formulé estructuras de costos y establecí precios de venta competitivos para optimizar la rentabilidad.",
                    "Determinó el punto de equilibrio y pronostiqué la demanda esperada para apoyar la planificación empresarial.",
                    "Calculé el costo promedio ponderado del capital (WACC) para evaluar el costo de la equidad y la deuda.",
                    "Asigné ubicaciones óptimas para nuevos proyectos, considerando factores estratégicos y financieros."
                ]
            },
            {
                "job_title": "Asistente Administrativo",
                "company": "Grupo AM PM, Guadalajara, Jalisco",
                "duration": "Diciembre 2017 – Diciembre 2018",
                "responsibilities": [
                    "Gestioné el inventario y ordené suministros de oficina para garantizar operaciones diarias fluidas.",
                    "Creé, emití y cancelé facturas, manteniendo registros financieros precisos.",
                    "Actualicé y desarrollé flujos de trabajo de la empresa para mejorar la eficiencia.",
                    "Realicé tareas administrativas diarias y gestioné procesos contables para apoyar las funciones empresariales."
                ]
            }
        ],
        "education_details": {
            "degree": "Licenciatura en Administración y Finanzas",
            "institution": "Universidad Panamericana de Guadalajara",
            "graduation_year": "2024"
        },
        "skills_details": {
            "technical": [
                "Modelado financiero",
                "Análisis de datos",
                "Competencia en herramientas de software financiero (p. ej., Excel, Bloomberg Terminal)",
                "Análisis de inversiones",
                "Gestión de riesgos"
            ],
            "soft": [
                "Planificación estratégica",
                "Comunicación",
                "Resolución de problemas",
                "Pensamiento analítico",
                "Gestión de proyectos"
            ]
        },
        "projects_details": [
            {
                "name": "Página web de Predicción de Inversiones en Acciones",
                "description": ("Desarrollé una aplicación web para determinar la viabilidad de invertir en una acción utilizando regresiones multivariables y simulación de Monte Carlo."),
                "technologies": "Streamlit, Python, regresión multivariable, simulación de Monte Carlo",
                "link": "https://predictor-de-precios-gonzalocl.streamlit.app/"
            }
        ],
        "certifications_details": [
            {
                "name": "Python para Finanzas: Fundamentos de Inversión y Análisis de Datos",
                "organization": "Udemy",
                "date": "2024"
            },
            {
                "name": "Ganador del Torneo de Debate de Preparatoria",
                "description": "Ganador en dos ocasiones del torneo de debate de preparatoria.",
                "years": "2018-2019"
            }
        ],
        "languages_details": [
            "Español (Nativo)",
            "Inglés (Fluido)"
        ],
        "interests_details": [
            "Deportes extremos",
            "Miembro del equipo de voleibol de la universidad",
            "Viajar",
            "Acampar"
        ]
    }
}

# App layout and bilingual support
st.sidebar.title("Select Language / Seleccione el Idioma")
language = st.sidebar.radio("", ["English", "Español"])

# Set content based on language selection
selected_content = content["en"] if language == "English" else content["es"]

st.title(selected_content["title"])

# Personal Information
with st.expander(selected_content["personal_info"], expanded=False):
    st.write(selected_content["name"])
    st.write(selected_content["contact"])
    st.write(selected_content["email"])
    st.write(selected_content["phone"])

# Professional Summary
with st.expander(selected_content["summary"], expanded=False):
    st.write(selected_content["summary_text"])

# Work Experience
with st.expander(selected_content["work_experience"], expanded=False):
    for job in selected_content["work_experience_details"]:
        st.subheader(f"{job['job_title']} - {job['company']}")
        st.write(job["duration"])
        st.write("\n".join([f"- {resp}" for resp in job["responsibilities"]]))

# Education
with st.expander(selected_content["education"], expanded=False):
    st.write(f"{selected_content['education_details']['degree']}, {selected_content['education_details']['institution']}, {selected_content['education_details']['graduation_year']}")

# Skills
with st.expander(selected_content["skills"], expanded=False):
    st.subheader("Technical Skills" if language == "English" else "Habilidades Técnicas")
    st.write("\n".join([f"- {skill}" for skill in selected_content["skills_details"]["technical"]]))
    st.subheader("Soft Skills" if language == "English" else "Habilidades Blandas")
    st.write("\n".join([f"- {skill}" for skill in selected_content["skills_details"]["soft"]]))

# Projects
with st.expander(selected_content["projects"], expanded=False):
    for project in selected_content["projects_details"]:
        st.subheader(project["name"])
        st.write(project["description"])
        st.write(f"Technologies used: {project['technologies']}")
        st.write(f"[Link to project]({project['link']})")

# Certifications and Awards
with st.expander(selected_content["certifications"], expanded=False):
    for cert in selected_content["certifications_details"]:
        st.subheader(cert["name"])
        if "description" in cert:
            st.write(cert["description"])
        if "organization" in cert:
            st.write(f"Issuing Organization: {cert['organization']}" if language == "English" else f"Organización emisora: {cert['organization']}")
        if "date" in cert:
            st.write(f"Date: {cert['date']}" if language == "English" else f"Fecha: {cert['date']}")

# Languages
with st.expander(selected_content["languages"], expanded=False):
    st.write("\n".join([f"- {lang}" for lang in selected_content["languages_details"]]))

# Interests and Hobbies
with st.expander(selected_content["interests"], expanded=False):
    st.write("\n".join([f"- {interest}" for interest in selected_content["interests_details"]]))

# Why Hire Me
with st.expander(selected_content["why_hire_me"], expanded=False):
    st.write(selected_content["why_hire_me_text"])

# Upload PDFs to allow download
st.sidebar.title("Download CV")
st.sidebar.subheader("Select a version to download")

# English CV
with open("CV_Gonzalo_Cortes_Leal_EN.pdf", "rb") as file:
    btn = st.sidebar.download_button(
        label="Download CV in English",
        data=file,
        file_name="CV_Gonzalo_Cortes_Leal_EN.pdf",
        mime="application/pdf"
    )

# Spanish CV
with open("CV_Gonzalo_Cortes_Leal_ES.pdf", "rb") as file:
    btn = st.sidebar.download_button(
        label="Descargar CV en Español",
        data=file,
        file_name="CV_Gonzalo_Cortes_Leal_ES.pdf",
        mime="application/pdf"
    )

# Run the app with Streamlit
# To run the app, save this code in a file (e.g., `cv.py`) and run `streamlit run cv.py` in your terminal.
