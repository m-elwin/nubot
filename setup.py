from setuptools import setup

package_name = 'nubot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/env-hooks', ['env-hooks/nubot.dsv']),
        ('share/' + package_name + '/worlds', ['worlds/nubot_world.sdf']),
        ('share/' + package_name + '/launch', ['launch/simulate.launch.xml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matthew Elwin',
    maintainer_email='elwin@northwestern.edu',
    description='A simulated robot with lidar',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
