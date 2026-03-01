from setuptools import find_packages, setup

package_name = 'ball_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools==58.2.0', 'numpy<2.0.0'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='yonatanchiel@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ball_tracker_node = ball_tracker.ball_tracker_node:main',
            'virtual_camera_node = ball_tracker.virtual_camera_node:main',
        ],
    },
)
