from setuptools import setup

package_name = 'nodecomh'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='halvor',
    maintainer_email='halvor@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'processing = nodecomh.processing_node:main',
            'receiver = nodecomh.receiver_node:main',
            'transmitter = nodecomh.transmitter_node:main'
        ],
    },
)
