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
        "title": "Python Freelancer Developer",
        "time": "Dec 2023 - Present",
        "company": "Upwork",
        "jobs": [
            {
                "title": "Ad Managers",
                "details": [
                    "Integrated Shopify APIs to retrieve product data and handled bulk operations with GraphQL to manage pagination data.",
                    "Integrated APIs from Facebook Ads, TikTok Business Manager, Snapchat Ads, Klaviyo APIs to obtain performance metrics.",
                    "Deployed code to Google App Engine using Flask and managed daily operations with Google Scheduler.",
                    "Exported data to CSV files for further analysis."
                ],
            },
            {
                "title": "Data Crawling:",
                "details": [
                    "Crawled data from both web and mobile applications.",
                    "Implemented multiprocessing to optimize data crawling performance.",
                    "Exported crawled data to CSV files for processing and analysis."
                ],
            },
        ]
    },
    {
        "title": "AI Software Developer",
        "time": "June 2022 - Jan 2024",
        "company": "Paracel Technology Solutions",
        "jobs": [
            {
                "title": "AI Tasks:",
                "details": [
                    "Researched and implemented code for various regression models including Random Forest, XGBoost, and Decision Tree.",
                    "Researched and implemented deep learning models for time-series tasks including LSTM, MLP, CNN, and LSTM-CNN.",
                    "Researched and implemented deep learning models such as YOLO and VGG16.",
                    "Research about LLM models."
                    "Researched and built a Graph Neural Network, utilizing Docker for containerization."
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
        "title": "Voice Recognition Based On Sex",
        "link": "https://github.com/alinh99/phanbietgiongnamnu",
        "details": [
            "Analyze, Filter, and Visualize Data",
            "Training Data with Machine Learning Models: XGBoost, Decision Tree, Random Forest",
            "Get results in each model (R^2, MSE, RMSE)"
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
            "Seaborn"
        ]
    },
    {
        "title": "House Price Prediction",
        "link": "https://github.com/alinh99/predict-house-price",
        "details": [
            "Training Data with Machine Learning Models: Linear Regression",
            "Predict House Price in the Model"
        ],
        "type": "Machine Learning",
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
            "Seaborn"
        ]
    },
    {
        "title": "Probability of Passing Prediction",
        "link": "https://github.com/alinh99/predict-the-probability-of-passing",
        "details": [
            "Training Data with Machine Learning Models: Logistic Regression",
            "Predict House Price in the Model"
        ],
        "type": "Machine Learning",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Numpy",
            "Matplotlib",
        ]
    },
    {
        "title": "Data Crawling from a website",
        "link": "https://github.com/alinh99/DataCrawling",
        "details": [
            "Crawl Data from website",
            "Export to CSV file"
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
        "title": "Shopify API",
        "link": "https://github.com/alinh99/pythonShopify",
        "details": [
            "Handle Bulk Operations in GraphQL",
            "Get Order and Product data",
            "Export CSV file"
        ],
        "type": "Shopify API",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "ShopifyAPI",
            "Pandas",
        ]
    },
    {
        "title": "TikTok API",
        "link": "#",
        "details": [
            "Get user data by tags",
            "Get metrics of Tiktok Business"
        ],
        "type": "Tiktok API",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Tiktok_business_api",
            "Pyktok",
            "Pandas"
        ]
    },
    {
        "title": "Odoo External API",
        "link": "#",
        "details": [
            "Integrate Odoo External API into an application using modules: Employees, HR, Payroll, Attendance",
        ],
        "type": "App",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Odoo Framework"
        ]
    },
    {
        "title": "Odoo Website API",
        "link": "#",
        "details": [
            "Integrate Odoo Website API to build a website in Odoo"
        ],
        "type": "Web",
        "language": "Python",
        "platform_developments": [
            "Windows",
            "Linux",
            "MacOS"
        ],
        "libraries": [
            "Odoo Framework"
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