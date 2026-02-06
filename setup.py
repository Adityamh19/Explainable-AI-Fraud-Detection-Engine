from setuptools import setup, find_packages

setup(
    name="fintech_guardian",
    version="1.0.0",
    author="Your Name",
    description="Modular Fraud Detection Engine",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'xgboost',
        'scikit-learn',
        'imbalanced-learn',
        'joblib',
        'shap',
        'matplotlib',
        'requests',
        'pyyaml'
    ],
    python_requires=">=3.8"
)