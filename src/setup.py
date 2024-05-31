from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='MobileDogs',
   version='1.0',
   description='The "Mobile Dogs" project is a system for tracking stray dogs using wearable devices (collars).',
   license='MIT',
   author='Kuzmin Ilia, Nikiforova Darya',
   author_email='saharokbro@mail.ru, darya.n.2004@mail.ru',
   url='https://github.com/Darya778/MobileDogs',
   packages=['src'],
   install_requires=requirements,
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
