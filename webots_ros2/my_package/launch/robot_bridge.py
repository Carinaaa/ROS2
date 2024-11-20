from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Path to your URDF file
    urdf_file_path = os.path.join(
        os.getenv('AMENT_PREFIX_PATH', '/path/to/your/workspace/install'),
        'my_package',
        'urdf',
        'my_robot.urdf'
    )

    # Load robot_state_publisher with URDF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_file_path).read()}]
    )

    # Example publisher node (replace with your nodes)
    example_topic_publisher = Node(
        package='your_package_name',
        executable='example_topic_publisher',
        name='example_topic_publisher',
        output='screen',
    )

    # Foxglove ROS2 bridge (optional, if needed for external visualization)
    foxglove_bridge = Node(
        package='foxglove_bridge',
        executable='foxglove_bridge',
        name='foxglove_bridge',
        output='screen',
    )

    # Launch Description
    return LaunchDescription([
        robot_state_publisher,
        example_topic_publisher,
        foxglove_bridge,  # Comment this if Foxglove bridge is not required
    ])
