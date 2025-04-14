from setuptools import setup, find_packages

setup(
    name="my-app",                    # Choose your package name
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A packaged Python app with app.py",
    packages=find_packages(),         # Automatically finds the my_app/ package
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'my-app = my_app.app:run'  # CLI: lets you run `my-app` from terminal
        ],
    },
)
