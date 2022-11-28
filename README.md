# o3d_ros_point_cloud_converter

This package implements functions to convert open3d point cloud into sensor_msgs/PointCloud2 ROS message (and vice versa)

### Dependencies

The library contains python modules which are dependent on the following 3rd-party libraries:
```
setuptools, numpy, open3d, rospy
```

### Installation

To install the o3d_ros_point_cloud_converter package on your system, clone the GitHub repository in a folder of your choice, open the cloned repository path in a terminal and run the following command

```
python3 -m pip install .
```

Instead if you want to install the package in "editable" or "develop" mode (to prevent the uninstall/install of the
package at every pkg modification) you have can run the following command:

```
python3 -m pip install -e .
```


## Usage

- __convert_cloud_from_o3d_to_ros__: this function converts the datatype of point cloud from Open3D to ROS PointCloud2
- __convert_cloud_from_ros_to_o3d__: this function converts the datatype of point cloud from ROS PointCloud2 to Open3D

## License

Distributed under the ```GPLv3``` License. See [LICENSE](LICENSE) for more information.

## Authors

The package is provided by:

- [Fabio Amadio](https://github.com/fabio-amadio) [Mantainer]
