from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot',
            executable='walker',
            name='mimic',
            remappings=[
                ('/output/cmd_vel', '/my_robot/cmd_vel'),
            ]
        )
    ])
    
