import subprocess

# Updated list of dependencies with latest versions
dependencies = [
    "Appium-Python-Client==3.1.1",
    "attrs==23.1.0",
    "certifi==2024.6.15",
    "cffi==1.16.0",
    "charset-normalizer==3.2.0",
    "decorator==5.1.1",
    "docutils==0.20.1",
    "et-xmlfile==1.1.0",
    "Faker==19.0.0",
    "h11==0.14.0",
    "idna==3.4",
    "imageio==2.31.1",
    "imutils==0.5.4",
    "kitchen==1.2.6",
    "lazy_loader==0.3",
    "natsort==8.4.0",
    "networkx==3.6.0",
    "numpy==1.24.3",
    "opencv-python-headless==4.9.3.6",
    "openpyxl==3.1.2",
    "outcome==1.3.0.post0",
    "packaging==23.1",
    "pillow==10.2.0",
    "PySocks==1.7.1",
    "python-dateutil==2.8.2",
    "requests==2.31.0",
    "robotframework==6.1.1",
    "robotframework-appiumlibrary==2.0.0",
    "robotframework-databaselibrary==1.4.3",
    "robotframework-excellib==2.0.1",
    "robotframework-imagecompare==0.2.0",
    "robotframework-pabot==2.16.0",
    "robotframework-pythonlibcore==4.3.0",
    "robotframework-retryfailed==0.2.0",
    "robotframework-seleniumlibrary==6.2.0",
    "robotframework-SikuliLibrary==2.0.3",
    "robotframework-stacktrace==0.4.1",
    "scikit-image==0.23.0",
    "scipy==1.12.0",
    "selenium==4.21.0",
    "setuptools==67.6.0",
    "six==1.16.0",
    "sniffio==1.3.0",
    "sortedcontainers==2.4.0",
    "tifffile==2024.1.30",
    "trio==0.23.2",
    "trio-websocket==0.11.1",
    "typing_extensions==4.9.0",
    "urllib3==2.1.0",
    "wheel==0.40.0",
    "wsproto==1.2.0",
]

# Install each dependency
for package in dependencies:
    subprocess.run(["pip", "install", package])