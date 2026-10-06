#!/usr/bin/env python3
"""
DigitalSaathi — 100K+ SEO Keyword Generator
=============================================
Generates a master keyword database from legitimate dimension combinations.
Only creates keywords that represent real, useful search intents.

Output: seo_keywords_master.csv
Columns: keyword, cluster, sub_cluster, state, qualification, intent, 
         url_pattern, page_type, priority, tier, language
"""

import csv
import os
import sys
from itertools import product
from datetime import datetime

# Configure UTF-8 for stdout/stderr on Windows console
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

OUTPUT_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata\seo"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "seo_keywords_master.csv")
SUMMARY_FILE = os.path.join(OUTPUT_DIR, "seo_summary.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

YEAR = "2026"
YEARS = ["2025", "2026"]

# ============================================================
# EXPANDED DIMENSION DATA (FOR 100K+ LEGITIMATE KEYWORDS)
# ============================================================

ALL_STATES_UTS = [
    ("Bihar", "bihar"), ("Uttar Pradesh", "uttar-pradesh"), ("Jharkhand", "jharkhand"),
    ("West Bengal", "west-bengal"), ("Delhi", "delhi"), ("Maharashtra", "maharashtra"),
    ("Rajasthan", "rajasthan"), ("Madhya Pradesh", "madhya-pradesh"),
    ("Gujarat", "gujarat"), ("Odisha", "odisha"), ("Tamil Nadu", "tamil-nadu"),
    ("Karnataka", "karnataka"), ("Kerala", "kerala"), ("Haryana", "haryana"),
    ("Punjab", "punjab"), ("Chhattisgarh", "chhattisgarh"), ("Assam", "assam"),
    ("Himachal Pradesh", "himachal-pradesh"), ("Uttarakhand", "uttarakhand"),
    ("Telangana", "telangana"), ("Andhra Pradesh", "andhra-pradesh"),
    ("Goa", "goa"), ("Jammu Kashmir", "jammu-kashmir"),
    ("Tripura", "tripura"), ("Meghalaya", "meghalaya"), ("Manipur", "manipur"),
    ("Nagaland", "nagaland"), ("Mizoram", "mizoram"), ("Arunachal Pradesh", "arunachal-pradesh"),
    ("Sikkim", "sikkim"), ("Chandigarh", "chandigarh"), ("Puducherry", "puducherry"),
    ("Ladakh", "ladakh"), ("Andaman Nicobar", "andaman-nicobar")
]

MAJOR_DISTRICTS = [
    # Bihar
    ("Patna", "bihar"), ("Gaya", "bihar"), ("Muzaffarpur", "bihar"), ("Bhagalpur", "bihar"),
    ("Darbhanga", "bihar"), ("Purnia", "bihar"), ("Rohtas", "bihar"), ("Begusarai", "bihar"),
    # UP
    ("Lucknow", "uttar-pradesh"), ("Varanasi", "uttar-pradesh"), ("Kanpur", "uttar-pradesh"),
    ("Prayagraj", "uttar-pradesh"), ("Noida", "uttar-pradesh"), ("Gorakhpur", "uttar-pradesh"),
    ("Meerut", "uttar-pradesh"), ("Agra", "uttar-pradesh"), ("Bareilly", "uttar-pradesh"),
    # MP & Rajasthan
    ("Bhopal", "madhya-pradesh"), ("Indore", "madhya-pradesh"), ("Gwalior", "madhya-pradesh"), ("Jabalpur", "madhya-pradesh"),
    ("Jaipur", "rajasthan"), ("Jodhpur", "rajasthan"), ("Kota", "rajasthan"), ("Udaipur", "rajasthan"),
    # Jharkhand & Bengal & Delhi
    ("Ranchi", "jharkhand"), ("Jamshedpur", "jharkhand"), ("Dhanbad", "jharkhand"),
    ("Kolkata", "west-bengal"), ("Siliguri", "west-bengal"), ("Asansol", "west-bengal"),
    ("New Delhi", "delhi"), ("South Delhi", "delhi"), ("Dwarka", "delhi"),
    # Maharashtra & South
    ("Mumbai", "maharashtra"), ("Pune", "maharashtra"), ("Nagpur", "maharashtra"),
    ("Ahmedabad", "gujarat"), ("Surat", "gujarat"),
    ("Bangalore", "karnataka"), ("Hyderabad", "telangana"), ("Chennai", "tamil-nadu")
]

QUALIFICATIONS = [
    ("10th pass", "10th-pass"), ("12th pass", "12th-pass"), ("ITI", "iti"),
    ("Diploma", "diploma"), ("Graduate", "graduate"), ("Postgraduate", "postgraduate"),
    ("B.Tech", "btech"), ("BCA", "bca"), ("MCA", "mca"), ("MBA", "mba"),
    ("B.Com", "bcom"), ("B.Sc", "bsc"), ("BA", "ba"),
    ("B.Ed", "bed"), ("M.Sc", "msc"), ("M.Tech", "mtech"),
    ("LLB", "llb"), ("MBBS", "mbbs"), ("Engineering", "engineering"),
    ("Any Graduate", "any-graduate"), ("10th 12th pass", "10th-12th-pass"),
    ("Polytechnic", "polytechnic"), ("B.Pharma", "bpharma"), ("D.Pharma", "dpharma"),
    ("GNM Nursing", "gnm-nursing"), ("ANM Nursing", "anm-nursing"), ("B.Sc Nursing", "bsc-nursing"),
    ("BBA", "bba"), ("MA", "ma"), ("M.Com", "mcom"), ("Ph.D", "phd")
]

GOV_EXAMS = {
    "SSC": [
        ("SSC CGL", "ssc-cgl"), ("SSC CHSL", "ssc-chsl"), ("SSC MTS", "ssc-mts"),
        ("SSC GD Constable", "ssc-gd"), ("SSC JE", "ssc-je"),
        ("SSC Stenographer", "ssc-stenographer"), ("SSC CPO", "ssc-cpo"),
        ("SSC Selection Post", "ssc-selection-post"), ("SSC JHT", "ssc-jht"),
        ("SSC Scientific Assistant", "ssc-scientific-assistant"),
        ("SSC CGL Inspector", "ssc-cgl-inspector"), ("SSC CGL Auditor", "ssc-cgl-auditor"),
        ("SSC CGL Tax Assistant", "ssc-cgl-tax-assistant"), ("SSC CGL ASO", "ssc-cgl-aso"),
        ("SSC MTS Havaldar", "ssc-mts-havaldar"), ("SSC CHSL DEO", "ssc-chsl-deo"),
        ("SSC CHSL LDC", "ssc-chsl-ldc"), ("SSC CPO SI Delhi Police", "ssc-cpo-delhi-police")
    ],
    "UPSC": [
        ("UPSC CSE", "upsc-cse"), ("UPSC CDS", "upsc-cds"), ("UPSC NDA", "upsc-nda"),
        ("UPSC CAPF", "upsc-capf"), ("UPSC EPFO", "upsc-epfo"),
        ("UPSC IES", "upsc-ies"), ("UPSC IFS", "upsc-ifs"),
        ("UPSC CMS", "upsc-cms"), ("UPSC Geo Scientist", "upsc-geo-scientist"),
        ("UPSC Prelims", "upsc-prelims"), ("UPSC Mains", "upsc-mains"),
        ("UPSC EPFO EO AO", "upsc-epfo-eo-ao"), ("UPSC EPFO APFC", "upsc-epfo-apfc"),
        ("UPSC Civil Services IAS", "upsc-ias"), ("UPSC Civil Services IPS", "upsc-ips"),
        ("UPSC Civil Services IFS", "upsc-ifs-foreign")
    ],
    "Railway": [
        ("RRB NTPC", "rrb-ntpc"), ("RRB Group D", "rrb-group-d"),
        ("RRB JE", "rrb-je"), ("RRB ALP", "rrb-alp"),
        ("RRB Paramedical", "rrb-paramedical"), ("RRB Ministerial", "rrb-ministerial"),
        ("RPF Constable", "rpf-constable"), ("RPF SI", "rpf-si"),
        ("RRB NTPC Graduate", "rrb-ntpc-graduate"), ("RRB NTPC Undergraduate", "rrb-ntpc-undergraduate"),
        ("Railway Apprentice", "railway-apprentice"), ("RRB Technician", "rrb-technician"),
        ("RRB Station Master", "rrb-station-master"), ("RRB Goods Guard", "rrb-goods-guard"),
        ("RRB Ticket Collector", "rrb-tc"), ("RRB Trackman", "rrb-trackman"),
        ("RRB Pointsman", "rrb-pointsman"), ("RRB Senior Clerk", "rrb-senior-clerk")
    ],
    "Banking": [
        ("IBPS PO", "ibps-po"), ("IBPS Clerk", "ibps-clerk"), ("IBPS SO", "ibps-so"),
        ("IBPS RRB PO", "ibps-rrb-po"), ("IBPS RRB Clerk", "ibps-rrb-clerk"),
        ("IBPS SO IT Officer", "ibps-so-it"), ("IBPS SO Agriculture Officer", "ibps-so-agri"),
        ("IBPS SO Law Officer", "ibps-so-law"), ("IBPS SO Marketing Officer", "ibps-so-marketing"),
        ("SBI PO", "sbi-po"), ("SBI Clerk", "sbi-clerk"), ("SBI SO", "sbi-so"),
        ("RBI Grade B", "rbi-grade-b"), ("RBI Assistant", "rbi-assistant"),
        ("NABARD Grade A", "nabard-grade-a"), ("NABARD Development Assistant", "nabard-da"),
        ("SIDBI Grade A", "sidbi-grade-a"), ("IDBI Executive", "idbi-executive"),
        ("IDBI Assistant Manager", "idbi-am"), ("LIC AAO", "lic-aao"), ("LIC ADO", "lic-ado"),
        ("LIC HFL", "lic-hfl"), ("NIACL AO", "niacl-ao"), ("UIIC AO", "uiic-ao"),
        ("OICL AO", "oicl-ao"), ("GIC Assistant Manager", "gic-am")
    ],
    "Defence": [
        ("Indian Army Agniveer", "army-agniveer"), ("Indian Navy Agniveer", "navy-agniveer"),
        ("Indian Air Force Agniveer", "airforce-agniveer"),
        ("Indian Army TES", "army-tes"), ("Indian Army TGC", "army-tgc"),
        ("NDA", "nda"), ("CDS", "cds"), ("AFCAT", "afcat"),
        ("Indian Coast Guard Navik", "coast-guard-navik"), ("Indian Coast Guard Yantrik", "coast-guard-yantrik"),
        ("Military Nursing Service MNS", "military-nursing"), ("Indian Army Clerk", "army-clerk"),
        ("Indian Army GD", "army-gd"), ("Indian Army Technical", "army-tech"),
        ("Indian Army Tradesman", "army-tradesman"), ("Territorial Army", "territorial-army"),
        ("Air Force Group X", "airforce-group-x"), ("Air Force Group Y", "airforce-group-y"),
        ("Navy SSR", "navy-ssr"), ("Navy MR", "navy-mr")
    ],
    "Police": [
        ("UP Police Constable", "up-police-constable"), ("UP Police SI", "up-police-si"),
        ("UP Police Radio Operator", "up-police-radio-operator"), ("UP Police Computer Operator", "up-police-computer-operator"),
        ("Bihar Police Constable", "bihar-police-constable"), ("Bihar Police SI", "bihar-police-si"),
        ("Bihar Police Driver", "bihar-police-driver"), ("Bihar Police Fireman", "bihar-police-fireman"),
        ("Delhi Police Constable", "delhi-police-constable"), ("Delhi Police SI", "delhi-police-si"),
        ("Delhi Police Head Constable", "delhi-police-hc"), ("Delhi Police Driver", "delhi-police-driver"),
        ("MP Police Constable", "mp-police-constable"), ("MP Police SI", "mp-police-si"),
        ("Rajasthan Police Constable", "rajasthan-police-constable"), ("Rajasthan Police SI", "rajasthan-police-si"),
        ("Haryana Police Constable", "haryana-police-constable"), ("Haryana Police SI", "haryana-police-si"),
        ("CRPF Constable GD", "crpf-constable"), ("CRPF Head Constable Ministerial", "crpf-hcm"),
        ("BSF Constable GD", "bsf-constable"), ("BSF Head Constable RO RM", "bsf-ro-rm"),
        ("CISF Constable Fireman", "cisf-fireman"), ("CISF Head Constable Ministerial", "cisf-hcm"),
        ("ITBP Constable GD", "itbp-constable"), ("ITBP Head Constable", "itbp-hc"),
        ("SSB Constable GD", "ssb-constable"), ("SSB Head Constable", "ssb-hc"),
        ("Assam Rifles GD", "assam-rifles-gd"), ("Assam Rifles Technical", "assam-rifles-tech"),
        ("Maharashtra Police Constable", "maharashtra-police-constable"), ("Maharashtra Police SI", "maharashtra-police-si"),
        ("West Bengal Police Constable", "wb-police-constable"), ("West Bengal Police SI", "wb-police-si"),
        ("Jharkhand Police Constable", "jharkhand-police-constable"), ("Jharkhand Police SI", "jharkhand-police-si"),
        ("Odisha Police Constable", "odisha-police-constable"), ("Chhattisgarh Police Constable", "cg-police-constable")
    ],
    "Teaching": [
        ("CTET", "ctet"), ("CTET Paper 1", "ctet-paper-1"), ("CTET Paper 2", "ctet-paper-2"),
        ("DSSSB TGT", "dsssb-tgt"), ("DSSSB PGT", "dsssb-pgt"), ("DSSSB PRT", "dsssb-prt"),
        ("KVS Teacher PRT", "kvs-prt"), ("KVS TGT", "kvs-tgt"), ("KVS PGT", "kvs-pgt"),
        ("NVS Teacher PRT", "nvs-prt"), ("NVS TGT", "nvs-tgt"), ("NVS PGT", "nvs-pgt"),
        ("SUPER TET", "super-tet"), ("UPTET Paper 1", "uptet-paper-1"), ("UPTET Paper 2", "uptet-paper-2"),
        ("BPSC Teacher TRE 3.0", "bpsc-tre-3"), ("BPSC Teacher TRE 4.0", "bpsc-tre-4"),
        ("BPSC Head Teacher", "bpsc-head-teacher"), ("BPSC Headmaster", "bpsc-headmaster"),
        ("BTET", "btet"), ("HTET", "htet"), ("REET Level 1", "reet-level-1"), ("REET Level 2", "reet-level-2"),
        ("MPTET Varg 1", "mptet-varg-1"), ("MPTET Varg 2", "mptet-varg-2"), ("MPTET Varg 3", "mptet-varg-3"),
        ("OTET", "otet"), ("TN TET", "tn-tet"), ("KAR TET", "kar-tet"),
        ("WB TET", "wb-tet"), ("UGC NET", "ugc-net"), ("CSIR NET", "csir-net"),
        ("UGC NET Computer Science", "ugc-net-cs"), ("UGC NET Commerce", "ugc-net-commerce"),
        ("UGC NET Management", "ugc-net-mgmt"), ("UGC NET Economics", "ugc-net-economics"),
        ("UGC NET English", "ugc-net-english"), ("UGC NET Hindi", "ugc-net-hindi"),
        ("EMRS Teacher TGT", "emrs-tgt"), ("EMRS Teacher PGT", "emrs-pgt")
    ],
    "PSU": [
        ("ONGC Graduate Trainee", "ongc-gt"), ("ONGC Apprentice", "ongc-apprentice"),
        ("BHEL Engineer Trainee", "bhel-et"), ("SAIL Management Trainee", "sail-mt"),
        ("SAIL OCTT", "sail-octt"), ("NTPC Executive Trainee", "ntpc-et"),
        ("GAIL Executive Trainee", "gail-et"), ("Coal India Management Trainee", "cil-mt"),
        ("HAL Management Trainee", "hal-mt"), ("HAL Design Trainee", "hal-dt"),
        ("BEL Probationary Engineer", "bel-pe"), ("BARC Scientific Officer", "barc-ocse"),
        ("BARC Stipendiary Trainee", "barc-st"), ("DRDO CEPTAM", "drdo-ceptam"),
        ("DRDO Scientist B", "drdo-scientist-b"), ("ISRO Scientist SC", "isro-scientist-sc"),
        ("ISRO Technical Assistant", "isro-tech-assistant"), ("IOCL Apprentice", "iocl-apprentice"),
        ("IOCL Junior Engineering Assistant", "iocl-jea"), ("BPCL Graduate Apprentice", "bpcl-apprentice"),
        ("HPCL Engineer", "hpcl-engineer"), ("Power Grid Diploma Trainee", "pgcil-dt"),
        ("Power Grid Executive Trainee", "pgcil-et"), ("NHPC Trainee Engineer", "nhpc-te"),
        ("Delhi Metro DMRC CRA", "dmrc-cra"), ("Delhi Metro DMRC JE", "dmrc-je"),
        ("Delhi Metro DMRC Maintainer", "dmrc-maintainer"), ("NMRC Train Operator", "nmrc-to"),
        ("ECIL Junior Technician", "ecil-jt"), ("AAI Junior Executive ATC", "aai-je-atc"),
        ("AAI Junior Executive Common Cadre", "aai-je-common")
    ],
    "State PSC": [
        ("BPSC CCE", "bpsc-cce"), ("BPSC CDPO", "bpsc-cdpo"), ("BPSC Assistant Engineer", "bpsc-ae"),
        ("UPPSC PCS", "uppsc-pcs"), ("UPPSC RO ARO", "uppsc-ro-aro"), ("UPPSC Staff Nurse", "uppsc-staff-nurse"),
        ("JPSC Combined Civil Services", "jpsc-ccs"), ("MPPSC State Service Exam", "mppsc-sse"),
        ("MPPSC Forest Service", "mppsc-forest"), ("RPSC RAS RTS", "rpsc-ras"),
        ("RPSC 1st Grade Teacher", "rpsc-1st-grade"), ("RPSC 2nd Grade Teacher", "rpsc-2nd-grade"),
        ("WBPSC WBCS", "wbpsc-wbcs"), ("WBPSC Miscellaneous", "wbpsc-misc"),
        ("UKPSC PCS", "ukpsc-pcs"), ("HPPSC HPAS", "hppsc-hpas"), ("HPSC HCS", "hpsc-hcs"),
        ("GPSC Class 1 2", "gpsc-class-1-2"), ("OPSC OAS", "opsc-oas"), ("KPSC KAS", "kpsc-kas"),
        ("TNPSC Group 1", "tnpsc-group-1"), ("TNPSC Group 2", "tnpsc-group-2"), ("TNPSC Group 4", "tnpsc-group-4"),
        ("APPSC Group 1", "appsc-group-1"), ("APPSC Group 2", "appsc-group-2"),
        ("TSPSC Group 1", "tspsc-group-1"), ("TSPSC Group 2", "tspsc-group-2"), ("TSPSC Group 4", "tspsc-group-4"),
        ("CGPSC State Service", "cgpsc-sse"), ("PPSC PCS", "ppsc-pcs")
    ]
}

EXAM_INTENTS = [
    ("notification", "notification", "info"),
    ("vacancy", "vacancy", "info"),
    ("eligibility", "eligibility", "info"),
    ("syllabus", "syllabus", "info"),
    ("exam pattern", "exam-pattern", "info"),
    ("salary", "salary", "info"),
    ("age limit", "age-limit", "info"),
    ("application fee", "application-fee", "info"),
    ("apply online", "apply-online", "action"),
    ("admit card", "admit-card", "action"),
    ("result", "result", "action"),
    ("cutoff", "cutoff", "info"),
    ("cutoff marks category wise", "cutoff-category", "info"),
    ("answer key", "answer-key", "info"),
    ("previous year papers", "previous-papers", "resource"),
    ("question paper with solutions", "solved-papers", "resource"),
    ("preparation", "preparation", "guide"),
    ("study material", "study-material", "resource"),
    ("mock test", "mock-test", "tool"),
    ("books", "books", "resource"),
    ("selection process", "selection-process", "info"),
    ("how to apply", "how-to-apply", "guide"),
    ("important dates", "important-dates", "info"),
    ("exam date", "exam-date", "info"),
    ("last date to apply", "last-date", "info"),
    ("form", "form", "action"),
    ("online form", "online-form", "action"),
    ("qualification required", "qualification", "info"),
    ("salary in hand after 7th pay", "salary-in-hand", "info"),
    ("job profile and promotions", "job-profile", "info"),
    ("posting and transfer policy", "posting", "info"),
    ("physical test PET PST criteria", "physical-test", "info"),
    ("medical standard requirements", "medical-standard", "info"),
    ("age relaxation for OBC SC ST EWS", "age-relaxation", "info"),
    ("negative marking details", "negative-marking", "info")
]

UNIVERSITIES_LIST = [
    ("Delhi University DU", "du"), ("Mumbai University MU", "mumbai-university"),
    ("Anna University", "anna-university"), ("AKTU Dr APJ Abdul Kalam Technical University", "aktu"),
    ("VTU Visvesvaraya Technological University", "vtu"), ("Pune University SPPU", "sppu"),
    ("Calicut University", "calicut-university"), ("JNTU Hyderabad", "jntu-hyderabad"),
    ("JNTU Kakinada", "jntu-kakinada"), ("Gujarat Technological University GTU", "gtu"),
    ("Patna University", "patna-university"), ("BRABU Bihar University", "brabu"),
    ("Magadh University", "magadh-university"), ("LNMU Darbhanga", "lnmu"),
    ("PPU Patliputra University", "ppu"), ("VKSU Ara", "vksu"), ("TMBU Bhagalpur", "tmbu"),
    ("BNMU Madhepura", "bnmu"), ("Purnea University", "purnea-university"),
    ("Ranchi University", "ranchi-university"), ("BBMKU Dhanbad", "bbmku"),
    ("VBU Hazaribagh", "vbu"), ("Calcutta University", "calcutta-university"),
    ("MAKAUT WBUT", "makaut"), ("RGPV Bhopal", "rgpv"), ("CSVTU Bhilai", "csvtu"),
    ("RTU Kota", "rtu"), ("Rajasthan University", "uniraj"),
    ("Kurukshetra University KUK", "kuk"), ("MDU Rohtak", "mdu"),
    ("GNDU Amritsar", "gndu"), ("PTU Jalandhar", "ptu"),
    ("BHU Banaras Hindu University", "bhu"), ("AMU Aligarh Muslim University", "amu"),
    ("JNU Jawaharlal Nehru University", "jnu"), ("Jamia Millia Islamia JMI", "jmi"),
    ("IGNOU", "ignou"), ("Osmania University", "osmania-university"),
    ("Andhra University", "andhra-university"), ("Madras University", "madras-university"),
    ("Kerala University", "kerala-university"), ("MG University Kerala", "mgu-kerala"),
    ("Gauhati University", "gauhati-university"), ("Utkal University", "utkal-university"),
    ("BPUT Odisha", "bput"), ("HNBGU Uttarakhand", "hnbgu"),
    ("Kumaun University", "kumaun-university"), ("HPU Shimla", "hpu")
]

SUBJECTS_BY_STREAM = {
    "MCA_BCA_CS": [
        ("Java Programming", "java"), ("Advanced Java", "adv-java"), ("Python Programming", "python"),
        ("C Programming", "c-programming"), ("C++ OOP", "cpp"), ("DBMS Database Management", "dbms"),
        ("SQL and Relational Queries", "sql"), ("Operating System OS", "operating-system"),
        ("Computer Networks CN", "computer-networks"), ("Data Structures and Algorithms DSA", "dsa"),
        ("Design and Analysis of Algorithms DAA", "daa"), ("Software Engineering SE", "software-engineering"),
        ("Web Development HTML CSS JS", "web-development"), ("Artificial Intelligence AI", "ai"),
        ("Machine Learning ML", "machine-learning"), ("Cloud Computing AWS Azure", "cloud-computing"),
        ("Cybersecurity and Ethical Hacking", "cybersecurity"), ("Computer Organization Architecture COA", "coa"),
        ("Compiler Design", "compiler-design"), ("Theory of Computation Automata TOC", "toc"),
        ("Discrete Mathematics", "discrete-math"), ("Digital Electronics", "digital-electronics"),
        ("Microprocessor 8085 8086", "microprocessor"), ("Computer Graphics and Multimedia", "computer-graphics"),
        ("Object Oriented Programming OOP", "oop"), ("Linux and Shell Scripting", "linux"),
        ("React JS Frontend", "react-js"), ("Node JS Backend", "nodejs"),
        ("PHP and MySQL", "php-mysql"), ("Android App Development", "android"),
        ("Data Science with Python", "data-science"), ("Big Data Hadoop Spark", "big-data"),
        ("MongoDB and NoSQL", "mongodb-nosql"), ("Cryptography and Network Security", "cryptography"),
        ("Distributed Systems", "distributed-systems"), ("Information Security", "information-security"),
        ("Mobile Computing", "mobile-computing"), ("Data Mining and Data Warehousing", "data-mining"),
        ("IoT Internet of Things", "iot"), ("Blockchain Technology", "blockchain")
    ],
    "COMMERCE_MGMT": [
        ("Financial Accounting", "financial-accounting"), ("Corporate Accounting", "corporate-accounting"),
        ("Cost Accounting", "cost-accounting"), ("Management Accounting", "management-accounting"),
        ("Business Economics", "business-economics"), ("Macro Economics", "macro-economics"),
        ("Micro Economics", "micro-economics"), ("Business Statistics", "business-statistics"),
        ("Business Mathematics", "business-mathematics"), ("Business Law Mercantile Law", "business-law"),
        ("Company Law", "company-law"), ("Direct Tax Income Tax", "income-tax"),
        ("Indirect Tax GST", "gst-tax"), ("Auditing and Assurance", "auditing"),
        ("Financial Management FM", "financial-management"), ("Marketing Management", "marketing-management"),
        ("Human Resource Management HRM", "hrm"), ("Operations Management", "operations-management"),
        ("Organizational Behavior OB", "organizational-behavior"), ("International Business", "international-business"),
        ("Banking Operations and Law", "banking-law"), ("Insurance and Risk Management", "insurance-management"),
        ("Tally Prime with GST", "tally-prime"), ("Security Analysis Portfolio Management SAPM", "sapm")
    ],
    "ARTS_HUMANITIES": [
        ("Indian Polity and Constitution", "indian-polity"), ("Ancient Indian History", "ancient-history"),
        ("Medieval Indian History", "medieval-history"), ("Modern Indian History", "modern-history"),
        ("World History", "world-history"), ("Physical Geography", "physical-geography"),
        ("Indian Geography", "indian-geography"), ("Sociology Fundamentals", "sociology"),
        ("General Psychology", "psychology"), ("Public Administration", "public-administration"),
        ("English Literature and Poetry", "english-literature"), ("English Grammar and Composition", "english-grammar"),
        ("Hindi Sahitya History and Novels", "hindi-sahitya"), ("Hindi Vyakaran Grammar", "hindi-vyakaran"),
        ("International Relations IR", "international-relations"), ("Political Theory", "political-theory")
    ],
    "SCIENCE_ENGG": [
        ("Engineering Physics", "engineering-physics"), ("Engineering Chemistry", "engineering-chemistry"),
        ("Engineering Mathematics 1", "maths-1"), ("Engineering Mathematics 2", "maths-2"),
        ("Engineering Mathematics 3", "maths-3"), ("Engineering Mechanics", "engineering-mechanics"),
        ("Basic Electrical Engineering BEE", "bee"), ("Basic Electronics Engineering", "basic-electronics"),
        ("Thermodynamics", "thermodynamics"), ("Fluid Mechanics", "fluid-mechanics"),
        ("Strength of Materials SOM", "som"), ("Theory of Machines TOM", "tom"),
        ("Manufacturing Process", "manufacturing-process"), ("Structural Analysis", "structural-analysis"),
        ("Concrete Technology", "concrete-tech"), ("Surveying", "surveying"),
        ("Organic Chemistry", "organic-chemistry"), ("Inorganic Chemistry", "inorganic-chemistry"),
        ("Physical Chemistry", "physical-chemistry"), ("Mechanics and Waves", "mechanics-waves"),
        ("Electromagnetism and Optics", "electromagnetism"), ("Quantum Physics", "quantum-physics"),
        ("Cell Biology and Genetics", "cell-biology"), ("Zoology Animal Diversity", "zoology"),
        ("Botany Plant Physiology", "botany"), ("Microbiology", "microbiology"),
        ("Biotechnology", "biotechnology"), ("Environmental Science EVS", "evs")
    ]
}

ACADEMIC_CONTENT_INTENTS = [
    ("handwritten notes PDF", "handwritten-notes", "resource"),
    ("viva questions with answers", "viva-questions", "resource"),
    ("top interview questions and answers", "interview-questions", "resource"),
    ("important questions for semester exam", "important-questions", "resource"),
    ("multiple choice questions MCQ quiz", "mcq-quiz", "tool"),
    ("previous 5 year question papers solved", "previous-papers", "resource"),
    ("complete syllabus and topics list", "syllabus", "info"),
    ("practical programs source code and output", "practical-programs", "resource"),
    ("lab manual with viva voce questions", "lab-manual", "resource"),
    ("final year project ideas and source code", "projects", "resource"),
    ("mini project with documentation report", "mini-projects", "resource"),
    ("quick revision cheat sheet formula PDF", "cheat-sheet", "resource"),
    ("step by step complete tutorial guide", "tutorial", "guide"),
    ("learning roadmap for beginners", "roadmap", "guide"),
    ("recommended standard textbooks PDF", "textbooks", "resource"),
    ("2 marks and 10 marks solved question bank", "question-bank", "resource")
]

CYBER_CAFE_CERTIFICATES = [
    ("Income Certificate Aay Praman Patra", "income-certificate"),
    ("Caste Certificate Jati Praman Patra", "caste-certificate"),
    ("Residence Domicile Niwas Praman Patra", "residence-certificate"),
    ("OBC NCL Non Creamy Layer Certificate", "obc-ncl-certificate"),
    ("EWS Economically Weaker Section Certificate", "ews-certificate"),
    ("Character Certificate Charitra Praman Patra", "character-certificate"),
    ("Birth Certificate Janam Praman Patra", "birth-certificate"),
    ("Death Certificate Mrityu Praman Patra", "death-certificate"),
    ("Marriage Certificate Vivah Panjiyan", "marriage-certificate"),
    ("Ration Card Online Apply", "ration-card"),
    ("Aadhaar Card Update and Correction", "aadhaar-update"),
    ("PAN Card Apply and Correction Form 49A", "pan-card-apply"),
    ("Voter ID Card Voter Helpline Form 6 Form 8", "voter-id-apply"),
    ("Driving License Learner DL Online Sarathi", "driving-license"),
    ("Ayushman Card PMJAY Health Card Download", "ayushman-card"),
    ("E-Shram Card Registration and Download", "eshram-card"),
    ("PM Kisan Samman Nidhi KYC Registration", "pm-kisan-kyc"),
    ("Kisan Credit Card KCC Online Apply", "kcc-apply"),
    ("Labour Card Majdoor Card Registration", "labour-card"),
    ("Divyangjan Disability Certificate UDID", "disability-certificate")
]

STATE_JOB_INTENTS = [
    ("government jobs", "government-jobs", "listing"),
    ("govt jobs", "govt-jobs", "listing"),
    ("sarkari naukri", "sarkari-naukri", "listing"),
    ("government jobs latest", "government-jobs-latest", "listing"),
    ("upcoming government jobs", "upcoming-govt-jobs", "listing"),
    ("government jobs for freshers", "govt-jobs-freshers", "listing"),
    ("government jobs without exam", "govt-jobs-without-exam", "listing"),
    ("latest vacancy notification", "latest-vacancy", "listing"),
    ("police recruitment bharti", "police-recruitment", "listing"),
    ("teacher recruitment vacancy", "teacher-recruitment", "listing"),
    ("forest department jobs", "forest-jobs", "listing"),
    ("health department staff nurse jobs", "health-jobs", "listing"),
    ("agriculture department jobs", "agriculture-jobs", "listing"),
    ("high court civil court jobs", "court-jobs", "listing"),
    ("panchayat sachiv vdo jobs", "panchayat-jobs", "listing"),
    ("block development jobs", "block-jobs", "listing"),
    ("district collectorate jobs", "district-jobs", "listing"),
    ("clerk stenographer jobs", "clerk-jobs", "listing"),
    ("driver conductor recruitment", "driver-jobs", "listing"),
    ("junior engineer JE jobs", "je-jobs", "listing"),
    ("lab technician pharmacist jobs", "lab-technician-jobs", "listing"),
    ("anganwadi helper worker jobs", "anganwadi-jobs", "listing")
]

# --- PDF Tools ---
PDF_TOOLS = [
    ("jpg to pdf", "jpg-to-pdf"), ("png to pdf", "png-to-pdf"),
    ("image to pdf", "image-to-pdf"), ("pdf to jpg", "pdf-to-jpg"),
    ("pdf to png", "pdf-to-png"), ("pdf to word", "pdf-to-word"),
    ("word to pdf", "word-to-pdf"), ("excel to pdf", "excel-to-pdf"),
    ("pdf compressor", "pdf-compressor"), ("compress pdf", "compress-pdf"),
    ("merge pdf", "merge-pdf"), ("combine pdf", "combine-pdf"),
    ("split pdf", "split-pdf"), ("pdf splitter", "pdf-splitter"),
    ("rotate pdf", "rotate-pdf"), ("pdf page extractor", "pdf-page-extractor"),
    ("pdf editor", "pdf-editor"), ("pdf reader", "pdf-reader"),
    ("pdf viewer", "pdf-viewer"), ("pdf unlock", "pdf-unlock"),
    ("pdf password remover", "pdf-password-remover"),
    ("pdf to text", "pdf-to-text"), ("pdf metadata editor", "pdf-metadata"),
    ("pdf page reorder", "pdf-page-reorder"),
    ("add watermark to pdf", "pdf-watermark"),
    ("pdf page number", "pdf-page-number"),
    ("pdf to excel", "pdf-to-excel"),
    ("html to pdf", "html-to-pdf"),
]

PDF_MODIFIERS = [
    "online", "free", "converter", "tool", "online free",
    "without signup", "fast", "best", "mobile",
    "no watermark", "unlimited", "batch",
]

# --- Image/Photo Tools ---
IMAGE_TOOLS = [
    ("image resizer", "image-resizer"), ("photo resizer", "photo-resizer"),
    ("image compressor", "image-compressor"), ("photo compressor", "photo-compressor"),
    ("image converter", "image-converter"), ("jpg to png", "jpg-to-png"),
    ("png to jpg", "png-to-jpg"), ("webp to jpg", "webp-to-jpg"),
    ("webp to png", "webp-to-png"), ("jpg to webp", "jpg-to-webp"),
    ("image cropper", "image-cropper"), ("photo cropper", "photo-cropper"),
    ("background remover", "background-remover"),
    ("image to base64", "image-to-base64"),
    ("svg to png", "svg-to-png"), ("gif maker", "gif-maker"),
    ("image rotator", "image-rotator"), ("image flipper", "image-flipper"),
    ("bulk image resizer", "bulk-image-resizer"),
    ("image optimizer", "image-optimizer"),
]

# --- Cyber Café / Photo Tools ---
PHOTO_SIZES = [
    ("passport photo", "passport-photo"),
    ("passport photo Indian", "passport-photo-india"),
    ("visa photo US", "visa-photo-us"), ("visa photo UK", "visa-photo-uk"),
    ("visa photo Canada", "visa-photo-canada"), ("visa photo Australia", "visa-photo-australia"),
    ("Aadhaar photo", "aadhaar-photo"),
    ("PAN card photo", "pan-card-photo"),
    ("driving license photo", "dl-photo"),
    ("voter ID photo", "voter-id-photo"),
]

PHOTO_FORM_EXAMS = [
    "SSC", "UPSC", "Railway", "IBPS", "SBI", "RBI", "CTET", "NDA", "CDS",
    "BPSC", "UPPSC", "GATE", "CAT", "CLAT", "NEET", "JEE", "NTSE",
    "KVS", "NVS", "DRDO", "ISRO", "college admission", "university",
    "scholarship form", "exam form",
]

SIGNATURE_FORMS = [
    "SSC", "UPSC", "IBPS", "SBI", "Railway", "GATE", "CTET", "BPSC",
    "UPPSC", "NDA", "CDS", "NEET", "JEE", "government form", "online form",
    "bank form", "exam form",
]

CYBER_CAFE_SERVICES = [
    ("photo print layout A4", "photo-print-a4"),
    ("passport photo print", "passport-photo-print"),
    ("ID card maker", "id-card-maker"),
    ("certificate maker", "certificate-maker"),
    ("form filling guide", "form-filling"),
    ("document scanner", "document-scanner"),
    ("QR code generator", "qr-code-generator"),
    ("barcode generator", "barcode-generator"),
]

# --- Calculators ---
EDUCATION_CALCS = [
    ("CGPA calculator", "cgpa-calculator"), ("CGPA to percentage", "cgpa-to-percentage"),
    ("percentage to CGPA", "percentage-to-cgpa"), ("SGPA calculator", "sgpa-calculator"),
    ("GPA calculator", "gpa-calculator"), ("percentage calculator", "percentage-calculator"),
    ("attendance calculator", "attendance-calculator"),
    ("marks calculator", "marks-calculator"), ("grade calculator", "grade-calculator"),
    ("aggregate calculator", "aggregate-calculator"),
    ("semester calculator", "semester-calculator"),
    ("required marks calculator", "required-marks-calculator"),
]

FINANCE_CALCS = [
    ("EMI calculator", "emi-calculator"), ("SIP calculator", "sip-calculator"),
    ("FD calculator", "fd-calculator"), ("RD calculator", "rd-calculator"),
    ("GST calculator", "gst-calculator"), ("salary calculator", "salary-calculator"),
    ("income tax calculator", "income-tax-calculator"),
    ("profit loss calculator", "profit-loss-calculator"),
    ("discount calculator", "discount-calculator"),
    ("compound interest calculator", "compound-interest-calculator"),
    ("simple interest calculator", "simple-interest-calculator"),
    ("loan calculator", "loan-calculator"), ("home loan calculator", "home-loan-calculator"),
    ("car loan calculator", "car-loan-calculator"),
    ("personal loan calculator", "personal-loan-calculator"),
    ("PPF calculator", "ppf-calculator"), ("NPS calculator", "nps-calculator"),
    ("gratuity calculator", "gratuity-calculator"),
    ("HRA calculator", "hra-calculator"),
    ("TDS calculator", "tds-calculator"),
    ("mutual fund calculator", "mutual-fund-calculator"),
    ("lumpsum calculator", "lumpsum-calculator"),
    ("inflation calculator", "inflation-calculator"),
]

GENERAL_CALCS = [
    ("age calculator", "age-calculator"),
    ("date difference calculator", "date-difference-calculator"),
    ("days calculator", "days-calculator"),
    ("time calculator", "time-calculator"),
    ("BMI calculator", "bmi-calculator"),
    ("calorie calculator", "calorie-calculator"),
    ("unit converter", "unit-converter"),
    ("length converter", "length-converter"),
    ("weight converter", "weight-converter"),
    ("temperature converter", "temperature-converter"),
    ("area calculator", "area-calculator"),
    ("volume calculator", "volume-calculator"),
    ("speed calculator", "speed-calculator"),
    ("fuel cost calculator", "fuel-cost-calculator"),
    ("tip calculator", "tip-calculator"),
    ("binary to decimal", "binary-decimal"),
    ("hex to decimal", "hex-decimal"),
    ("octal converter", "octal-converter"),
    ("roman numeral converter", "roman-numeral"),
    ("random number generator", "random-number"),
    ("word counter", "word-counter"),
    ("character counter", "character-counter"),
]

CALC_MODIFIERS = [
    "online", "free", "formula", "with example", "for students",
    "India", "2026",
]

UNIVERSITY_CALCS = [
    "Mumbai University", "Delhi University", "Anna University", "AKTU",
    "VTU", "Pune University", "Calicut University", "JNTU",
    "Gujarat University", "Patna University", "RGPV", "CSVTU",
    "Kumaun University", "Magadh University", "Bihar University",
    "Ranchi University", "BHU", "AMU", "JNU",
]

# --- Developer Tools ---
DEV_TOOLS = [
    ("JSON formatter", "json-formatter"), ("JSON validator", "json-validator"),
    ("JSON beautifier", "json-beautifier"), ("JSON minifier", "json-minifier"),
    ("JSON viewer", "json-viewer"), ("JSON to CSV", "json-to-csv"),
    ("JSON to XML", "json-to-xml"), ("JSON to YAML", "json-to-yaml"),
    ("JSON editor", "json-editor"), ("JSON parser", "json-parser"),
    ("SQL formatter", "sql-formatter"), ("SQL beautifier", "sql-beautifier"),
    ("SQL validator", "sql-validator"), ("SQL minifier", "sql-minifier"),
    ("SQL to MongoDB", "sql-to-mongodb"),
    ("Base64 encoder", "base64-encoder"), ("Base64 decoder", "base64-decoder"),
    ("Base64 to image", "base64-to-image"), ("image to Base64", "image-to-base64"),
    ("URL encoder", "url-encoder"), ("URL decoder", "url-decoder"),
    ("HTML formatter", "html-formatter"), ("HTML beautifier", "html-beautifier"),
    ("HTML minifier", "html-minifier"), ("HTML to markdown", "html-to-markdown"),
    ("HTML encoder", "html-entity-encoder"), ("HTML decoder", "html-entity-decoder"),
    ("CSS formatter", "css-formatter"), ("CSS beautifier", "css-beautifier"),
    ("CSS minifier", "css-minifier"),
    ("JavaScript formatter", "js-formatter"), ("JavaScript beautifier", "js-beautifier"),
    ("JavaScript minifier", "js-minifier"),
    ("XML formatter", "xml-formatter"), ("XML to JSON", "xml-to-json"),
    ("YAML formatter", "yaml-formatter"), ("YAML to JSON", "yaml-to-json"),
    ("regex tester", "regex-tester"), ("regex generator", "regex-generator"),
    ("UUID generator", "uuid-generator"), ("GUID generator", "guid-generator"),
    ("hash generator MD5", "md5-hash"), ("hash generator SHA256", "sha256-hash"),
    ("hash generator SHA1", "sha1-hash"), ("hash generator SHA512", "sha512-hash"),
    ("timestamp converter", "timestamp-converter"),
    ("Unix timestamp", "unix-timestamp"),
    ("color picker", "color-picker"), ("color converter", "color-converter"),
    ("hex to RGB", "hex-to-rgb"), ("RGB to hex", "rgb-to-hex"),
    ("JWT decoder", "jwt-decoder"), ("JWT encoder", "jwt-encoder"),
    ("Lorem Ipsum generator", "lorem-ipsum"),
    ("markdown editor", "markdown-editor"), ("markdown previewer", "markdown-preview"),
    ("password generator", "password-generator"),
    ("QR code generator", "qr-code-generator"),
    ("cron expression generator", "cron-generator"),
    ("diff checker", "diff-checker"), ("text compare", "text-compare"),
    ("CSV to JSON", "csv-to-json"), ("JSON to CSV", "json-to-csv-tool"),
    ("text to binary", "text-to-binary"), ("binary to text", "binary-to-text"),
    ("IP address lookup", "ip-lookup"),
    ("user agent parser", "user-agent-parser"),
    ("HTTP status codes", "http-status-codes"),
    ("meta tag generator", "meta-tag-generator"),
    ("robots.txt generator", "robots-txt-generator"),
    ("sitemap generator", "sitemap-generator-tool"),
    ("favicon generator", "favicon-generator"),
    ("open graph generator", "og-generator"),
    ("CSS gradient generator", "css-gradient"),
    ("CSS flexbox generator", "css-flexbox"),
    ("CSS grid generator", "css-grid-generator"),
    ("CSS shadow generator", "css-shadow"),
    ("CSS border radius", "css-border-radius"),
    ("SVG editor", "svg-editor"),
    ("emoji picker", "emoji-picker"),
    ("ASCII table", "ascii-table"),
    ("character encoder", "character-encoder"),
    ("slug generator", "slug-generator"),
]

DEV_MODIFIERS = ["online", "free", "tool", "online free"]

# --- Resume / Career ---
RESUME_TYPES = [
    "fresher", "experienced", "MCA", "BCA", "B.Tech", "MBA", "B.Com", "B.Sc",
    "BA", "software engineer", "data analyst", "web developer", "full stack developer",
    "frontend developer", "backend developer", "Java developer", "Python developer",
    "Android developer", "data scientist", "machine learning engineer",
    "DevOps engineer", "cloud engineer", "network engineer",
    "teacher", "accountant", "bank", "government job",
    "internship", "part time", "freelancer",
    "mechanical engineer", "civil engineer", "electrical engineer",
    "electronics engineer", "nursing", "pharmacy",
]

RESUME_INTENTS = [
    ("resume format", "format"), ("resume template", "template"),
    ("resume example", "example"), ("resume sample", "sample"),
    ("resume objective", "objective"), ("resume summary", "summary"),
    ("resume skills", "skills"), ("resume projects", "projects"),
    ("cover letter", "cover-letter"),
]

CAREER_CONTENT = [
    ("interview questions", "interview-questions"),
    ("interview tips", "interview-tips"),
    ("salary negotiation", "salary-negotiation"),
    ("career path", "career-path"),
    ("skills required", "skills-required"),
    ("roadmap", "career-roadmap"),
    ("certifications", "certifications"),
    ("courses", "courses"),
    ("scope", "scope"),
    ("future", "future"),
]

career_roles = [
    "software engineer", "web developer", "data scientist", "data analyst",
    "machine learning engineer", "DevOps engineer", "cloud engineer",
    "full stack developer", "frontend developer", "backend developer",
    "mobile developer", "Android developer", "iOS developer",
    "Java developer", "Python developer", "React developer",
    "cybersecurity analyst", "network engineer", "database administrator",
    "QA engineer", "UI/UX designer", "product manager",
    "digital marketing executive", "content writer", "graphic designer",
    "teacher", "bank PO", "bank clerk", "IAS officer", "IPS officer",
    "mechanical engineer", "civil engineer", "electrical engineer",
    "pharmacist", "nurse", "chartered accountant", "data entry operator"
]

# --- Scholarships ---
SCHOLARSHIP_TYPES = [
    "central government", "state government", "Bihar", "UP", "Delhi",
    "Jharkhand", "Maharashtra", "Rajasthan", "MP", "West Bengal",
    "SC ST", "OBC", "minority", "girl students", "merit based",
    "need based", "engineering", "medical", "MBA", "law",
    "MCA", "BCA", "B.Tech", "postgraduate", "PhD",
    "10th pass", "12th pass", "graduate",
    "international", "USA", "UK", "Canada", "Australia", "Germany",
    "NTSE", "KVPY", "UGC", "CSIR",
    "private", "corporate", "Tata", "Reliance",
]

SCHOLARSHIP_INTENTS = [
    "scholarship", "scholarship 2026", "scholarship apply online",
    "scholarship last date", "scholarship eligibility",
    "scholarship amount", "scholarship form",
    "scholarship list", "scholarship result",
]

# ============================================================
# KEYWORD GENERATION
# ============================================================

keywords = []
seen = set()

def add_kw(keyword, cluster, sub_cluster, state, qualification, intent,
           url_pattern, page_type, priority, tier, language="en"):
    """Add keyword if not duplicate."""
    kw_lower = keyword.lower().strip()
    if kw_lower in seen or len(kw_lower) < 5:
        return
    seen.add(kw_lower)
    keywords.append({
        "keyword": keyword,
        "cluster": cluster,
        "sub_cluster": sub_cluster,
        "state": state,
        "qualification": qualification,
        "intent": intent,
        "url_pattern": url_pattern,
        "page_type": page_type,
        "priority": priority,
        "tier": tier,
        "language": language,
    })

def score_priority(demand, relevance):
    """Simple priority scorer."""
    if demand == "high" and relevance == "high":
        return ("HIGH", 1)
    elif demand == "high" or relevance == "high":
        return ("MEDIUM", 2)
    else:
        return ("LOW", 3)


# ============================================================
# KEYWORD GENERATION ENGINE (100,000+ TARGET)
# ============================================================

keywords = []
seen = set()

def add_kw(keyword, cluster, sub_cluster, state, qualification, intent,
           url_pattern, page_type, priority, tier, language="en"):
    """Add keyword if not duplicate and meets quality criteria."""
    kw_clean = " ".join(keyword.strip().split())
    kw_lower = kw_clean.lower()
    if kw_lower in seen or len(kw_lower) < 4:
        return
    seen.add(kw_lower)
    keywords.append({
        "keyword": kw_clean,
        "cluster": cluster,
        "sub_cluster": sub_cluster,
        "state": state,
        "qualification": qualification,
        "intent": intent,
        "url_pattern": url_pattern,
        "page_type": page_type,
        "priority": priority,
        "tier": tier,
        "language": language,
    })

def score_priority(demand, relevance):
    if demand == "high" and relevance == "high":
        return ("HIGH", 1)
    elif demand == "high" or relevance == "high":
        return ("MEDIUM", 2)
    else:
        return ("LOW", 3)


print("🔄 [1/12] Generating Government Jobs keywords (Target: ~25,000)...")

# --- 1. GOVERNMENT JOBS ---
YEAR_LIST = ["2025", "2026", "2027"]

for category, exams in GOV_EXAMS.items():
    for exam_name, exam_slug in exams:
        # Base exam × intents
        for intent_name, intent_slug, intent_type in EXAM_INTENTS:
            kw = f"{exam_name} {intent_name}"
            url = f"/jobs/{exam_slug}/{intent_slug}/"
            add_kw(kw, "Government Jobs", category, "", "", intent_type,
                   url, "info", "HIGH", 1)
            
            # + years
            for year in YEAR_LIST:
                kw_y = f"{exam_name} {intent_name} {year}"
                url_y = f"/jobs/{exam_slug}/{intent_slug}-{year}/"
                add_kw(kw_y, "Government Jobs", category, "", "", intent_type,
                       url_y, "info", "HIGH", 1)
        
        # Exam × qualification
        for qual_name, qual_slug in QUALIFICATIONS[:18]:
            kw = f"{exam_name} {qual_name}"
            url = f"/jobs/{exam_slug}/{qual_slug}/"
            add_kw(kw, "Government Jobs", category, "", qual_name, "listing",
                   url, "listing", "MEDIUM", 2)
            
            kw2 = f"{exam_name} eligibility for {qual_name}"
            add_kw(kw2, "Government Jobs", category, "", qual_name, "info",
                   f"/jobs/{exam_slug}/eligibility-{qual_slug}/", "info", "MEDIUM", 2)
            
            kw3 = f"{exam_name} vacancy for {qual_name} 2026"
            add_kw(kw3, "Government Jobs", category, "", qual_name, "listing",
                   f"/jobs/{exam_slug}/vacancy-{qual_slug}-2026/", "listing", "HIGH", 1)

        # Category cutoffs & relaxations
        for cat in ["General", "OBC", "SC", "ST", "EWS", "Female", "Ex-Servicemen"]:
            add_kw(f"{exam_name} cutoff for {cat} category", "Government Jobs", category, "", "", "info",
                   f"/jobs/{exam_slug}/cutoff-{cat.lower()}/", "info", "MEDIUM", 2)
            add_kw(f"{exam_name} age limit for {cat} candidates", "Government Jobs", category, "", "", "info",
                   f"/jobs/{exam_slug}/age-limit-{cat.lower()}/", "info", "MEDIUM", 2)

        # Guides & preparation
        guide_intents = [
            f"how to prepare for {exam_name} without coaching",
            f"how to apply for {exam_name} online form",
            f"how to crack {exam_name} in first attempt",
            f"{exam_name} syllabus and exam pattern in Hindi",
            f"{exam_name} best books for preparation",
            f"{exam_name} free mock test series",
            f"{exam_name} previous 10 year question papers with solution",
            f"{exam_name} salary slip after 7th pay commission",
            f"{exam_name} medical and physical test standards",
            f"{exam_name} negative marking rules",
            f"{exam_name} job profile and promotion hierarchy",
            f"{exam_name} typing test speed criteria",
            f"{exam_name} normalisation formula explained",
            f"{exam_name} dress code rules for male and female candidates",
            f"{exam_name} shift timings and reporting time instructions",
            f"{exam_name} documents to carry on exam day",
            f"{exam_name} self declaration form format download",
            f"is calculator allowed in {exam_name} online exam",
            f"{exam_name} safe score and expected cut off target",
            f"{exam_name} certificate verification proforma format"
        ]
        for g in guide_intents:
            add_kw(g, "Government Jobs", category, "", "", "guide",
                   f"/jobs/{exam_slug}/guide/", "guide", "MEDIUM", 2)


print("🔄 [2/12] Generating State & District Jobs keywords (Target: ~18,000)...")

# --- 2. STATE & DISTRICT JOBS ---
STATE_DEPTS = [
    ("police", "police-jobs"), ("teacher", "teacher-jobs"), ("health department", "health-jobs"),
    ("revenue patwari lekhpal", "patwari-jobs"), ("court clerk stenographer", "court-jobs"),
    ("panchayat sachiv vdo", "panchayat-jobs"), ("junior engineer PWD electricity", "je-jobs"),
    ("forest guard vanrakshak", "forest-jobs"), ("anganwadi sevika sahayika", "anganwadi-jobs"),
    ("transport driver conductor", "driver-jobs"), ("agriculture krishi vibhag", "agriculture-jobs"),
    ("staff nurse ANM GNM", "nurse-jobs"), ("pharmacist medical officer", "pharmacist-jobs"),
    ("lab technician assistant", "lab-technician-jobs"), ("computer operator DEO", "deo-jobs"),
    ("electrician lineman power corp", "lineman-jobs"), ("sweeper peon group d", "group-d-jobs"),
    ("block development BDO", "bdo-jobs"), ("excise abkari sub inspector", "excise-jobs"),
    ("jail warder guard", "jail-warder-jobs")
]

for state_name, state_slug in ALL_STATES_UTS:
    for intent_name, intent_slug, ptype in STATE_JOB_INTENTS:
        kw = f"{state_name} {intent_name}"
        url = f"/jobs/{state_slug}/{intent_slug}/"
        add_kw(kw, "State Jobs", state_name, state_name, "", "listing", url, ptype, "HIGH", 1)
        
        for yr in YEAR_LIST:
            kw_y = f"{state_name} {intent_name} {yr}"
            add_kw(kw_y, "State Jobs", state_name, state_name, "", "listing",
                   f"/jobs/{state_slug}/{intent_slug}-{yr}/", ptype, "HIGH", 1)

    for qual_name, qual_slug in QUALIFICATIONS:
        kw = f"{state_name} government jobs {qual_name}"
        url = f"/jobs/{state_slug}/govt-jobs-{qual_slug}/"
        add_kw(kw, "State Jobs", state_name, state_name, qual_name, "listing", url, "listing", "HIGH", 1)
        
        for yr in ["2025", "2026"]:
            add_kw(f"{state_name} govt jobs for {qual_name} {yr}", "State Jobs", state_name, state_name, qual_name, "listing",
                   f"/jobs/{state_slug}/govt-jobs-{qual_slug}-{yr}/", "listing", "HIGH", 1)
            add_kw(f"{state_name} sarkari naukri {qual_name} {yr}", "State Jobs", state_name, state_name, qual_name, "listing",
                   f"/jobs/{state_slug}/govt-jobs-{qual_slug}-{yr}/", "listing", "HIGH", 1)

    for dept_name, dept_slug in STATE_DEPTS:
        add_kw(f"{state_name} {dept_name} vacancy 2026", "State Jobs", state_name, state_name, "", "listing",
               f"/jobs/{state_slug}/{dept_slug}-2026/", "listing", "HIGH", 1)
        add_kw(f"{state_name} {dept_name} recruitment notification", "State Jobs", state_name, state_name, "", "listing",
               f"/jobs/{state_slug}/{dept_slug}/", "listing", "MEDIUM", 2)
        add_kw(f"{state_name} {dept_name} salary and eligibility", "State Jobs", state_name, state_name, "", "info",
               f"/jobs/{state_slug}/{dept_slug}-eligibility/", "info", "MEDIUM", 2)
        add_kw(f"{state_name} {dept_name} apply online form 2026", "State Jobs", state_name, state_name, "", "action",
               f"/jobs/{state_slug}/{dept_slug}-apply/", "action", "HIGH", 1)

# District-level targeted keywords
for dist_name, state_slug in MAJOR_DISTRICTS:
    for q_name, q_slug in QUALIFICATIONS[:10]:
        add_kw(f"{dist_name} job vacancy for {q_name}", "State Jobs", dist_name, dist_name, q_name, "listing",
               f"/jobs/{state_slug}/{dist_name.lower()}-{q_slug}/", "listing", "MEDIUM", 2)
    for dept_name, dept_slug in STATE_DEPTS[:8]:
        add_kw(f"{dist_name} {dept_name} bharti 2026", "State Jobs", dist_name, dist_name, "", "listing",
               f"/jobs/{state_slug}/{dist_name.lower()}-{dept_slug}/", "listing", "MEDIUM", 2)


print("🔄 [3/12] Generating Exam, Admit Card, Results & Cutoff keywords (Target: ~12,000)...")

# --- 3. EXAM / ADMIT CARD / RESULTS ---
all_exams = []
for exams in GOV_EXAMS.values():
    all_exams.extend(exams)

EXAM_ACTIONS_EXPANDED = [
    ("admit card download link", "admit-card", "action"),
    ("hall ticket call letter download", "hall-ticket", "action"),
    ("exam date and shift schedule", "exam-date", "info"),
    ("exam center and city intimation slip", "city-intimation", "action"),
    ("official answer key and response sheet", "answer-key", "info"),
    ("objection raise link for answer key", "answer-key-objection", "action"),
    ("final result and merit list PDF", "result", "action"),
    ("score card and marksheet login", "score-card", "action"),
    ("expected and official cut off marks", "cutoff", "info"),
    ("category wise cutoff marks General OBC SC ST", "cutoff-category", "info"),
    ("document verification schedule and list", "dv-schedule", "info"),
    ("medical exam date and admit card", "medical-admit-card", "action"),
    ("joining letter and merit ranking", "joining-letter", "info"),
    ("previous year cutoff marks trend", "cutoff-trend", "info"),
    ("selection list PDF download", "selection-list", "action")
]

for exam_name, exam_slug in all_exams:
    for action_name, action_slug, act_type in EXAM_ACTIONS_EXPANDED:
        kw = f"{exam_name} {action_name}"
        url = f"/exams/{exam_slug}/{action_slug}/"
        add_kw(kw, "Exam Results", "Admit Cards & Results", "", "", act_type, url, "action", "HIGH", 1)
        
        for yr in YEAR_LIST:
            kw_y = f"{exam_name} {action_name} {yr}"
            add_kw(kw_y, "Exam Results", "Admit Cards & Results", "", "", act_type,
                   f"/exams/{exam_slug}/{action_slug}-{yr}/", "action", "HIGH", 1)

    for step in ["how to download admit card online", "how to check result by roll number",
                 "how to download score card with registration id", "how to calculate normalised marks"]:
        add_kw(f"{exam_name} {step}", "Exam Results", "Guides", "", "", "guide",
               f"/exams/{exam_slug}/guide/", "guide", "MEDIUM", 2)


print("🔄 [4/12] Generating MCA/BCA/College & University keywords (Target: ~22,000)...")

# --- 4. MCA/BCA/COLLEGE ---
DEGREES_TO_MAP = [
    ("MCA", "mca", "MCA_BCA_CS"),
    ("BCA", "bca", "MCA_BCA_CS"),
    ("B.Tech CSE", "btech-cse", "MCA_BCA_CS"),
    ("B.Tech IT", "btech-it", "MCA_BCA_CS"),
    ("B.Sc Computer Science", "bsc-cs", "MCA_BCA_CS"),
    ("B.Tech", "btech", "SCIENCE_ENGG"),
    ("B.Sc", "bsc", "SCIENCE_ENGG"),
    ("B.Com", "bcom", "COMMERCE_MGMT"),
    ("B.Com Honours", "bcom-hons", "COMMERCE_MGMT"),
    ("MBA", "mba", "COMMERCE_MGMT"),
    ("BBA", "bba", "COMMERCE_MGMT"),
    ("BA", "ba", "ARTS_HUMANITIES"),
    ("Diploma Engineering", "polytechnic", "SCIENCE_ENGG")
]

for deg_name, deg_slug, stream_key in DEGREES_TO_MAP:
    subjects = SUBJECTS_BY_STREAM[stream_key]
    for sub_name, sub_slug in subjects:
        for c_name, c_slug, c_type in ACADEMIC_CONTENT_INTENTS:
            kw = f"{deg_name} {sub_name} {c_name}"
            url = f"/students/{deg_slug}/{sub_slug}/{c_slug}/"
            p, t = score_priority("high" if deg_name in ["MCA", "BCA", "B.Tech CSE"] else "medium", "high")
            add_kw(kw, "College", deg_name, "", "", c_type, url, "resource", p, t)

        # Subject Base
        add_kw(f"{deg_name} {sub_name} study material", "College", deg_name, "", "", "resource",
               f"/students/{deg_slug}/{sub_slug}/", "resource", "HIGH", 1)

# Semester syllabus and subject guides
for deg_name, deg_slug in [("MCA", "mca"), ("BCA", "bca"), ("B.Tech", "btech"), ("B.Com", "bcom"), ("BBA", "bba"), ("MBA", "mba")]:
    for sem in range(1, 9):
        sem_str = f"semester {sem}"
        for item in ["syllabus PDF", "subjects list", "notes handwritten", "question papers solved", "important questions", "project topics", "lab manual"]:
            add_kw(f"{deg_name} {sem_str} {item}", "College", deg_name, "", "", "resource",
                   f"/students/{deg_slug}/sem-{sem}/{item.replace(' ', '-')}/", "resource", "MEDIUM", 2)

# Deep topic level viva, lab, and MCQ questions for MCA / BCA / B.Tech CSE
CS_CORE_TOPICS = [
    ("Java", [
        "OOPs Concepts", "Inheritance", "Polymorphism", "Abstraction and Encapsulation", "Interfaces and Abstract Classes",
        "Exception Handling try catch throw", "Multithreading and Concurrency", "Collections ArrayList HashMap LinkedList",
        "Generics and Streams API", "JDBC Database Connectivity", "Servlets and JSP Lifecycle", "Spring Boot REST Controller",
        "Hibernate JPA ORM Mapping", "Lambda Expressions", "String Constant Pool Immutability", "Garbage Collection JVM Architecture"
    ]),
    ("Python", [
        "Data Types List Tuple Set Dictionary", "List Comprehension and Generators", "Decorators and Closures",
        "Object Oriented Programming Classes", "Exception Handling try except", "File Handling Read Write",
        "NumPy Arrays and Indexing", "Pandas DataFrame and Series", "Matplotlib and Seaborn Visualisation",
        "Django Models and Views", "Flask Routing and REST API", "Lambda Map Filter Reduce", "Regex Pattern Matching", "Multiprocessing vs Multithreading"
    ]),
    ("DBMS", [
        "ER Diagram and Cardinality", "Relational Model and Constraints", "Normalization 1NF 2NF 3NF BCNF",
        "SQL DDL DML DCL Commands", "SQL Joins Inner Left Right Full", "Subqueries and Correlated Subqueries",
        "Views and Indexes Clustered Non-Clustered", "Stored Procedures and Triggers", "ACID Properties in DBMS",
        "Concurrency Control Locking 2PL", "Deadlock Prevention and Detection", "Transactions and Recovery Rollback",
        "B Tree and B+ Tree Indexing", "RDBMS vs NoSQL MongoDB"
    ]),
    ("Data Structures", [
        "Arrays and Dynamic Arrays", "Singly Doubly Circular Linked List", "Stack Push Pop Peek Infix to Postfix",
        "Queue Linear Circular Deque Priority", "Binary Tree Traversals Inorder Preorder Postorder",
        "Binary Search Tree BST Search Insert Delete", "AVL Tree Balancing and Rotations", "Heap Min Heap Max Heap Heapify",
        "Graph Representation Adjacency Matrix List", "Graph BFS and DFS Traversal", "Dijkstra Shortest Path Algorithm",
        "Sorting Bubble Insertion Selection Quick Merge", "Binary Search and Linear Search", "Dynamic Programming Memoization Tabulation"
    ]),
    ("Operating System", [
        "Process vs Thread PCB Context Switch", "CPU Scheduling FCFS SJF Round Robin Priority", "Process Synchronization Critical Section Mutex Semaphore",
        "Deadlock Banker's Algorithm Detection Recovery", "Memory Management Paging and Segmentation", "Virtual Memory Page Replacement FIFO LRU Optimal",
        "File System Architecture Inode", "Disk Scheduling FCFS SSTF SCAN LOOK", "System Calls fork exec wait"
    ]),
    ("Computer Networks", [
        "OSI 7 Layers Model Architecture", "TCP IP Protocol Suite Comparison", "IP Addressing Subnetting CIDR Calculation",
        "Routing Algorithms Distance Vector Link State", "TCP 3-Way Handshake vs UDP", "Flow Control Stop and Wait Sliding Window",
        "Error Detection CRC Checksum Parity", "DNS HTTP HTTPS FTP SMTP Protocols", "Network Security Firewalls SSL TLS"
    ])
]

for subject_title, topics in CS_CORE_TOPICS:
    for topic_item in topics:
        for deg in ["MCA", "BCA", "B.Tech CSE"]:
            slug_deg = deg.lower().replace(' ', '-')
            slug_topic = topic_item.lower().replace(' ', '-')
            add_kw(f"{deg} {subject_title} {topic_item} viva questions and answers", "College", deg, "", "", "resource",
                   f"/students/{slug_deg}/{subject_title.lower()}/{slug_topic}/", "resource", "HIGH", 1)
            add_kw(f"{deg} {subject_title} {topic_item} practical programs code", "College", deg, "", "", "resource",
                   f"/students/{slug_deg}/{subject_title.lower()}/{slug_topic}/", "resource", "MEDIUM", 2)
            add_kw(f"{deg} {subject_title} {topic_item} MCQ test quiz", "College", deg, "", "", "tool",
                   f"/students/{slug_deg}/{subject_title.lower()}/{slug_topic}/", "tool", "HIGH", 1)
            add_kw(f"{deg} {subject_title} {topic_item} handwritten short notes", "College", deg, "", "", "resource",
                   f"/students/{slug_deg}/{subject_title.lower()}/{slug_topic}/", "resource", "HIGH", 1)

# University specific syllabus and grading
for uni_name, uni_slug in UNIVERSITIES_LIST:
    for deg in ["MCA", "BCA", "B.Tech", "B.Com", "MBA", "B.Sc", "BA"]:
        add_kw(f"{uni_name} {deg} CGPA to percentage formula", "College", "University", "", "", "tool",
               f"/calculators/cgpa-{uni_slug}/", "tool", "HIGH", 1)
        add_kw(f"{uni_name} {deg} syllabus PDF 2026", "College", "University", "", "", "info",
               f"/students/{deg.lower().replace('.', '')}/syllabus-{uni_slug}/", "info", "MEDIUM", 2)
        add_kw(f"{uni_name} {deg} previous year question papers", "College", "University", "", "", "resource",
               f"/students/{deg.lower().replace('.', '')}/papers-{uni_slug}/", "resource", "MEDIUM", 2)
        add_kw(f"{uni_name} grading system and marks distribution", "College", "University", "", "", "info",
               f"/students/grading-{uni_slug}/", "info", "LOW", 3)


print("🔄 [5/12] Generating PDF Tools keywords (Target: ~5,500)...")

# --- 5. PDF TOOLS ---
for tool_name, tool_slug in PDF_TOOLS:
    add_kw(tool_name, "PDF Tools", "PDF", "", "", "tool", f"/tools/pdf/{tool_slug}/", "tool", "HIGH", 1)
    for mod in PDF_MODIFIERS:
        add_kw(f"{tool_name} {mod}", "PDF Tools", "PDF", "", "", "tool", f"/tools/pdf/{tool_slug}/", "tool", "HIGH", 1)
        add_kw(f"best {tool_name} {mod}", "PDF Tools", "PDF", "", "", "tool", f"/tools/pdf/{tool_slug}/", "tool", "MEDIUM", 2)
        add_kw(f"free online {tool_name}", "PDF Tools", "PDF", "", "", "tool", f"/tools/pdf/{tool_slug}/", "tool", "HIGH", 1)
    
    for device in ["on mobile phone", "on android", "on iphone", "for government forms", "without losing quality", "100 percent free safe"]:
        add_kw(f"{tool_name} {device}", "PDF Tools", "PDF", "", "", "tool", f"/tools/pdf/{tool_slug}/", "tool", "MEDIUM", 2)

for target_kb in ["50KB", "100KB", "150KB", "200KB", "300KB", "500KB", "1MB", "2MB", "5MB", "10MB"]:
    for prefix in ["compress pdf to", "reduce pdf file size below", "resize pdf under", "convert document to pdf under"]:
        add_kw(f"{prefix} {target_kb}", "PDF Tools", "PDF", "", "", "tool", "/tools/pdf/pdf-compressor/", "tool", "HIGH", 1)


print("🔄 [6/12] Generating Image & Photo Tools keywords (Target: ~5,000)...")

# --- 6. IMAGE & PHOTO TOOLS ---
for tool_name, tool_slug in IMAGE_TOOLS:
    add_kw(tool_name, "Image Tools", "Image", "", "", "tool", f"/tools/image/{tool_slug}/", "tool", "HIGH", 1)
    for mod in ["online", "free", "online free", "tool without signup", "in high quality", "batch converter"]:
        add_kw(f"{tool_name} {mod}", "Image Tools", "Image", "", "", "tool", f"/tools/image/{tool_slug}/", "tool", "HIGH", 1)

for kb in ["10KB", "15KB", "20KB", "25KB", "30KB", "35KB", "40KB", "50KB", "60KB", "75KB", "80KB", "100KB", "150KB", "200KB", "300KB", "500KB"]:
    for verb in ["resize image to", "compress photo to", "reduce photo size in kb to", "convert jpg image to", "resize jpeg photo under"]:
        add_kw(f"{verb} {kb}", "Image Tools", "Image", "", "", "tool", "/tools/image/image-compressor/", "tool", "HIGH", 1)

for dim_str in ["100x100 px", "140x60 px", "150x70 px", "200x230 px", "200x300 px", "300x300 px", "350x450 px", "400x400 px", "500x500 px", "600x600 px", "3.5x4.5 cm", "2x2 inch", "35x45 mm", "51x51 mm"]:
    for act in ["resize photo to", "crop image to", "passport photo size", "signature dimension"]:
        add_kw(f"{act} {dim_str}", "Image Tools", "Dimensions", "", "", "tool", "/tools/image/image-resizer/", "tool", "HIGH", 1)


print("🔄 [7/12] Generating Cyber Café, Form & Certificate Tools (Target: ~7,000)...")

# --- 7. CYBER CAFÉ & FORMS ---
for cert_name, cert_slug in CYBER_CAFE_CERTIFICATES:
    for intent in ["online apply process", "documents required list", "status check portal", "download certificate online", "application form format PDF", "correction online"]:
        add_kw(f"{cert_name} {intent}", "Cyber Cafe", "Certificates", "", "", "action",
               f"/cyber-cafe/certificates/{cert_slug}/", "action", "HIGH", 1)
    
    for state_name, state_slug in ALL_STATES_UTS:
        add_kw(f"{state_name} {cert_name} online apply 2026", "Cyber Cafe", "Certificates", state_name, "", "action",
               f"/cyber-cafe/certificates/{state_slug}-{cert_slug}/", "action", "HIGH", 1)
        add_kw(f"{state_name} {cert_name} download status check portal", "Cyber Cafe", "Certificates", state_name, "", "action",
               f"/cyber-cafe/certificates/{state_slug}-{cert_slug}/", "action", "HIGH", 1)
        add_kw(f"{state_name} {cert_name} affidavit declaration format PDF", "Cyber Cafe", "Certificates", state_name, "", "resource",
               f"/cyber-cafe/certificates/{state_slug}-{cert_slug}/", "resource", "MEDIUM", 2)

# Photo and signature for all top competitive exams
for exam_name, exam_slug in all_exams:
    for photo_q in [
        f"{exam_name} photo and signature size in KB",
        f"{exam_name} photo dimension width and height in px",
        f"{exam_name} signature resize tool online free",
        f"{exam_name} photo date and name stamp requirements",
        f"{exam_name} thumb impression size and format",
        f"{exam_name} live photo capture upload guidelines",
        f"how to resize photo and signature for {exam_name} form",
        f"{exam_name} photo upload error solution"
    ]:
        add_kw(photo_q, "Cyber Cafe", "Form Photo Specs", "", "", "tool",
               f"/cyber-cafe/photo/specs-{exam_slug}/", "tool", "HIGH", 1)

# Cyber café print studio & A4 sheet layouts
for n_photos in ["4", "6", "8", "12", "16", "24", "30", "32"]:
    add_kw(f"{n_photos} passport photos on A4 sheet maker", "Cyber Cafe", "Print Studio", "", "", "tool",
           "/cyber-cafe/photo-print-a4/", "tool", "HIGH", 1)
    add_kw(f"print {n_photos} passport size photos on single page", "Cyber Cafe", "Print Studio", "", "", "tool",
           "/cyber-cafe/photo-print-a4/", "tool", "HIGH", 1)


print("🔄 [8/12] Generating Calculators keywords (Target: ~8,500)...")

# --- 8. CALCULATORS ---
all_calcs = EDUCATION_CALCS + FINANCE_CALCS + GENERAL_CALCS

for calc_name, calc_slug in all_calcs:
    cluster = "Calculators"
    sub = "Education" if calc_name in [c[0] for c in EDUCATION_CALCS] else \
          "Finance" if calc_name in [c[0] for c in FINANCE_CALCS] else "General"
    
    add_kw(calc_name, cluster, sub, "", "", "tool", f"/tools/calculators/{calc_slug}/", "tool", "HIGH", 1)
    for mod in CALC_MODIFIERS:
        add_kw(f"{calc_name} {mod}", cluster, sub, "", "", "tool", f"/tools/calculators/{calc_slug}/", "tool", "HIGH", 1)
    add_kw(f"how to calculate {calc_name.replace(' calculator', '')} with formula", cluster, sub, "", "", "guide",
           f"/tools/calculators/{calc_slug}/", "guide", "MEDIUM", 2)

# Specific university CGPA calculators
for uni_name, uni_slug in UNIVERSITIES_LIST:
    for scale in ["10 point scale", "percentage converter", "SGPA to CGPA"]:
        add_kw(f"{uni_name} CGPA {scale} online calculator", "Calculators", "Education", "", "", "tool",
               f"/tools/calculators/cgpa-{uni_slug}/", "tool", "HIGH", 1)

# Financial combinations
LOAN_AMOUNTS = ["50000", "1 lakh", "2 lakh", "3 lakh", "5 lakh", "7 lakh", "10 lakh", "15 lakh", "20 lakh", "25 lakh", "30 lakh", "40 lakh", "50 lakh", "75 lakh", "1 crore"]
LOAN_TENURES = ["6 months", "1 year", "2 years", "3 years", "5 years", "7 years", "10 years", "15 years", "20 years", "25 years", "30 years"]
LOAN_TYPES = ["home loan", "car loan", "personal loan", "education loan", "bike loan", "gold loan", "business loan"]

for ltype in LOAN_TYPES:
    for amt in LOAN_AMOUNTS:
        add_kw(f"{ltype} EMI calculator for {amt}", "Calculators", "Finance", "", "", "tool",
               "/tools/calculators/emi-calculator/", "tool", "HIGH", 1)
        for ten in LOAN_TENURES[:6]:
            add_kw(f"{ltype} EMI for {amt} for {ten}", "Calculators", "Finance", "", "", "tool",
                   "/tools/calculators/emi-calculator/", "tool", "MEDIUM", 2)

# SIP & Mutual Fund targets
for sip_amt in ["500", "1000", "1500", "2000", "2500", "3000", "4000", "5000", "7500", "10000", "15000", "20000", "25000", "50000"]:
    for duration in ["1 year", "3 years", "5 years", "7 years", "10 years", "15 years", "20 years", "25 years", "30 years"]:
        add_kw(f"SIP return calculator {sip_amt} per month for {duration}", "Calculators", "Finance", "", "", "tool",
               "/tools/calculators/sip-calculator/", "tool", "MEDIUM", 2)

# Salary breakdown CTC in India
for lpa in ["2.5", "3.0", "3.6", "4.0", "4.5", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0", "12.0", "15.0", "18.0", "20.0", "25.0", "30.0", "40.0", "50.0"]:
    add_kw(f"{lpa} LPA in hand salary calculator after tax and PF", "Calculators", "Finance", "", "", "tool",
           "/tools/calculators/salary-calculator/", "tool", "HIGH", 1)
    add_kw(f"{lpa} LPA monthly take home salary in India", "Calculators", "Finance", "", "", "tool",
           "/tools/calculators/salary-calculator/", "tool", "HIGH", 1)
    add_kw(f"how much in hand for {lpa} LPA CTC in new tax regime", "Calculators", "Finance", "", "", "guide",
           "/tools/calculators/salary-calculator/", "guide", "MEDIUM", 2)

# Age eligibility calculator for top competitive exams
for ex_name, ex_slug in all_exams[:40]:
    for cat in ["General", "OBC", "SC", "ST", "EWS"]:
        add_kw(f"age calculator for {ex_name} {cat} category 2026", "Calculators", "Education", "", "", "tool",
               f"/tools/calculators/age-{ex_slug}/", "tool", "HIGH", 1)
        add_kw(f"am I eligible for {ex_name} age limit check {cat}", "Calculators", "Education", "", "", "tool",
               f"/tools/calculators/age-{ex_slug}/", "tool", "HIGH", 1)

# Attendance calculations
for course in ["B.Tech", "BCA", "MCA", "B.Com", "B.Sc", "BA", "MBA", "MBBS", "LLB", "Diploma"]:
    for target_pct in ["75%", "80%", "85%", "65%"]:
        add_kw(f"how to calculate {target_pct} attendance for {course}", "Calculators", "Education", "", "", "guide",
               "/tools/calculators/attendance-calculator/", "guide", "MEDIUM", 2)
        add_kw(f"how many classes to attend for {target_pct} in {course}", "Calculators", "Education", "", "", "guide",
               "/tools/calculators/attendance-calculator/", "guide", "HIGH", 1)


print("🔄 [9/12] Generating Resume & Career keywords (Target: ~6,000)...")

# --- 9. RESUME & CAREER ---
for rtype in RESUME_TYPES:
    for intent_name, intent_slug in RESUME_INTENTS:
        add_kw(f"{rtype} {intent_name} download free", "Resume Career", "Resume", "", "", "resource",
               f"/career/resume/{rtype.lower().replace(' ', '-').replace('.', '')}-{intent_slug}/", "resource", "HIGH", 1)
        add_kw(f"{rtype} {intent_name} in Word Doc format", "Resume Career", "Resume", "", "", "resource",
               f"/career/resume/{rtype.lower().replace(' ', '-').replace('.', '')}-{intent_slug}/", "resource", "MEDIUM", 2)
    
    add_kw(f"{rtype} resume builder with PDF export", "Resume Career", "Resume", "", "", "tool",
           f"/career/resume/builder-{rtype.lower().replace(' ', '-').replace('.', '')}/", "tool", "HIGH", 1)
    add_kw(f"top skills to put on resume for {rtype}", "Resume Career", "Resume", "", "", "guide",
           f"/career/resume/{rtype.lower().replace(' ', '-').replace('.', '')}-skills/", "guide", "HIGH", 1)
    add_kw(f"resume headline and summary for {rtype} fresher", "Resume Career", "Resume", "", "", "guide",
           f"/career/resume/{rtype.lower().replace(' ', '-').replace('.', '')}-summary/", "guide", "MEDIUM", 2)

# Career roadmap and interview questions
for role in career_roles:
    for c_intent, c_slug in CAREER_CONTENT:
        add_kw(f"{role} {c_intent} 2026", "Resume Career", "Career", "", "", "guide",
               f"/career/{role.lower().replace('/', '-').replace(' ', '-')}/{c_slug}/", "guide", "HIGH", 1)
    add_kw(f"how to become {role} step by step roadmap", "Resume Career", "Career", "", "", "guide",
           f"/career/{role.lower().replace('/', '-').replace(' ', '-')}/roadmap/", "guide", "HIGH", 1)
    add_kw(f"{role} average salary for freshers in India", "Resume Career", "Career", "", "", "info",
           f"/career/{role.lower().replace('/', '-').replace(' ', '-')}/salary/", "info", "HIGH", 1)


print("🔄 [10/12] Generating Developer & Data Tools keywords (Target: ~5,500)...")

# --- 10. DEVELOPER TOOLS ---
for tool_name, tool_slug in DEV_TOOLS:
    add_kw(tool_name, "Developer Tools", "Developer", "", "", "tool", f"/tools/developer/{tool_slug}/", "tool", "HIGH", 1)
    for mod in DEV_MODIFIERS:
        add_kw(f"{tool_name} {mod}", "Developer Tools", "Developer", "", "", "tool", f"/tools/developer/{tool_slug}/", "tool", "HIGH", 1)
        add_kw(f"best free {tool_name} online", "Developer Tools", "Developer", "", "", "tool", f"/tools/developer/{tool_slug}/", "tool", "HIGH", 1)
    
    add_kw(f"how to use {tool_name} with example", "Developer Tools", "Developer", "", "", "guide",
           f"/tools/developer/{tool_slug}/", "guide", "LOW", 3)

# Regex patterns
REGEX_PATTERNS = [
    "email address", "Indian phone mobile number", "strong password", "URL web address",
    "PAN card number", "Aadhaar card number", "GSTIN number", "IP address IPv4 IPv6",
    "date format DD MM YYYY", "hex color code", "postal pincode India", "credit debit card number",
    "alphanumeric only", "letters only without spaces", "numbers only with decimals",
    "UUID GUID", "HTML tags remover", "slug url string"
]
for reg in REGEX_PATTERNS:
    add_kw(f"regular expression regex for {reg}", "Developer Tools", "Regex", "", "", "tool",
           "/tools/developer/regex-tester/", "tool", "HIGH", 1)
    add_kw(f"{reg} regex pattern and validation example", "Developer Tools", "Regex", "", "", "guide",
           "/tools/developer/regex-tester/", "guide", "MEDIUM", 2)

# Common Developer errors
PROGRAMMING_LANGS = ["Java", "Python", "JavaScript", "C++", "C#", "PHP", "SQL", "TypeScript", "React", "NodeJS"]
COMMON_ERRORS = [
    "NullPointerException", "TypeError cannot read properties of undefined", "IndexOutOfBoundsException",
    "SyntaxError unexpected token", "ClassNotFoundException", "StackOverflowError", "Segmentation fault core dumped",
    "CORS policy error blocked by access control", "cannot find symbol variable", "fatal error out of memory",
    "module not found error", "database connection refused", "SQL syntax error near", "unhandled promise rejection"
]
for lang in PROGRAMMING_LANGS:
    for err in COMMON_ERRORS:
        add_kw(f"{lang} {err} fix and solution", "Developer Tools", "Error Fix", "", "", "guide",
               f"/tools/developer/{lang.lower()}-errors/", "guide", "MEDIUM", 2)

# Data converters & encoders
DATA_CONVERSIONS = [
    ("JSON to CSV", "json-to-csv"), ("CSV to JSON", "csv-to-json"), ("JSON to XML", "json-to-xml"),
    ("XML to JSON", "xml-to-json"), ("JSON to YAML", "json-to-yaml"), ("YAML to JSON", "yaml-to-json"),
    ("JSON to SQL Table", "json-to-sql"), ("SQL Query to JSON", "sql-to-json"),
    ("JSON to TypeScript Interface", "json-to-typescript"), ("JSON to Java POJO Class", "json-to-java"),
    ("JSON to Python Dict", "json-to-python"), ("JSON to Go Struct", "json-to-go"),
    ("Base64 to Image PNG JPG", "base64-to-image"), ("Image to Base64 String", "image-to-base64"),
    ("URL Encode String Online", "url-encode"), ("URL Decode Online", "url-decode"),
    ("HTML Entity Encode", "html-encode"), ("HTML Entity Decode", "html-decode"),
    ("Hex to String ASCII", "hex-to-string"), ("String to Hex Converter", "string-to-hex"),
    ("Binary to Text Converter", "binary-to-text"), ("Text to Binary 01", "text-to-binary"),
    ("MD5 Hash Generator Online", "md5-hash"), ("SHA256 Hash Generator", "sha256-hash"),
    ("SHA512 Hash Checksum", "sha512-hash"), ("JWT Token Decode and Verify", "jwt-decoder"),
    ("Cron Expression Generator Online", "cron-generator"), ("Markdown to HTML Converter", "markdown-to-html"),
    ("HTML to Markdown Converter", "html-to-markdown"), ("CSS Minifier and Beautifier", "css-minifier"),
    ("JavaScript Obfuscator Deobfuscator", "js-deobfuscator"), ("SQL Query Formatter Beautifier", "sql-formatter")
]

for conv_name, conv_slug in DATA_CONVERSIONS:
    add_kw(conv_name, "Developer Tools", "Converters", "", "", "tool", f"/tools/developer/{conv_slug}/", "tool", "HIGH", 1)
    for mod in ["free online tool", "fast converter", "without server upload safe", "for programmers"]:
        add_kw(f"{conv_name} {mod}", "Developer Tools", "Converters", "", "", "tool", f"/tools/developer/{conv_slug}/", "tool", "HIGH", 1)


print("🔄 [11/12] Generating Scholarships keywords (Target: ~4,000)...")

# --- 11. SCHOLARSHIPS ---
for stype in SCHOLARSHIP_TYPES:
    for intent in SCHOLARSHIP_INTENTS:
        add_kw(f"{stype} {intent}", "Scholarships", stype, "", "", "listing",
               f"/scholarships/{stype.lower().replace(' ', '-')}/", "listing", "MEDIUM", 2)
    for yr in YEAR_LIST:
        add_kw(f"{stype} scholarship {yr} online apply last date", "Scholarships", stype, "", "", "action",
               f"/scholarships/{stype.lower().replace(' ', '-')}-{yr}/", "action", "HIGH", 1)

for state_name, state_slug in ALL_STATES_UTS[:25]:
    for q_name, q_slug in QUALIFICATIONS[:12]:
        add_kw(f"{state_name} scholarship for {q_name} students 2026", "Scholarships", state_name, state_name, q_name, "listing",
               f"/scholarships/{state_slug}/{q_slug}-2026/", "listing", "HIGH", 1)
        add_kw(f"{state_name} pre and post matric scholarship for {q_name}", "Scholarships", state_name, state_name, q_name, "listing",
               f"/scholarships/{state_slug}/{q_slug}/", "listing", "MEDIUM", 2)

for scheme in [
    "National Scholarship Portal NSP 2.0", "UP Scholarship Postmatric Pre Matric", "Bihar Post Matric Scholarship PMS",
    "e-Kalyan Jharkhand Scholarship", "MahaDBT Maharashtra Scholarship", "SSP Karnataka Scholarship",
    "Oasis West Bengal Scholarship", "Medhasoft Bihar Scholarship", "Prerana Odisha Scholarship",
    "Dr Ambedkar Post Matric Scholarship", "Begum Hazrat Mahal National Scholarship", "Central Sector Scheme CSSS",
    "AICTE Pragati Scholarship for Girls", "AICTE Saksham Scholarship for Divyang", "Ishan Uday Special Scholarship for NER",
    "Prime Minister Special Scholarship Scheme PMSSS", "Inspire Scholarship SHE DST", "Kotak Kanya Scholarship",
    "HDFC Badhte Kadam Scholarship", "Reliance Foundation Undergraduate Postgraduate Scholarship", "Tata Trust Medical and Engineering Scholarship"
]:
    slug = scheme.lower().replace(' ', '-').replace('.', '')
    add_kw(f"{scheme} 2026 apply online", "Scholarships", "Schemes", "", "", "action", f"/scholarships/{slug}/", "action", "HIGH", 1)
    add_kw(f"{scheme} eligibility criteria and family income limit", "Scholarships", "Schemes", "", "", "info", f"/scholarships/{slug}/eligibility/", "info", "HIGH", 1)
    add_kw(f"{scheme} application status check login", "Scholarships", "Schemes", "", "", "action", f"/scholarships/{slug}/status/", "action", "HIGH", 1)
    add_kw(f"{scheme} documents required and bonafide certificate format", "Scholarships", "Schemes", "", "", "info", f"/scholarships/{slug}/documents/", "info", "MEDIUM", 2)
    add_kw(f"{scheme} amount and payment date PFMS", "Scholarships", "Schemes", "", "", "info", f"/scholarships/{slug}/amount/", "info", "MEDIUM", 2)


print("🔄 [12/12] Generating Hindi & High-Intent Long Tail keywords (Target: ~6,000)...")

# --- 12. HINDI & REGIONAL QUERIES ---
HINDI_STATES = [
    ("बिहार", "bihar"), ("उत्तर प्रदेश", "uttar-pradesh"), ("झारखंड", "jharkhand"),
    ("मध्य प्रदेश", "madhya-pradesh"), ("राजस्थान", "rajasthan"), ("हरियाणा", "haryana"),
    ("दिल्ली", "delhi"), ("छत्तीसगढ़", "chhattisgarh"), ("उत्तराखंड", "uttarakhand"),
    ("हिमाचल प्रदेश", "himachal-pradesh"), ("पश्चिम बंगाल", "west-bengal")
]

HINDI_INTENTS = [
    "सरकारी नौकरी 2026", "सरकारी भर्ती 2026", "लेटेस्ट सरकारी रिजल्ट", "एडमिट कार्ड डाउनलोड",
    "10वीं पास सरकारी जॉब", "12वीं पास सरकारी जॉब", "ग्रेजुएट सरकारी नौकरी", "पुलिस कांस्टेबल भर्ती",
    "शिक्षक भर्ती ऑनलाइन फॉर्म", "ऑनलाइन फॉर्म कैसे भरें", "पासपोर्ट फोटो साइज कैसे बनाएं",
    "हस्ताक्षर साइज कैसे छोटा करें", "आय प्रमाण पत्र ऑनलाइन आवेदन", "जाति प्रमाण पत्र कैसे बनाएं",
    "निवास प्रमाण पत्र ऑनलाइन", "राशन कार्ड में नाम कैसे जोड़ें", "स्कॉलरशिप ऑनलाइन फॉर्म 2026"
]

for h_state, s_slug in HINDI_STATES:
    for h_intent in HINDI_INTENTS:
        add_kw(f"{h_state} {h_intent}", "State Jobs", h_state, h_state, "", "listing",
               f"/hi/jobs/{s_slug}/", "listing", "HIGH", 1, "hi")

# Top exam Hindi queries
for ex_name, ex_slug in all_exams[:40]:
    add_kw(f"{ex_name} का फॉर्म कब निकलेगा 2026", "Government Jobs", "Hindi", "", "", "info", f"/hi/jobs/{ex_slug}/", "info", "HIGH", 1, "hi")
    add_kw(f"{ex_name} एडमिट कार्ड कैसे डाउनलोड करें", "Exam Results", "Hindi", "", "", "action", f"/hi/exams/{ex_slug}/", "action", "HIGH", 1, "hi")
    add_kw(f"{ex_name} का रिजल्ट कब आएगा", "Exam Results", "Hindi", "", "", "action", f"/hi/exams/{ex_slug}/", "action", "HIGH", 1, "hi")
    add_kw(f"{ex_name} सिलेबस और परीक्षा पैटर्न हिंदी में", "Government Jobs", "Hindi", "", "", "info", f"/hi/jobs/{ex_slug}-syllabus/", "info", "HIGH", 1, "hi")
    add_kw(f"{ex_name} वेतन 7th पे स्केल", "Government Jobs", "Hindi", "", "", "info", f"/hi/jobs/{ex_slug}-salary/", "info", "MEDIUM", 2, "hi")


# ============================================================
# WRITE OUTPUT & GENERATE COMPREHENSIVE SUMMARY
# ============================================================

print(f"\n✅ Total unique keywords generated: {len(keywords):,}")

# Sort by tier then priority
tier_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
keywords.sort(key=lambda x: (x["tier"], tier_order.get(x["priority"], 3), x["cluster"], x["keyword"]))

# Write CSV
print(f"📝 Writing CSV to {OUTPUT_FILE}...")
fieldnames = ["keyword", "cluster", "sub_cluster", "state", "qualification",
              "intent", "url_pattern", "page_type", "priority", "tier", "language"]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(keywords)

# Write summary
print(f"📊 Writing summary to {SUMMARY_FILE}...")
cluster_counts = {}
tier_counts = {1: 0, 2: 0, 3: 0}
priority_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
language_counts = {"en": 0, "hi": 0}
page_type_counts = {}
intent_counts = {}

for kw in keywords:
    cluster = kw["cluster"]
    cluster_counts[cluster] = cluster_counts.get(cluster, 0) + 1
    tier_counts[kw["tier"]] = tier_counts.get(kw["tier"], 0) + 1
    priority_counts[kw["priority"]] = priority_counts.get(kw["priority"], 0) + 1
    lang = kw["language"]
    language_counts[lang] = language_counts.get(lang, 0) + 1
    pt = kw["page_type"]
    page_type_counts[pt] = page_type_counts.get(pt, 0) + 1
    intent = kw["intent"]
    intent_counts[intent] = intent_counts.get(intent, 0) + 1

unique_urls = len(set(kw["url_pattern"] for kw in keywords))

with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
    f.write("=" * 70 + "\n")
    f.write("  DIGITALSAATHI MASTER 100K+ SEO KEYWORD DATABASE SUMMARY\n")
    f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("=" * 70 + "\n\n")
    
    f.write(f"TOTAL KEYWORDS:      {len(keywords):,}\n")
    f.write(f"UNIQUE URL TARGETS:  {unique_urls:,}\n\n")
    
    f.write("KEYWORDS BY CLUSTER:\n")
    f.write("-" * 50 + "\n")
    for cluster, count in sorted(cluster_counts.items(), key=lambda x: -x[1]):
        pct = (count / len(keywords)) * 100
        bar = "█" * int(count // 1500)
        f.write(f"  {cluster:<25} {count:>8,}  ({pct:>5.1f}%)  {bar}\n")
    
    f.write(f"\nKEYWORDS BY TIER:\n")
    f.write("-" * 50 + "\n")
    f.write(f"  🔴 Tier 1 (High Priority):   {tier_counts.get(1, 0):>8,}  ({(tier_counts.get(1,0)/len(keywords))*100:>5.1f}%)\n")
    f.write(f"  🟠 Tier 2 (Medium Priority): {tier_counts.get(2, 0):>8,}  ({(tier_counts.get(2,0)/len(keywords))*100:>5.1f}%)\n")
    f.write(f"  🟢 Tier 3 (Long Tail):       {tier_counts.get(3, 0):>8,}  ({(tier_counts.get(3,0)/len(keywords))*100:>5.1f}%)\n")
    
    f.write(f"\nKEYWORDS BY PRIORITY:\n")
    f.write("-" * 50 + "\n")
    for p, c in sorted(priority_counts.items()):
        f.write(f"  {p:<10} {c:>8,}\n")
    
    f.write(f"\nKEYWORDS BY LANGUAGE:\n")
    f.write("-" * 50 + "\n")
    for lang, c in sorted(language_counts.items(), key=lambda x: -x[1]):
        f.write(f"  {lang:<10} {c:>8,}\n")
    
    f.write(f"\nKEYWORDS BY PAGE TYPE:\n")
    f.write("-" * 50 + "\n")
    for pt, c in sorted(page_type_counts.items(), key=lambda x: -x[1]):
        f.write(f"  {pt:<15} {c:>8,}\n")
    
    f.write(f"\nKEYWORDS BY INTENT:\n")
    f.write("-" * 50 + "\n")
    for intent, c in sorted(intent_counts.items(), key=lambda x: -x[1]):
        f.write(f"  {intent:<20} {c:>8,}\n")
    
    f.write("\n" + "=" * 70 + "\n")
    f.write("  PROGRAMMATIC SEO ARCHITECTURE ROADMAP\n")
    f.write("=" * 70 + "\n\n")
    f.write("1. Master Dataset Rule: 100,000+ Keyword Opportunities != 100,000 Thin Pages.\n")
    f.write(f"   -> Consolidate into {unique_urls:,} high-value dynamic page templates.\n")
    f.write("2. Phase 1 (Launch): Tools + Core Calculators + Top Tier 1 Central & State Jobs.\n")
    f.write("3. Phase 2 (Growth): MCA/BCA subjects + District & State Qualification Hubs.\n")
    f.write("4. Phase 3 (Scale): Dynamic query matching + Search Console feedback flywheel.\n")

print(f"\n🎉 Done! Files written:")
print(f"   📄 {OUTPUT_FILE}")
print(f"   📊 {SUMMARY_FILE}")
print(f"\n📈 Cluster breakdown:")
for cluster, count in sorted(cluster_counts.items(), key=lambda x: -x[1]):
    print(f"   {cluster:<25} {count:>8,}")
print(f"\n   {'TOTAL':<25} {len(keywords):>8,}")



