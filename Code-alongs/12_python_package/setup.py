from setuptools import setup
from setuptools import find_packages

print(find_packages(exclude=["test*", "exploration"]))

# setup(
#     name="travel_planner",
#     version="0.0.1",
#     description="""
#     This package is used for travel planning in public transports.
#     It has backend, frontend, and utils.
#     """,
#     author="Sandra Nilsson",
#     author_email="sandra@gmail.com",
#     install_requires=["streamlit", "pandas", "requests", "folium", "python-dotenv"],
#     packages=find_packages(exclude=["test*", "exploration"]),
# )
