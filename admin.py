from datetime import datetime

skills = {
            "Data Analyst": 90, 
            "Python": 90, 
            "API": 90, 
            "SQL": 80, 
            "Pytorch": 70, 
            "Tensorflow": 70, 
            "Machine Learning": 80
}

general_information = {
    "name": "Ryan Nguyen",
    "address": "Danang, Vietnam",
    "phone": "+84937739735",
    "email": "alinh1803@gmail.com",
    "age": f"{datetime.now().year - 2000}"
}

experience = [
    {
        "title": "Python Developer",
        "time": "March 2023 - June 2024",
        "company": "Paracel Technology Solutions",
        "jobs": [
            {
                "title": "Data Crawling:",
                "details": [
                    "Crawled data from both web and mobile applications.",
                    "Implemented multiprocessing to optimize data crawling performance.",
                    "Exported crawled data to CSV files for processing and analysis."
                ],
            },
            {
                "title": "AI Tasks:",
                "details": [
                    "Researched and implemented code for various regression models including Random Forest, XGBoost, and Decision Tree.",
                ]
            },
            {
                "title": "Odoo Tasks:",
                "details": [
                    "Implement external APIs and website APIs in Odoo projects.",
                    "Developed and customized specific modules in Odoo.",
                ]
            }
        ]
    },
]

projects = [
    {
        "title": "RUL Prediction",
        "link": "https://github.com/alinh99/CarAuctionPrediction",
        "details": [
            "Analyze, Filter, and Visualize Data",
            "Training Data with Deep Learning Models: LSTM, CNN, MLP",
            "Predict RUL in each Model"
        ],
        "type": "Data Analyst & Machine Learning",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Pandas",
            "Tensorflow",
            "Numpy",
            "Sklearn",
            "Seaborn"
        ]
    },
    {
        "title": "Car Auction Price Prediction",
        "link": "https://github.com/alinh99/CarAuctionPrediction",
        "details": [
            "Analyze, Filter, and Visualize Data",
            "Training Data with Machine Learning Models: Random Forest, XGBoost, Decision Tree, ...",
            "Predict Car Auction Price in each Model"
        ],
        "type": "Data Analyst & Machine Learning",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Pandas",
            "Numpy",
            "Matplotlib",
            "Sklearn",
            "Seaborn",
            "Xgboost",
            "Catboost",
            "Joblib",
            "LightGBM"
        ]
    },
    {
        "title": "Data Crawling from a website",
        "link": "https://github.com/alinh99/DataCrawling",
        "details": [
            "Crawl Data from website",
            "Export to CSV file",
            "Multi-processing handling"
        ],
        "type": "Web Crawling",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Selenium",
            "Pandas",
        ]
    },
    {
        "title": "English for IT",
        "link": "https://github.com/alinh99/eng_for_it",
        "details": [
            "Front-end and Back-end handling for this app",
            "Authentication: Firebase",
            "Functions: Help students learn 4 skills: Reading, Writing, Speaking, and Listening via tests and calculate points after these tests",
            "Data: Manual Input"
        ],
        "type": "App",
        "language": "Dart & Flutter",
        "platform_developments": [
            "Android"
        ],
        "libraries": [
            "Firebase",
            "Text to Speech",
            "Speech To Text"
        ]
    }
]