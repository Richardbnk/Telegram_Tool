import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='Telegram_Tool',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Robot Specialist Library for Robot Process Automation",
    url="https://github.com/Richardbnk/Telegram_Tool",
    packages=['telegram_tool'],
    
    py_modules = ['telegram'],
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
