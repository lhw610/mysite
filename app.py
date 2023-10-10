from flask import Flask, render_template, url_for
app = Flask(__name__)

# update the recent activities. The dictionary has list as value
# [event, word to put hyper link, hyperlink, optional next setnece]
recent_updates = {
    'May 2023 ': ['Our two-stage feature detection for FAST exam gudiance is accepted to IEEE IUS'],
    'May 2023': ['AI-based FAST Exam guidance was presented at Society for Academic Emergency Medicine (SAEM)'],
    'Dec 2022': ['Our work in automoated cerebral vessel detection is presented at International Symposium on Intracranial pressure and Brain Monitoring (ICP)'],
    'Oct 2022': ['Presented ','AI-based organ detection in ultrasound FAST exam', 'https://www.annemergmed.com/article/S0196-0644(22)00649-7/fulltext', ' at American College of Emergency Physicians (ACEP)'],
    'Sep 2022': ['AI Assistance to Acquire High-Quality FAST Exams is presented at Military Health System Research Symposium (MHSRS)'],
    'May 2022': ['Promoted to Data Scientist - AI Based Medical Ultrasound Imaging Analysis'],
    'June 2021': ['Co-authored research by developing cardiomyocytes segmentation model, ', "Cell states beyond transcriptomic","https://www.sciencedirect.com/science/article/pii/S2405471221001563", ' is publisehd to Cell Systems'],
    'Apr 2021': ['Our work in Automated ultrasound methods for cerebral blood flow velocity measurement is presented at Point of Care Ultrasound conference'],
    'Dec 2020': ['Allen Cell and Structure Segmenter is published to ','bioRxiv','https://www.biorxiv.org/content/10.1101/491035v2'],
    'July 2020': ['Started working as Assocaite Data Scientist at Ultrasound Application Group, Precision Diagnosis and Image-Guided Therapy, Philips Research'],
    'Dec 2019': ["Check out my Master's research on " ,'Semi-Supervised Brain MR Image Segmentation','https://arxiv.org/abs/1908.04466',' at Neurips 2019 ML4H'],
    'July 2019': ['Started my professional career as Scientific Data Engineer at Allen Institute!'],
    'May 2019': ['Graduated from Cornell University with Master in Biomedical Engineering'],
}

@app.route("/")
@app.route("/profile")
def index():
    return render_template('index.html', recent_updates=recent_updates)

@app.route("/projects")
def projects():
    return render_template('projects.html', title='projects')

@app.route("/publications")
def publications():
    return render_template('publications.html', title='publications')

if __name__ == "__main__":
    app.run(debug=True)
