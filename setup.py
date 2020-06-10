from setuptools import setup


setup(
    name="AmpliPython",
    version="1.1",
    url="https://github.com/Alveona/AmpliPython",
    license="MIT",
    author="Alveona",
    author_email="pomavau@yandex.ru",
    description="AmpliPython is lightweight Amplitude Integration for event logging",
    long_description=__doc__,
    packages=["amplipython"],
    namespace_packages=["amplipython"],
    zip_safe=False,
    platforms="any",
    install_requires=["pydantic", "requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
