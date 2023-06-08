import setuptools

version = "0.2.1"

with open("aix360/version.py", "w") as f:
    f.write('# generated by setup.py\nversion = "{}"\n'.format(version))

extra_requires = {
    "default": [
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
    ],
    "rbm": [
        "matplotlib",
        "pandas<=1.4.3",
        "scipy>=0.17",
        "scikit-learn<1.2.0",
        "cvxpy>=1.1",
    ],
    "profwt": [
        "keras==2.3.1",
        "scipy>=0.17",
        "tensorflow==1.14",
    ],
    "cofrnet": [
        "pandas<=1.4.3",
        "torch",
        "tqdm",
    ],
    "ted": [
        "pandas",
        "scikit-learn",
    ],
    "dipvae": [
        "matplotlib",
        "torch",
        "torchvision",
    ],
    "rule_induction": [
        "matplotlib",
        "numba",
        "pandas<=1.4.3",
        "scikit-learn",
        "nyoka",
        "cvxpy",
        "xmltodict==0.12.0",
    ],
    "lime": [
        "lime",
        "tqdm",
        "pandas",
    ],
    "matching": ["otoc @ git+https://github.com/IBM/otoc@main#egg=otoc"],
    "protodash": [
        "scikit-learn",
        "xport",
        "cvxpy",
        "requests",
    ],
    "contrastive": [
        "keras==2.3.1",
        "tensorflow==1.14",
        "requests",
        "scipy>=0.17",
        "scikit-image",
        "torch",
        "h5py<3.0.0",  # to resolve keras error: 'str' object has no attribute 'decode'
    ],
    "shap": [
        "keras==2.3.1",
        "tensorflow==1.14",
        "matplotlib",
        "numba",
        "pandas<=1.4.3",
        "shap",
        "tqdm",
    ],
    "nncontrastive": [
        "pandas<=1.4.3",
        "tensorflow==2.9.3",
    ],
    "tsice": [
        "pandas<=1.4.3",
        "scikit-learn",
        "scipy",
        "plotly",  # required for example notebook
        "ipython",  # required for example notebook
        "kaleido",  # required for example notebook
        "requests",  # for dataset
    ],
    "imd": [
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "networkx",
        "pygraphviz",  # for creating graph visualization
    ],
}

# minimal dependencies in install_requires
install_requires = extra_requires["default"]  # ted is supported by default.

setuptools.setup(
    name="aix360",
    version=version,
    description="IBM AI Explainability 360",
    authos="aix360 developers",
    url="https://github.com/IBM/AIX360",
    author_email="aix360@us.ibm.com",
    packages=setuptools.find_packages(),
    license="Apache License 2.0",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    extras_require=extra_requires,
    package_data={
        "aix360": [
            "data/*",
            "data/*/*",
            "data/*/*/*",
            "models/*",
            "models/*/*",
            "models/*/*/*",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
