from setuptools import setup

package_name = 'o3d_ros_point_cloud_converter'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[],
    install_requires=['setuptools', 'numpy', 'open3d'],
    zip_safe=True,
    maintainer='Fabio Amadio',
    maintainer_email='fabioamadio93@gmail.com',
    description='This package implements functions to convert open3d point cloud into sensor_msgs/PointCloud2 ROS message (and vice versa).',
    license='GNU GENERAL PUBLIC LICENSE v3',
    entry_points={},
)
