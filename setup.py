import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'york'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'model'), glob(os.path.join('model', '*.*'))),
        (os.path.join('share', package_name, 'model/meshes'), glob(os.path.join('model/meshes', '*.*'))),
        (os.path.join('share', package_name, 'model/urdf'), glob(os.path.join('model/urdf', '*.*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.*'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cmoralesd',
    maintainer_email='ctodo@todo.com',
    description='Paquete de pruebas para modelamiento y control del robot YORK',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
