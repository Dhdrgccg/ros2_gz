from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Добавляем директорию launch, если она будет
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ваше Имя',
    maintainer_email='user@example.com',
    description='Пакет для управления роботом в Gazebo',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_node = my_robot_controller.simple_node:main',
            'odom_listener = my_robot_controller.odom_listener:main',
            'robot_controller = my_robot_controller.robot_controller:main',
            'simple_controller = my_robot_controller.simple_controller:main',
        ],
    },
)
