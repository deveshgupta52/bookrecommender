from setuptools import setup
with open("README.md","r",encoding="utf-8") as f:
    long_description =  f.read()

REPO_NAME ="Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Devesh"
SRC_REPO ="src"
LIST_OF_REQUIREMENTS =[ 'streamlit','numpy']
setup(name=REPO_NAME,
      version="0.0.1",
      author=AUTHOR_USER_NAME,
      author_email="devesh@gmail916.com",
      description="A small package for Books Recommender System",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=[SRC_REPO],
      
      install_requires=LIST_OF_REQUIREMENTS,
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      python_requires=">=3.7")



