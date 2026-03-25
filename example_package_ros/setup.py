# Copyright 2024 Caleb Mossey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os
from glob import glob

package_name = 'example_package_ros'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        # Register package with ament index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include package.xml
        (os.path.join('share', package_name), ['package.xml']),
        # Include launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Include test files
        (os.path.join('share', package_name, 'test'), glob('test/*.py')),
    ],
    install_requires=['setuptools', 'example_package'],
    tests_require=['pytest'],
    zip_safe=True,
    maintainer='Example Name',
    maintainer_email='example@example.com',
    description='ROS-dependent example package',
    # license='TODO',
    entry_points={
        'console_scripts': [
            'example_node = example_package_ros.example_node:main',
            'advanced_example_node = example_package_ros.advanced_example_node:main',
        ],
    },
)
